import cv2
import numpy as np
from collections import Counter

# ---------------- Config ----------------
CAMERA_INDEX = 0        # phone camera (Continuity Camera / DroidCam)
WARP_SIZE = 300         # rectified face patch is WARP_SIZE x WARP_SIZE
CELL = WARP_SIZE // 3
SAMPLE_HALF = 15        # half-size of the square sampled inside each sticker cell
DETECT_WIDTH = 640      # frames are downscaled to this width for detection
STABLE_FRAMES = 3       # consecutive detections needed before the outline locks on
MIN_STICKERS = 5        # stickers that must be found to fit the 3x3 grid
WINDOW = "Cube Scanner"
FONT = cv2.FONT_HERSHEY_SIMPLEX

WARP_DST = np.array([[0, 0], [WARP_SIZE - 1, 0],
                     [WARP_SIZE - 1, WARP_SIZE - 1], [0, WARP_SIZE - 1]], dtype="float32")

# Fixed center sticker colors (never scanned)
FACE_CENTERS = {'U': 'Y', 'D': 'W', 'F': 'G', 'R': 'O', 'B': 'B', 'L': 'R'}
FACE_ORDER = ['U', 'D', 'F', 'R', 'B', 'L']

# Display colors for swatches/labels
SWATCH_BGR = {'Y': (0, 255, 255), 'W': (255, 255, 255), 'G': (0, 200, 0),
              'O': (0, 140, 255), 'B': (255, 80, 0), 'R': (0, 0, 230), 'X': (90, 90, 90)}


# ---------------- Color classification ----------------
def classify_color(bgr):
    """Classify a BGR color into one of 6 cube colors using HSV."""
    b, g, r = int(bgr[0]), int(bgr[1]), int(bgr[2])
    pixel = np.array([[[b, g, r]]], dtype=np.uint8)
    hsv = cv2.cvtColor(pixel, cv2.COLOR_BGR2HSV)[0][0]
    h, s, v = int(hsv[0]), int(hsv[1]), int(hsv[2])

    if v < 40:              return 'X'  # too dark
    if s < 60:              return 'W'  # low saturation = white
    if h < 10 or h > 170:   return 'R'  # red (wraps around)
    if 10 <= h < 25:        return 'O'
    if 25 <= h < 38:        return 'Y'
    if 38 <= h < 85:        return 'G'
    if 85 <= h < 130:       return 'B'
    if 130 <= h <= 170:     return 'R'
    return 'X'


def validate_cube(cube_array):
    """Each color must appear exactly 9 times."""
    return Counter(cube_array) == {'Y': 9, 'W': 9, 'G': 9, 'O': 9, 'B': 9, 'R': 9}


# ---------------- Sticker detection ----------------
def find_sticker_candidates(small):
    """
    Find square-ish regions enclosed by edges. On a stickered cube these are
    the stickers inside the black plastic; on a stickerless cube they're the
    piece faces between the grooves. Returns (cx, cy, side, angle_rad) tuples.
    """
    h, w = small.shape[:2]
    frame_area = h * w
    gray = cv2.cvtColor(small, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (5, 5), 0)

    cands = []
    # two sensitivity levels: faint grooves (stickerless) and strong edges (stickered)
    for lo, hi in ((12, 36), (30, 90)):
        edges = cv2.Canny(gray, lo, hi)
        edges = cv2.dilate(edges, np.ones((3, 3), np.uint8), iterations=1)
        n, labels, stats, _ = cv2.connectedComponentsWithStats(255 - edges, connectivity=4)

        for i in range(1, n):
            x, y, bw, bh, area = stats[i]
            if not (0.0015 * frame_area < area < 0.06 * frame_area):
                continue
            if x == 0 or y == 0 or x + bw >= w or y + bh >= h:   # touches border
                continue
            if max(bw, bh) > 1.8 * min(bw, bh):
                continue

            mask = (labels[y:y + bh, x:x + bw] == i).astype(np.uint8)
            cnts, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            cnt = max(cnts, key=cv2.contourArea)
            (cx, cy), (rw, rh), ang = cv2.minAreaRect(cnt)
            if min(rw, rh) < 6 or max(rw, rh) / min(rw, rh) > 1.35:
                continue
            if area / (rw * rh) < 0.72:                  # must fill its bounding square
                continue
            hull_area = cv2.contourArea(cv2.convexHull(cnt))
            if hull_area == 0 or area / hull_area < 0.88:  # must be convex-ish
                continue
            cands.append((cx + x, cy + y, np.sqrt(rw * rh), np.deg2rad(ang)))

    # merge duplicates found by both passes
    cands.sort(key=lambda c: -c[2])
    merged = []
    for c in cands:
        if all(np.hypot(c[0] - m[0], c[1] - m[1]) > 0.5 * m[2] for m in merged):
            merged.append(c)
    return merged


