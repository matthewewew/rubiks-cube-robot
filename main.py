import cube as cube_state
from solver.whiteCross import solve_white_cross
from solver.firstLayer import solve_first_layer
from solver.secondLayer import solve_second_layer
from solver.lastLayer import solve_last_layer
from scan import scan_cube
from esp32 import CubeBot

def main():
    print("Starting scan...")
    #cube_state.load(scan_cube())
    print("Scan complete, solving...")

    cube_state.load([
    'B', 'O', 'B', 'Y', 'Y', 'R', 'Y', 'Y', 'R', 
    'G', 'W', 'W', 'W', 'W', 'G', 'W', 'W', 'G', 
    'O', 'B', 'W', 'Y', 'G', 'Y', 'Y', 'G', 'O', 
    'G', 'G', 'R', 'O', 'O', 'O', 'B', 'O', 'O', 
    'Y', 'W', 'Y', 'B', 'B', 'B', 'W', 'B', 'B', 
    'O', 'G', 'G', 'R', 'R', 'R', 'R', 'R', 'R'])

    solve_white_cross()
    solve_first_layer()
    solve_second_layer()
    solve_last_layer()

    print("Moves:", len(cube_state.standardNotationMoves))
    print(', '.join(cube_state.standardNotationMoves))

    if cube_state.is_solved():
        print("Cube solved!")
        try:
            bot = CubeBot(port='COM5')
            bot.send_sequence(cube_state.standardNotationMoves)
            bot.close()
        except Exception as e:
            print(f"ESP32 not connected: {e}")
            print("Moves ready to send when bot is connected.")
    else:
        print("Something went wrong...")
        for i in range(0, 54, 9):
            print(cube_state.cube[i:i+9])

if __name__ == "__main__":
    main()