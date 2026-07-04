import cv2
import numpy as np

# Camera index — 0 is iPhone via Continuity Camera
CAMERA_INDEX = 0

# Sample radius — averages pixels in this area to avoid noise/text
SAMPLE_RADIUS = 10

# Fixed center sticker colors (never need to be scanned)
FACE_CENTERS = {
    'U': 'Y',  # top center always yellow
    'D': 'W',  # bottom center always white
    'F': 'G',  # front center always green
    'R': 'O',  # right center always orange
    'B': 'B',  # back center always blue
    'L': 'R',  # left center always red
}

# Face scan order
FACE_ORDER = ['U', 'D', 'F', 'R', 'B', 'L']

# Will be computed once from frame size
sticker_centers = []

def validate_cube(cube_array):
    """Check each color appears exactly 9 times."""
    from collections import Counter
    counts = Counter(cube_array)
    expected = {'Y': 9, 'W': 9, 'G': 9, 'O': 9, 'B': 9, 'R': 9}
    return counts == expected

def compute_sticker_centers(frame):
    """Compute the 9 sticker sample points based on frame size."""
    h, w = frame.shape[:2]
    cube_size = int(min(h, w) * 0.6)
    cx, cy = w // 2, h // 2
    x1 = cx - cube_size // 2
    y1 = cy - cube_size // 2
    cell = cube_size // 3

    centers = []
    for row in range(3):
        for col in range(3):
            sx = x1 + col * cell + cell // 2
            sy = y1 + row * cell + cell // 2
            centers.append((sx, sy))
    return centers, x1, y1, cube_size, cell


def sample_color(frame, center):
    """Average BGR color in a small region around center point."""
    x, y = center
    region = frame[y - SAMPLE_RADIUS:y + SAMPLE_RADIUS,
                   x - SAMPLE_RADIUS:x + SAMPLE_RADIUS]
    if region.size == 0:
        return np.array([0, 0, 0])
    avg = region.mean(axis=(0, 1))
    return avg


def classify_color(bgr):
    """Classify a BGR color into one of 6 cube colors using HSV."""
    b, g, r = int(bgr[0]), int(bgr[1]), int(bgr[2])
    pixel = np.array([[[b, g, r]]], dtype=np.uint8)
    hsv = cv2.cvtColor(pixel, cv2.COLOR_BGR2HSV)[0][0]
    h, s, v = int(hsv[0]), int(hsv[1]), int(hsv[2])

    if v < 40:                      return 'X'  # too dark
    if s < 60:                      return 'W'  # low saturation = white
    if h < 10 or h > 170:          return 'R'  # red (wraps around)
    if 10 <= h < 25:               return 'O'  # orange
    if 25 <= h < 38:               return 'Y'  # yellow
    if 38 <= h < 85:               return 'G'  # green
    if 85 <= h < 130:              return 'B'  # blue
    if 130 <= h <= 170:            return 'R'  # red (upper)
    return 'X'  # unknown


def scan_face(frame, face_name):
    """Sample all 9 stickers on a face, injecting known center."""
    colors = []
    for idx, center in enumerate(sticker_centers):
        if idx == 4:  # center sticker — always known
            colors.append(FACE_CENTERS[face_name])
        else:
            bgr = sample_color(frame, center)
            color = classify_color(bgr)
            colors.append(color)
    return colors


