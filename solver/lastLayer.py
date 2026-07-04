from cube import cube
from cube import is_solved
from solver.moves import *

def solve_last_layer():
    print("Last layer input state:")
    for i in range(0, 54, 9):
        print(cube[i:i+9])

    #Redefining corner pieces so we can find where the specific corner pieces are
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

    #################################
    # POST F2L: Creating Yellow Cross
    #################################

    while((cube[1] != 'Y') or (cube[3] != 'Y') or (cube[5] != 'Y') or (cube[7] != 'Y')):

        #Angle Cases
        if((cube[1] == 'Y') and (cube[3] == 'Y')):
                topRight()
                topRight()

        elif((cube[1] == 'Y') and (cube[5] == 'Y')):
                topLeft()
        
        elif((cube[3] == 'Y') and (cube[7] == 'Y')):
                topRight()

        if((cube[5] == 'Y') and (cube[7] == 'Y')):
                frontRight()
                sexyFront()
                frontLeft()
        
        #fixing vertical line scenario
        if((cube[1] == 'Y') and (cube[7] == 'Y')):
                topLeft() 
        #Horizontal line
        if((cube[3] == 'Y') and (cube[5] == 'Y')):
                frontRight()
                sexyFront()
                frontLeft()
        if((cube[1] != 'Y') and (cube[3] != 'Y')\
            and (cube[5] != 'Y') and (cube[7] != 'Y')):
                frontRight()
                sexyFront()
                frontLeft()

    ###########################
    # POST F2L AND YELLOW CROSS
    ########################### 

    #Solving Yellow Corners
    while(cube[0] != 'Y' or cube[2] != 'Y' or cube[6] != 'Y' or cube[8] != 'Y'):
        while(cube[6] != 'Y'):
                upsideDownSexyFront()
        topRight()


    while(cube[6] != 'Y'):
        upsideDownSexyFront()
    #Find Headlights

    def frontHeadlights():
        return [cube[i] for i in (18, 20)]

    def rightHeadlights():
        return [cube[i] for i in (27, 29)]

    def backHeadlights():
        return [cube[i] for i in (36, 38)]

    def leftHeadlights():
        return [cube[i] for i in (45, 47)]

    #See if a set of headlights exists
    def hasHeadlights(headlights):
        if headlights == ['G', 'G']\
                or headlights == ['O', 'O']\
                or headlights == ['B', 'B']\
                or headlights == ['R', 'R']:
            
            return True
        else:
            return False
        

    # #testing:
    # print(
    #     frontHeadlights(),
    #     rightHeadlights(),
    #     backHeadlights(),
    #     leftHeadlights()
    # )

    #Checking that corners are in right place
    def cornersPermuted():
        corners = {frozenset(c) for c in [ftlCorner(), ftrCorner(), btrCorner(), btlCorner()]}
        expected = {frozenset(e) for e in [{'Y','R','G'}, {'Y','O','G'}, {'Y','O','B'}, {'Y','R','B'}]}
        return corners == expected
    
    while not cornersPermuted():
        print("corners:", ftlCorner(), ftrCorner(), btrCorner(), btlCorner())
        print("permuted:", cornersPermuted())
        #Checking for front headlights
        if hasHeadlights(frontHeadlights()):
                tPermRight()
                break

        #Checking for right headlights
        elif hasHeadlights(rightHeadlights()):
                tPermBack()
                break

        #Checking for back headlights
        elif hasHeadlights(backHeadlights()):
                tPermLeft()
                break

        #Checking for left headlights
        elif hasHeadlights(leftHeadlights()):
                tPermFront()
                break

        else:
                tPermFront()

    #Full front top bars for final moves
    def frontBar():
        return [cube[i] for i in (18, 19, 20)]

    def rightBar():
        return [cube[i] for i in (27, 28, 29)]

    def backBar():
        return [cube[i] for i in (36, 37, 38)]

    def leftBar():
        return [cube[i] for i in (45, 46, 47)]

    #Functions to check if a bar is filled by a color
    def isGBar(bar):
        return bar == ['G','G','G']

    def isOBar(bar):
        return bar == ['O','O','O']

    def isBBar(bar):
        return bar == ['B','B','B']

    def isRBar(bar):
        return bar == ['R','R','R']

    #check if cube is solved
    while not (isGBar(frontBar()) and isOBar(rightBar()) and isBBar(backBar()) and isRBar(leftBar())):
        #Check for green bar for final moves
        print("bars:", frontBar(), rightBar(), backBar(), leftBar())
        print("cube[19]:", cube[19], "cube[28]:", cube[28], "cube[37]:", cube[37], "cube[46]:", cube[46])
        if isGBar(frontBar()) or isGBar(rightBar()) or isGBar(backBar()) or isGBar(leftBar()):         
                if rightBar() == ['G', 'G', 'G']:
                    topLeft()
                    #print("1")

                elif backBar() == ['G', 'G', 'G']:
                    topLeft()
                    topLeft()
                    #print("2")

                elif leftBar() == ['G', 'G', 'G']:
                    topRight()
                    #print("3")

                if frontBar() == ['G', 'G', 'G']:
                    if cube[28] == 'B':
                            uPermFront()
                            break
                    elif cube[28] == 'R':
                            luPermFront()
                            break
                    #print("4")                  

        #Search for orange bar
        elif isOBar(frontBar()) or isOBar(rightBar()) or isOBar(backBar()) or isOBar(leftBar()):
                if backBar() == ['O', 'O', 'O']:
                    topLeft()
                    #print("5")

                elif leftBar() == ['O', 'O', 'O']:
                    topLeft()
                    topLeft()
                    #print("6")

                elif frontBar() == ['O', 'O', 'O']:
                    topRight()
                    #print("7")

                if rightBar() == ['O', 'O', 'O']:
                    if cube[37] == 'R':
                            uPermRight()
                            break
                    elif cube[37] == 'G':
                            luPermRight()
                            break
                    #print("8")

        #Search for blue bar
        elif isBBar(frontBar()) or isBBar(rightBar()) or isBBar(backBar()) or isBBar(leftBar()):
                print("here")
                if leftBar() == ['B', 'B', 'B']:
                    topLeft()
                    #print("9")

                elif frontBar() == ['B', 'B', 'B']:
                    topLeft()
                    topLeft()
                    #print("10")

                elif rightBar() == ['B', 'B', 'B']:
                    topRight()
                    #print("11")

                if backBar() == ['B', 'B', 'B']:
                    if cube[46] == 'G':
                            uPermBack()
                            break
                    elif cube[46] == 'O':
                            luPermBack()
                            break
                    #print("12")
                    print(cube)

        #Search for red bar
        elif isRBar(frontBar()) or isRBar(rightBar()) or isRBar(backBar()) or isRBar(leftBar()):
                print("here")
                if frontBar() == ['R', 'R', 'R']:
                    topLeft()
                    #print("13")

                elif rightBar() == ['R', 'R', 'R']:
                    topLeft()
                    topLeft()
                    #print("14")

                elif backBar() == ['R', 'R', 'R']:
                    topRight()
                    #print("15")

                if leftBar() == ['R', 'R', 'R']:
                    if cube[19] == 'O':
                            uPermLeft()
                            break
                    elif cube[19] == 'B':
                            luPermLeft()
                            break
                    #print("16")

        else:
                uPermFront()
                #print("17")

    #Check for misaligned top:
    while not is_solved():
        topRight()