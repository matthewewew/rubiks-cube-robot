import cube as cube_state
from solver.whiteCross import solve_white_cross
from solver.firstLayer import solve_first_layer
from solver.secondLayer import solve_second_layer
from solver.lastLayer import solve_last_layer



def main():
    cube_state.load([
      'G', 'O', 'Y', 'Y', 'Y', 'W', 'B', 'W', 'B', 
      'W', 'Y', 'G', 'O', 'W', 'B', 'R', 'R', 'R', 
      'R', 'B', 'O', 'Y', 'G', 'B', 'G', 'G', 'Y', 
      'W', 'R', 'O', 'R', 'O', 'R', 'O', 'O', 'B', 
      'B', 'W', 'W', 'G', 'B', 'G', 'Y', 'Y', 'Y', 
      'O', 'O', 'W', 'W', 'R', 'B', 'G', 'G', 'R'])
    
    solve_white_cross()
    solve_first_layer()
    solve_second_layer()
    solve_last_layer()
    
    print("Moves:", len(cube_state.standardNotationMoves))
    print(', '.join(cube_state.standardNotationMoves))
    
    if cube_state.is_solved():
        print("Cube solved!")
    else:
        print("Something went wrong...")
        for i in range(0, 54, 9):
            print(cube_state.cube[i:i+9])

if __name__ == "__main__":
    main()

from esp32 import CubeBot

# inside main(), after solve stages:
if cube_state.is_solved():
    bot = CubeBot(port='/dev/tty.usbserial-0001')  # Windows: 'COM3', Mac/Linux: '/dev/tty.usbserial-0001'
    bot.send_sequence(cube_state.standardNotationMoves)
    bot.close()