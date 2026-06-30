import cube as cube_state
from cube import cube
from solver.moves import *  # grab all the move functions at once

def solve_first_layer():
    ######################################################
    #Post White Cross. Assume yellow is on top, green front.
    #First Layer Corners:
    ########################################################

    #Defining corner pieces so we can find where the specific corner pieces are
    def ftrCorner():
        return {cube[i] for i in (8, 20, 27)}

    def ftlCorner():
        return {cube[i] for i in (6, 18, 47)}

    def fbotlCorner():
        return {cube[i] for i in (9, 24, 53)}

    def fbotrCorner():
        return {cube[i] for i in (11, 26, 33)}


    def btrCorner():
        return {cube[i] for i in (2, 29, 36)}

    def btlCorner():
        return {cube[i] for i in (0, 38, 45)}

    def bbotlCorner():
        return {cube[i] for i in (15, 44, 51)}

    def bbotrCorner():
        return {cube[i] for i in (17, 35, 42)}


    #Solve green, orange, white corner
    while ((cube[26] != 'G') or (cube[33] != 'O') or (cube[11] != 'W')):
        
        if ftrCorner() == {'G', 'O', 'W'} or fbotrCorner() == {'G', 'O', 'W'}: 
            while (cube[26] != 'G') or (cube[33] != 'O') or (cube[11] != 'W'):
                sexyFront()
            break
        elif fbotlCorner() == {'G', 'O', 'W'}:      
            while (ftlCorner() != {'G', 'O', 'W'}):
                sexyLeft()        
            topRight()

            while (cube[26] != 'G') or (cube[33] != 'O') or (cube[11] != 'W'):
                sexyFront()
            break
        elif bbotrCorner() == {'G', 'O', 'W'}:
            while (btrCorner() != {'G', 'O', 'W'}):
                sexyRight()
            topLeft()

            while (cube[26] != 'G') or (cube[33] != 'O') or (cube[11] != 'W'):
                sexyFront()
            break

        elif bbotlCorner() == {'G', 'O', 'W'}:
            while (btlCorner() != {'G', 'O', 'W'}):
                sexyBack()

            topRight()
            topRight()

            while (cube[26] != 'G') or (cube[33] != 'O') or (cube[11] != 'W'):
                sexyFront()
            break
        else:
            topLeft()
            
            
        
    #Solve green, red, white corner
    while (cube[24] != 'G') or (cube[53] != 'R') or (cube[9] != 'W'):
        if ftlCorner() == {'G', 'R', 'W'} or fbotlCorner() == {'G', 'R', 'W'}: 
                while (cube[24] != 'G') or (cube[53] != 'R') or (cube[9] != 'W'):
                    sexyLeft()
                break
        elif fbotrCorner() == {'G', 'R', 'W'}:      
                while (ftrCorner() != {'G', 'R', 'W'}):
                    sexyFront()        
                topLeft()
                

                while (cube[24] != 'G') or (cube[53] != 'R') or (cube[9] != 'W'):
                    sexyLeft()
                break
        elif bbotrCorner() == {'G', 'R', 'W'}:
                while (btrCorner() != {'G', 'R', 'W'}):
                    sexyRight()
                topLeft()
                topLeft()
                
                

                while (cube[24] != 'G') or (cube[53] != 'R') or (cube[9] != 'W'):
                    sexyLeft()
                break

        elif bbotlCorner() == {'G', 'R', 'W'}:
                while (btlCorner() != {'G', 'R', 'W'}):
                    sexyBack()
                topRight()

                while (cube[24] != 'G') or (cube[53] != 'R') or (cube[9] != 'W'):
                    sexyLeft()
                break

        else:
                topLeft()
                

    #Solve white, blue, red corner
    while (cube[15] != 'W') or (cube[44] != 'B') or (cube[51] != 'R'):
        if btlCorner() == {'B', 'R', 'W'} or bbotlCorner() == {'B', 'R', 'W'}: 
                while (cube[15] != 'W') or (cube[44] != 'B') or (cube[51] != 'R'):
                    sexyBack()
                break
        elif fbotrCorner() == {'B', 'R', 'W'}:      
                while (ftrCorner() != {'B', 'R', 'W'}):
                    sexyFront()        
                topLeft()
                topLeft()
                
                

                while (cube[15] != 'W') or (cube[44] != 'B') or (cube[51] != 'R'):
                    sexyBack()
                break
        elif bbotrCorner() == {'B', 'R', 'W'}:
                while (btrCorner() != {'B', 'R', 'W'}):
                    sexyRight()
                topRight()

                while (cube[15] != 'W') or (cube[44] != 'B') or (cube[51] != 'R'):
                    sexyBack()
                break

        elif fbotlCorner() == {'B', 'R', 'W'}:
                while (ftlCorner() != {'B', 'R', 'W'}):
                    sexyLeft()
                topLeft()
                
                

                while (cube[15] != 'W') or (cube[44] != 'B') or (cube[51] != 'R'):
                    sexyBack()
                break

        else:
                topLeft()
                

    #Solve white, orange, blue corner   
    while (cube[17] != 'W') or (cube[35] != 'O') or (cube[42] != 'B'):
        if btrCorner() == {'B', 'O', 'W'} or bbotrCorner() == {'B', 'O', 'W'}: 
                while (cube[17] != 'W') or (cube[35] != 'O') or (cube[42] != 'B'):
                    sexyRight()
                break
        elif bbotlCorner() == {'B', 'O', 'W'}:      
                while (btlCorner() != {'B', 'O', 'W'}):
                    sexyBack()        
                topLeft()

                while (cube[17] != 'W') or (cube[35] != 'O') or (cube[42] != 'B'):
                    sexyRight()
                break
        elif fbotrCorner() == {'B', 'O', 'W'}:
                while (ftrCorner() != {'B', 'O', 'W'}):
                    sexyFront()
                topRight()

                while (cube[17] != 'W') or (cube[35] != 'O') or (cube[42] != 'B'):
                    sexyRight()
                break

        elif fbotlCorner() == {'B', 'O', 'W'}:
                while (ftlCorner() != {'B', 'O', 'W'}):
                    sexyLeft()
                topLeft()
                topLeft()

                while (cube[17] != 'W') or (cube[35] != 'O') or (cube[42] != 'B'):
                    sexyRight()
                break

        else:
                topLeft()