def _fit_lattice(pts, sides, angs):
    """
    Fit a 3x3 grid to a group of sticker centers. Returns (quad, inlier_count)
    in the same coordinates as pts, or None.
    """
    if len(pts) < MIN_STICKERS:
        return None

    # dominant grid angle (stickers are squares, so angles repeat every 90 deg)
    theta = np.arctan2(np.mean(np.sin(4 * angs)), np.mean(np.cos(4 * angs))) / 4

    # pitch = center-to-center distance between neighbors
    d = np.linalg.norm(pts[:, None] - pts[None], axis=2)
    np.fill_diagonal(d, np.inf)
    pitch = np.median(d.min(axis=1))
    side = np.median(sides)
    if not (0.95 * side < pitch < 1.9 * side):
        return None

    # express each center in grid units around the sticker nearest the middle
    ref = pts[np.argmin(np.linalg.norm(pts - pts.mean(axis=0), axis=1))]
    c, s = np.cos(-theta), np.sin(-theta)
    uv = (pts - ref) @ np.array([[c, -s], [s, c]]).T / pitch
    idx = np.round(uv).astype(int)
    resid = np.abs(uv - idx).max(axis=1)
    ok = resid < 0.35
    if ok.sum() < MIN_STICKERS:
        return None

    # find the 3x3 window holding the most stickers
    best = None
    iu, iv = idx[ok, 0], idx[ok, 1]
    for ou in range(iu.min(), iu.max() - 1):
        for ov in range(iv.min(), iv.max() - 1):
            inside = (iu >= ou) & (iu <= ou + 2) & (iv >= ov) & (iv <= ov + 2)
            if best is None or inside.sum() > best[0]:
                best = (inside.sum(), ou, ov)
    if best is None or best[0] < MIN_STICKERS:
        return None
    _, ou, ov = best

    # one detection per cell, keep the best-centered one
    cells = {}
    for k in np.where(ok)[0]:
        col, row = idx[k, 0] - ou, idx[k, 1] - ov
        if 0 <= col <= 2 and 0 <= row <= 2:
            if (col, row) not in cells or resid[k] < resid[cells[(col, row)]]:
                cells[(col, row)] = k
    cols = {cr[0] for cr in cells}
    rows = {cr[1] for cr in cells}
    if len(cells) < MIN_STICKERS or cols != {0, 1, 2} or rows != {0, 1, 2}:
        return None   # grid isn't pinned down in both directions yet

    # perspective-correct mapping from the flat 300x300 face to the image
    src = np.array([[(cr[0] + 0.5) * CELL, (cr[1] + 0.5) * CELL] for cr in cells], dtype="float32")
    dst = np.array([pts[k] for k in cells.values()], dtype="float32")
    H, mask = cv2.findHomography(src, dst, cv2.RANSAC, 0.2 * pitch)
    if H is None or mask.sum() < MIN_STICKERS:
        return None

    quad = cv2.perspectiveTransform(WARP_DST.reshape(-1, 1, 2), H).reshape(4, 2)
    if not cv2.isContourConvex(quad.astype(np.float32).reshape(-1, 1, 2)):
        return None
    area = cv2.contourArea(quad.astype(np.float32))
    if not (0.5 * (3 * pitch) ** 2 < area < 2.0 * (3 * pitch) ** 2):
        return None
    return quad, int(mask.sum())


def find_face_quad(frame):
    """
    Locate the cube face. Returns (quad, sticker_points), both in
    full-resolution coordinates; quad is None if no face was found.
    """
    h, w = frame.shape[:2]
    scale = DETECT_WIDTH / w
    small = cv2.resize(frame, (DETECT_WIDTH, int(h * scale)))

    cands = find_sticker_candidates(small)
    stickers = np.array([[c[0], c[1]] for c in cands]).reshape(-1, 2) / scale
    if len(cands) < MIN_STICKERS:
        return None, stickers

    pts = np.array([[c[0], c[1]] for c in cands])
    sides = np.array([c[2] for c in cands])
    angs = np.array([c[3] for c in cands])

    # background clutter can also look like squares, so try grouping around
    # each candidate (similar size, nearby) and keep the best grid fit
    best = None
    for i in range(len(cands)):
        near = np.linalg.norm(pts - pts[i], axis=1) < 4.5 * sides[i]
        similar = (sides > 0.7 * sides[i]) & (sides < 1.4 * sides[i])
        group = near & similar
        if group.sum() < MIN_STICKERS:
            continue
        fit = _fit_lattice(pts[group], sides[group], angs[group])
        if fit and (best is None or fit[1] > best[1]):
            best = fit
            if fit[1] == 9:
                break

    if best is None:
        return None, stickers
    return best[0] / scale, stickers


