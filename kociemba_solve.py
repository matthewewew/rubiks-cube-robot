import kociemba
import cube as cube_state
from scan import scan_cube
from esp32 import CubeBot

# kociemba uses a different face order and color notation
# it expects: U R F D L B, each face top-left to bottom-right
# colors represented as U/R/F/D/L/B (which face that color belongs to)

def convert_to_kociemba(cube_array):
    """
    Convert our cube array to kociemba format string.
    Our order: U D F R B L
    Kociemba order: U R F D L B
    Color map: Y=U, W=D, G=F, O=R, B=B, R=L
    """
    color_map = {
        'Y': 'U',  # yellow = up face
        'W': 'D',  # white = down face
        'G': 'F',  # green = front face
        'O': 'R',  # orange = right face
        'B': 'B',  # blue = back face
        'R': 'L',  # red = left face
    }

    # our cube array slices
    U = cube_array[0:9]
    D = cube_array[9:18]
    F = cube_array[18:27]
    R = cube_array[27:36]
    B = cube_array[36:45]
    L = cube_array[45:54]

    # kociemba wants U R F D L B order
    kociemba_order = U + R + F + D + L + B
    return ''.join(color_map[c] for c in kociemba_order)

def main():
    print("Starting scan...")
    cube_state.load(scan_cube())
    print("Scan complete, solving...")

    # cube_state.load([
    # 'R', 'O', 'R', 'R', 'Y', 'B', 'B', 'Y', 'O', 
    # 'O', 'W', 'R', 'Y', 'W', 'W', 'W', 'W', 'Y', 
    # 'R', 'R', 'B', 'G', 'G', 'G', 'G', 'O', 'Y', 
    # 'Y', 'Y', 'Y', 'W', 'O', 'Y', 'G', 'B', 'O', 
    # 'B', 'B', 'W', 'G', 'B', 'R', 'G', 'R', 'O', 
    # 'G', 'B', 'W', 'G', 'R', 'O', 'B', 'O', 'W'])

    kociemba_string = convert_to_kociemba(cube_state.cube)
    print(f"Kociemba input: {kociemba_string}")

    solution = kociemba.solve(kociemba_string)
    print(f"Kociemba solution: {solution}")

    moves = solution.split()
    print(f"Moves: {len(moves)}")

    try:
        bot = CubeBot(port='COM3')
        bot.send_sequence(moves)
        bot.close()
    except Exception as e:
        print(f"ESP32 not connected: {e}")
        print("Moves ready to send when bot is connected.")

if __name__ == "__main__":
    main()