def draw_overlay(frame, x1, y1, cube_size, cell, face_name, face_index):
    """Draw the alignment grid and live color labels on the frame."""
    overlay = frame.copy()
    x2 = x1 + cube_size
    y2 = y1 + cube_size

    # outer box
    cv2.rectangle(overlay, (x1, y1), (x2, y2), (0, 255, 0), 2)

    # grid lines
    for i in range(1, 3):
        cv2.line(overlay, (x1 + i * cell, y1), (x1 + i * cell, y2), (0, 255, 0), 1)
        cv2.line(overlay, (x1, y1 + i * cell), (x2, y1 + i * cell), (0, 255, 0), 1)

    # live color labels on each sticker
    for idx, (sx, sy) in enumerate(sticker_centers):
        if idx == 4:
            label = FACE_CENTERS[face_name]
            color_dot = (200, 200, 200)
        else:
            bgr = sample_color(frame, (sx, sy))
            label = classify_color(bgr)
            color_dot = (0, 0, 255)

        cv2.circle(overlay, (sx, sy), SAMPLE_RADIUS, color_dot, 2)
        cv2.putText(overlay, label, (sx - 8, sy + 6),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 0), 2)

    # instructions
    h = frame.shape[0]
    cv2.putText(overlay, f"Show face: {face_name}",
                (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv2.putText(overlay, "SPACE to capture | R to retake | Q to quit",
                (20, 80), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 1)
    cv2.putText(overlay, f"Face {face_index + 1}/6",
                (20, h - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 1)

    return overlay


def build_cube_array(captured):
    """
    Convert captured face colors into the 54-element cube array.
    Order: U, D, F, R, B, L (9 stickers each)
    """
    cube = []
    for face in FACE_ORDER:
        cube.extend(captured[face])
    return cube


def scan_cube():
    """
    Full scanning pipeline. Returns 54-element cube state array
    ready to pass into cube_state.load().
    """
    global sticker_centers

    cap = cv2.VideoCapture(CAMERA_INDEX)
    if not cap.isOpened():
        raise RuntimeError(f"Could not open camera at index {CAMERA_INDEX}")

    cap.set(cv2.CAP_PROP_BUFFERSIZE, 1)

    # warmup — give Continuity Camera time to initialize
    print("Warming up camera...")
    for _ in range(30):
        cap.read()

    # now read the first real frame
    ret, frame = cap.read()
    if not ret:
        raise RuntimeError("Could not read from camera")

    sticker_centers, x1, y1, cube_size, cell = compute_sticker_centers(frame)

    captured = {}
    face_index = 0

    print("Cube Scanner started.")
    print(f"First face to show: {FACE_ORDER[0]}")
    print("SPACE to capture | R to retake | Q to quit")

    while face_index < 6:
        ret, frame = cap.read()
        if not ret:
            break

        face_name = FACE_ORDER[face_index]
        overlay = draw_overlay(frame, x1, y1, cube_size, cell, face_name, face_index)
        cv2.imshow('Cube Scanner', overlay)

        key = cv2.waitKey(1) & 0xFF

        if key == ord(' '):
            colors = scan_face(frame, face_name)

            # check for any unknown colors before accepting
            if 'X' in colors:
                print(f"Warning: unknown color detected in {face_name}: {colors}")
                print("Retake recommended — press SPACE again to accept anyway or R to retake")
            else:
                captured[face_name] = colors
                print(f"Captured {face_name}: {colors}")
                face_index += 1
                if face_index < 6:
                    print(f"Next face: {FACE_ORDER[face_index]}")

        elif key == ord('f'):  # force accept even with X
            colors = scan_face(frame, face_name)
            captured[face_name] = colors
            print(f"Force captured {face_name}: {colors}")
            face_index += 1
            if face_index < 6:
                print(f"Next face: {FACE_ORDER[face_index]}")

        elif key == ord('r') and face_index > 0:
            face_index -= 1
            del captured[FACE_ORDER[face_index]]
            print(f"Retaking {FACE_ORDER[face_index]}")

        elif key == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

    if len(captured) < 6:
        raise RuntimeError(f"Scan incomplete — only got {len(captured)}/6 faces")

    cube_array = build_cube_array(captured)
    print(f"\nFull cube array ({len(cube_array)} stickers):")
    for i in range(0, 54, 9):
        print(f"  {FACE_ORDER[i // 9]}: {cube_array[i:i+9]}")
    if not validate_cube(cube_array):
        from collections import Counter
        print("Invalid scan — color counts:", Counter(cube_array))
        raise RuntimeError("Cube state is invalid, rescan needed")
    return cube_array


# run standalone for testing
if __name__ == "__main__":
    result = scan_cube()
    print("\nReady to solve:", result)