class QuadTracker:
    """Smooths detections over frames so the outline doesn't jitter or flicker."""

    def __init__(self):
        self.reset()

    def reset(self):
        self.pts, self.hits, self.misses = None, 0, 0

    def update(self, pts, frame):
        if pts is None:
            self.misses += 1
            if self.misses > 6:
                self.reset()
            return
        self.misses = 0
        diag = np.hypot(*frame.shape[:2])
        if self.pts is None or np.max(np.linalg.norm(pts - self.pts, axis=1)) > 0.08 * diag:
            self.pts, self.hits = pts, 1        # big jump: start tracking the new position
        else:
            self.pts = 0.5 * self.pts + 0.5 * pts
            self.hits += 1

    @property
    def locked(self):
        return self.pts is not None and self.hits >= STABLE_FRAMES


# ---------------- Sampling ----------------
def warp_face(frame, quad):
    M = cv2.getPerspectiveTransform(quad.astype("float32"), WARP_DST)
    return cv2.warpPerspective(frame, M, (WARP_SIZE, WARP_SIZE))


def scan_warped_face(warped, face_name):
    """Sample the 8 outer stickers; median ignores glare and logo text."""
    colors = []
    for idx in range(9):
        if idx == 4:
            colors.append(FACE_CENTERS[face_name])
            continue
        row, col = divmod(idx, 3)
        cx, cy = col * CELL + CELL // 2, row * CELL + CELL // 2
        region = warped[cy - SAMPLE_HALF:cy + SAMPLE_HALF, cx - SAMPLE_HALF:cx + SAMPLE_HALF]
        bgr = np.median(region.reshape(-1, 3), axis=0)
        colors.append(classify_color(bgr))
    return colors


def build_cube_array(captured):
    cube = []
    for face in FACE_ORDER:
        cube.extend(captured.get(face, ['X'] * 9))
    return cube


# ---------------- Drawing ----------------
def _draw_header(view, face_name, status, status_color):
    w = view.shape[1]
    ui = max(1.0, w / 1280)
    lines = [
        (f"Show face: {face_name}  ({FACE_ORDER.index(face_name) + 1}/6)", 1.0, (0, 255, 0)),
        (status, 0.6, status_color),
        ("SPACE capture | F force | R back one face | Q quit", 0.55, (255, 255, 255)),
    ]
    y = int(40 * ui)
    for text, size, col in lines:
        cv2.putText(view, text, (20, y), FONT, size * ui, (0, 0, 0), 4)
        cv2.putText(view, text, (20, y), FONT, size * ui, col, 2)
        y += int(35 * ui)


def draw_searching_view(frame, stickers, face_name):
    view = frame.copy()
    ui = max(1.0, view.shape[1] / 1280)
    for x, y in stickers:   # show what it's picking up so you can tell it's working
        cv2.circle(view, (int(x), int(y)), int(5 * ui), (200, 200, 200), -1)
    _draw_header(view, face_name, "Searching for cube face... hold it flat to the camera", (0, 165, 255))
    return view


