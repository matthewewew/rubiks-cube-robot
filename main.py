import cube as cube_state
from solver.whiteCross import solve_white_cross
from solver.firstLayer import solve_first_layer
from solver.secondLayer import solve_second_layer
from solver.lastLayer import solve_last_layer
from scan import scan_cube
from esp32 import CubeBot

def main():
    print("Starting scan...")
    cube_state.load(scan_cube())
    print("Scan complete, solving...")

    # cube_state.load([
    #   'W', 'Y', 'W', 'Y', 'Y', 'W', 'Y', 'Y', 'Y', 
    #   'W', 'W', 'W', 'W', 'W', 'W', 'Y', 'Y', 'Y', 
    #   'G', 'R', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 
    #   'O', 'B', 'R', 'O', 'O', 'R', 'O', 'O', 'R', 
    #   'B', 'O', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 
    #   'O', 'G', 'R', 'O', 'R', 'R', 'O', 'R', 'R'])

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