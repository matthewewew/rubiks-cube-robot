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

    def solveFtrCorner():
        if fbotrCorner() == {'G', 'O', 'W'}:
            if cube[11] == 'W':
                return
            elif cube[26] == 'W':   # front face = sexyFront
                invSexyFront()
            elif cube[33] == 'W':   # right face = invSexyFront
                sexyFront()
        elif ftrCorner() == {'G', 'O', 'W'}:
            if cube[8] == 'W':
                sexyFront()
            elif cube[20] == 'W':   # front face = sexyFront
                invSexyFront()
            elif cube[27] == 'W':   # right face = invSexyFront
                sexyFront()
        if (cube[26] != 'G') or (cube[33] != 'O') or (cube[11] != 'W'):
            solveFtrCorner()

    def solveFtlCorner():
        if fbotlCorner() == {'G', 'R', 'W'}:
            if cube[9] == 'W':
                return
            elif cube[24] == 'W':   # front face = sexyLeft
                sexyLeft()
            elif cube[53] == 'W':   # left face = invSexyLeft
                invSexyLeft()
        elif ftlCorner() == {'G', 'R', 'W'}:
            if cube[6] == 'W':
                sexyLeft()
            elif cube[18] == 'W':   # front face = sexyLeft
                sexyLeft()
            elif cube[47] == 'W':   # left face = invSexyLeft
                invSexyLeft()
        if (cube[24] != 'G') or (cube[53] != 'R') or (cube[9] != 'W'):
            solveFtlCorner()

    def solveBtlCorner():
        if bbotlCorner() == {'B', 'R', 'W'}:
            if cube[15] == 'W':
                return
            elif cube[44] == 'W':   # back face = sexyBack
                invSexyBack()
            elif cube[51] == 'W':   # left face = invSexyBack
                sexyBack()
        elif btlCorner() == {'B', 'R', 'W'}:
            if cube[0] == 'W':
                sexyBack()
            elif cube[38] == 'W':   # back face = sexyBack
                invSexyBack()
            elif cube[45] == 'W':   # left face = invSexyBack
                sexyBack()
        if (cube[15] != 'W') or (cube[44] != 'B') or (cube[51] != 'R'):
            solveBtlCorner()

    def solveBtrCorner():
        if bbotrCorner() == {'B', 'O', 'W'}:
            if cube[17] == 'W':
                return
            elif cube[42] == 'W':   # back face = sexyRight
                sexyRight()
            elif cube[35] == 'W':   # right face = invSexyRight
                invSexyRight()
        elif btrCorner() == {'B', 'O', 'W'}:
            if cube[2] == 'W':
                sexyRight()
            elif cube[36] == 'W':   # back face = sexyRight
                sexyRight()
            elif cube[29] == 'W':   # right face = invSexyRight
                invSexyRight()
        if (cube[17] != 'W') or (cube[35] != 'O') or (cube[42] != 'B'):
            solveBtrCorner()

    #Solve green, orange, white corner
    while ((cube[26] != 'G') or (cube[33] != 'O') or (cube[11] != 'W')):
        
        if ftrCorner() == {'G', 'O', 'W'} or fbotrCorner() == {'G', 'O', 'W'}: 
            solveFtrCorner()
            break

        elif fbotlCorner() == {'G', 'O', 'W'}:      
            while (ftlCorner() != {'G', 'O', 'W'}):
                sexyLeft()        
            topRight()

            solveFtrCorner()
            break
        elif bbotrCorner() == {'G', 'O', 'W'}:
            while (btrCorner() != {'G', 'O', 'W'}):
                sexyRight()
            topLeft()

            solveFtrCorner()
            break
        elif bbotlCorner() == {'G', 'O', 'W'}:
            while (btlCorner() != {'G', 'O', 'W'}):
                sexyBack()
            topRight()
            topRight()

            solveFtrCorner()
            break
        else:
            topLeft()

    print(f"ftr corner after insert: {[cube[26], cube[33], cube[11]]} | Should be: ['G', 'O', 'W']")

        
    #Solve green, red, white corner
    while (cube[24] != 'G') or (cube[53] != 'R') or (cube[9] != 'W'):
        if ftlCorner() == {'G', 'R', 'W'} or fbotlCorner() == {'G', 'R', 'W'}: 
                solveFtlCorner()
                break
        elif fbotrCorner() == {'G', 'R', 'W'}:      
                while (ftrCorner() != {'G', 'R', 'W'}):
                    sexyFront()        
                topLeft()
                
                solveFtlCorner()
                break
        elif bbotrCorner() == {'G', 'R', 'W'}:
                while (btrCorner() != {'G', 'R', 'W'}):
                    sexyRight()
                topLeft()
                topLeft()
                
                solveFtlCorner()
                break

        elif bbotlCorner() == {'G', 'R', 'W'}:
                while (btlCorner() != {'G', 'R', 'W'}):
                    sexyBack()
                topRight()

                solveFtlCorner()
                break
        else:
                topLeft()
                
    print(f"ftl corner after insert: {[cube[24], cube[53], cube[9]]} | Should be: ['G', 'R', 'W']")
    #Solve white, blue, red corner
    while (cube[15] != 'W') or (cube[44] != 'B') or (cube[51] != 'R'):
        if btlCorner() == {'B', 'R', 'W'} or bbotlCorner() == {'B', 'R', 'W'}: 
                solveBtlCorner()
                break
        elif fbotrCorner() == {'B', 'R', 'W'}:      
                while (ftrCorner() != {'B', 'R', 'W'}):
                    sexyFront()        
                topLeft()
                topLeft()
                
                solveBtlCorner()
                break
        elif bbotrCorner() == {'B', 'R', 'W'}:
                while (btrCorner() != {'B', 'R', 'W'}):
                    sexyRight()
                topRight()

                solveBtlCorner()
                break

        elif fbotlCorner() == {'B', 'R', 'W'}:
                while (ftlCorner() != {'B', 'R', 'W'}):
                    sexyLeft()
                topLeft()
                
                solveBtlCorner()
                break

        else:
                topLeft()
                
    print(f"btl corner after insert: {[cube[44], cube[51], cube[15]]} | Should be: ['B', 'R', 'W']")

    #Solve white, orange, blue corner   
    while (cube[17] != 'W') or (cube[35] != 'O') or (cube[42] != 'B'):
        if btrCorner() == {'B', 'O', 'W'} or bbotrCorner() == {'B', 'O', 'W'}: 
                solveBtrCorner()
                break
        elif bbotlCorner() == {'B', 'O', 'W'}:      
                while (btlCorner() != {'B', 'O', 'W'}):
                    sexyBack()        
                topLeft()

                solveBtrCorner()
                break
        elif fbotrCorner() == {'B', 'O', 'W'}:
                while (ftrCorner() != {'B', 'O', 'W'}):
                    sexyFront()
                topRight()

                solveBtrCorner()
                break
        elif fbotlCorner() == {'B', 'O', 'W'}:
                while (ftlCorner() != {'B', 'O', 'W'}):
                    sexyLeft()
                topLeft()
                topLeft()

                solveBtrCorner()
                break
        else:
                topLeft()

    print(f"btr corner after insert: {[cube[42], cube[35], cube[17]]} | Should be: ['B', 'O', 'W']")

    print("First layer end state:")
    for i in range(0, 54, 9):
        print(cube[i:i+9])