def draw_capture_view(frame, quad, warped, colors, face_name):
    view = frame.copy()
    h, w = view.shape[:2]
    ui = max(1.0, w / 1280)
    Minv = cv2.getPerspectiveTransform(WARP_DST, quad.astype("float32"))

    # outline + inner grid lines, projected onto the cube
    cv2.polylines(view, [quad.astype(np.int32)], True, (0, 255, 0), max(2, int(3 * ui)))
    for i in (1, 2):
        t = i * CELL
        seg = np.array([[[t, 0]], [[t, WARP_SIZE]], [[0, t]], [[WARP_SIZE, t]]], dtype="float32")
        p = cv2.perspectiveTransform(seg, Minv).reshape(-1, 2).astype(int)
        cv2.line(view, tuple(p[0]), tuple(p[1]), (0, 255, 0), max(1, int(2 * ui)))
        cv2.line(view, tuple(p[2]), tuple(p[3]), (0, 255, 0), max(1, int(2 * ui)))

    # detected color on each sticker
    centers = np.array([[[(i % 3) * CELL + CELL / 2, (i // 3) * CELL + CELL / 2]]
                        for i in range(9)], dtype="float32")
    proj = cv2.perspectiveTransform(centers, Minv).reshape(-1, 2)
    r = int(14 * ui)
    for (x, y), c in zip(proj, colors):
        p = (int(x), int(y))
        cv2.circle(view, p, r, SWATCH_BGR[c], -1)
        cv2.circle(view, p, r, (0, 0, 0), 2)
        cv2.putText(view, c, (p[0] - int(7 * ui), p[1] + int(6 * ui)), FONT, 0.55 * ui, (0, 0, 0), 2)

    # rectified preview, top right
    ps = int(180 * ui)
    prev = cv2.resize(warped, (ps, ps))
    for i in (1, 2):
        cv2.line(prev, (i * ps // 3, 0), (i * ps // 3, ps), (0, 255, 0), 1)
        cv2.line(prev, (0, i * ps // 3), (ps, i * ps // 3), (0, 255, 0), 1)
    view[10:10 + ps, w - 10 - ps:w - 10] = prev
    cv2.rectangle(view, (w - 10 - ps, 10), (w - 10, 10 + ps), (255, 255, 255), 2)

    _draw_header(view, face_name, "Face locked - check the colors, then SPACE", (0, 255, 0))
    return view


# Click-cycle order puts commonly confused colors next to each other
# (white<->yellow, orange<->red, green<->blue) so most fixes are one click.
CYCLE = ['W', 'Y', 'O', 'R', 'G', 'B']
NET_POS = {'U': (1, 0), 'L': (0, 1), 'F': (1, 1), 'R': (2, 1), 'B': (3, 1), 'D': (1, 2)}
REVIEW_SW, REVIEW_GAP, REVIEW_TOP = 52, 20, 95


class ReviewState:
    """Shared between the mouse callback and the review loop."""

    def __init__(self, captured):
        self.captured = captured
        self.active = False       # clicks only do something on the review screen
        self.selected = None      # (face, idx) of the last clicked sticker
        self.rects = {}           # (face, idx) -> (x1, y1, x2, y2)

    def hit(self, x, y):
        for key, (x1, y1, x2, y2) in self.rects.items():
            if x1 <= x <= x2 and y1 <= y <= y2:
                return key
        return None

    def set_color(self, key, color):
        face, idx = key
        old = self.captured[face][idx]
        self.captured[face][idx] = color
        print(f"Edited {face}[{idx}]: {old} -> {color}")

    def cycle(self, key, step):
        face, idx = key
        cur = self.captured[face][idx]
        nxt = CYCLE[(CYCLE.index(cur) + step) % len(CYCLE)] if cur in CYCLE else CYCLE[0]
        self.set_color(key, nxt)


def on_review_mouse(event, x, y, flags, state):
    if not state.active or event not in (cv2.EVENT_LBUTTONDOWN, cv2.EVENT_RBUTTONDOWN):
        return
    key = state.hit(x, y)
    if key is None:
        state.selected = None
        return
    if key[1] == 4:               # centers are fixed by the cube's orientation
        return
    state.selected = key
    state.cycle(key, 1 if event == cv2.EVENT_LBUTTONDOWN else -1)


def draw_review(state):
    captured = state.captured
    sw, gap, top = REVIEW_SW, REVIEW_GAP, REVIEW_TOP
    face_px = sw * 3
    width = 4 * (face_px + gap) + gap
    height = top + 3 * (face_px + gap) + 80
    img = np.full((height, width, 3), 30, np.uint8)
    state.rects = {}

    for n, face in enumerate(FACE_ORDER):
        gx, gy = NET_POS[face]
        ox, oy = gap + gx * (face_px + gap), top + gy * (face_px + gap)
        for i, c in enumerate(captured.get(face, ['X'] * 9)):
            row, col = divmod(i, 3)
            x1, y1 = ox + col * sw, oy + row * sw
            x2, y2 = x1 + sw - 3, y1 + sw - 3
            state.rects[(face, i)] = (x1, y1, x2, y2)
            cv2.rectangle(img, (x1, y1), (x2, y2), SWATCH_BGR[c], -1)
            cv2.putText(img, c, (x1 + sw // 2 - 8, y1 + sw // 2 + 6), FONT, 0.55, (0, 0, 0), 2)
            if i == 4:            # mark fixed centers
                cv2.rectangle(img, (x1 + 3, y1 + 3), (x2 - 3, y2 - 3), (60, 60, 60), 1)
            if state.selected == (face, i):
                cv2.rectangle(img, (x1 - 2, y1 - 2), (x2 + 2, y2 + 2), (255, 0, 255), 3)
        cv2.putText(img, f"{n + 1}: {face}", (ox, oy - 6), FONT, 0.5, (255, 255, 255), 1)

    cube = build_cube_array(captured)
    valid = validate_cube(cube)
    counts = Counter(cube)

    cv2.putText(img, "Review scan - click a sticker to fix it", (gap, 32), FONT, 0.75, (255, 255, 255), 2)
    x = gap
    for c in "YWGOBR":            # per-color counts, red if not 9
        n = counts.get(c, 0)
        cv2.putText(img, f"{c}:{n}", (x, 68), FONT, 0.6, (0, 255, 0) if n == 9 else (0, 0, 255), 2)
        x += 70
    if counts.get('X'):
        cv2.putText(img, f"?:{counts['X']}", (x, 68), FONT, 0.6, (0, 0, 255), 2)

    lines = ["Left click: next color | Right click: previous | or click then type Y W G O B R",
             "SPACE confirm | 1-6 retake a face | Q quit" if valid else
             "Every color needs exactly 9 - fix stickers or press 1-6 to retake | Q quit"]
    cv2.putText(img, lines[0], (gap, height - 45), FONT, 0.45, (200, 200, 200), 1)
    cv2.putText(img, lines[1], (gap, height - 20), FONT, 0.45,
                (255, 255, 255) if valid else (0, 140, 255), 1)
    return img, valid


# ---------------- Main scan loop ----------------
def scan_cube():
    cap = cv2.VideoCapture(CAMERA_INDEX)
    if not cap.isOpened():
        raise RuntimeError(f"Could not open camera at index {CAMERA_INDEX}")
    cap.set(cv2.CAP_PROP_BUFFERSIZE, 1)

    print("Warming up camera...")
    for _ in range(30):
        cap.read()

    tracker = QuadTracker()
    captured = {}
    pending = list(FACE_ORDER)
    history = []

    review = ReviewState(captured)
    cv2.namedWindow(WINDOW)
    cv2.setMouseCallback(WINDOW, on_review_mouse, review)
    color_keys = {ord(c.lower()): c for c in CYCLE} | {ord(c): c for c in CYCLE}

    try:
        while True:
            # ---- review screen once every face is captured ----
            if not pending:
                review.active = True
                img, valid = draw_review(review)
                cv2.imshow(WINDOW, img)
                key = cv2.waitKey(30) & 0xFF
                if key == ord(' ') and valid:
                    break
                if key in color_keys and review.selected:
                    review.set_color(review.selected, color_keys[key])
                elif ord('1') <= key <= ord('6'):
                    face = FACE_ORDER[key - ord('1')]
                    pending, history = [face], []
                    review.active, review.selected = False, None
                    tracker.reset()
                    print(f"Retaking {face}")
                elif key in (ord('q'), 27):
                    raise RuntimeError("Scan aborted by user.")
                continue

            # ---- live capture ----
            ret, frame = cap.read()
            if not ret:
                raise RuntimeError("Lost camera feed")

            face_name = pending[0]
            quad, stickers = find_face_quad(frame)
            tracker.update(quad, frame)

            colors = None
            if tracker.locked:
                warped = warp_face(frame, tracker.pts)
                colors = scan_warped_face(warped, face_name)
                view = draw_capture_view(frame, tracker.pts, warped, colors, face_name)
            else:
                view = draw_searching_view(frame, stickers, face_name)

            cv2.imshow(WINDOW, view)
            key = cv2.waitKey(1) & 0xFF

            if key in (ord(' '), ord('f')):
                if colors is None:
                    print("No face locked yet - hold the cube flat toward the camera")
                    continue
                if key == ord(' ') and 'X' in colors:
                    print(f"Unknown color on {face_name}: {colors} - reposition, or F to force")
                    continue
                captured[face_name] = colors
                history.append(face_name)
                pending.pop(0)
                tracker.reset()
                print(f"Captured {face_name}: {colors}")
            elif key == ord('r') and history:
                prev = history.pop()
                captured.pop(prev, None)
                pending.insert(0, prev)
                tracker.reset()
                print(f"Back to {prev}")
            elif key == ord('q'):
                raise RuntimeError("Scan aborted by user.")
    finally:
        cap.release()
        cv2.destroyAllWindows()

    return build_cube_array(captured)


if __name__ == "__main__":
    result = scan_cube()
    print("\nFinal 54-element array:")
    for i in range(0, 54, 9):
        print(f"  {FACE_ORDER[i // 9]}: {result[i:i + 9]}")