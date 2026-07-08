from cube import cube  # imports the actual list object
from solver.moves import topRight, topLeft, frontLeft, frontRight, leftDown, leftUp, \
    rightDown, rightUp, backLeft, backRight, bottomLeft, bottomRight




def solve_white_cross():
    
    #######################################
    #START OF WHITE CROSS CODE; RED-WHITE EDGE
    ####################################### 
    #top -- 1 (top-back)


    if cube[1] == 'R' and cube[37] == 'W':
        backLeft()
        leftUp()
        print('in top\n')
    elif cube[1] == 'W' and cube[37] == 'R':
        topRight()
        leftUp()
        leftUp()
        print('in top-\n')
        
    #top -- 2 (left)
    elif cube[3] == 'R' and cube[46] == 'W':
        leftDown()
        frontLeft()
        bottomLeft()
        print('in top 2\n')
    elif cube[3] == 'W' and cube[46] == 'R':
        leftDown()
        leftDown()
        print('in top 2-\n')
    #top -- 3 (bottom)
    elif cube[7] == 'W' and cube[19] == 'R':
        frontLeft()
        frontLeft()
        bottomLeft()
        print('in top 3\n')
    elif cube[7] == 'R' and cube[19] == 'W':
        frontLeft()
        leftDown()
        print('in top 3-\n')
    #top -- 4 (right)
    elif cube[5] == 'W' and cube[28] == 'R':
        topLeft()
        topLeft()
        leftUp()
        leftUp()
        print('in top 4\n')
    elif cube[5] == 'R' and cube[28] == 'W':
        rightDown()
        frontRight()
        bottomLeft()
        print('in top 4-\n')
    #middle -- 1 (back-left)
    elif cube[41] == 'W' and cube[48] == 'R':
        leftUp()
        print('in mid 1\n')
    elif cube[41] == 'R' and cube[48] == 'W':
        bottomLeft()
        backLeft()
        bottomRight()
        
        print('in mid 1-\n')
    #middle -- 2 (front-left)
    elif cube[21] == 'W' and cube[50] == 'R':
        leftDown()
        print('in mid 2\n')
    elif cube[21] == 'R' and cube[50] == 'W':
        frontLeft()
        bottomLeft()
        print('in mid 2-\n')
    #middle -- 3 (front-right)
    elif cube[23] == 'W' and cube[30] == 'R':
        rightDown()
        bottomRight()
        bottomRight()
        print('in mid 3\n')
    elif cube[23] == 'R' and cube[30] == 'W':
        frontRight()
        bottomLeft()
        print('in mid 3-\n')
    #middle -- 4 (back-right)
    elif cube[32] == 'W' and cube[39] == 'R':
        backRight()
        bottomRight()
        print('in mid 4\n')
    elif cube[32] == 'R' and cube[39] == 'W':
        rightUp()
        bottomLeft()
        bottomLeft()
        print('in mid 4-\n')
    #bottom -- 1 (bottom-Left edge)
    elif cube[12] == 'R' and cube[52] == 'W':
        leftDown()
        backLeft()
        bottomRight()
        print('in bot 1\n')
        #Another Elif not needed because it would be where 
        #its supposed to be
        
    #bottom - 2 (bottom-front edge)
    elif cube[25] == 'W' and cube[10] == 'R':
        frontRight()
        leftDown()
        print('in bot 2\n')
    elif cube[25] == 'R' and cube[10] == 'W':
        bottomLeft()
        print('in bot 2-\n')
    #bottom - 3 (bottom-right edge)
    elif cube[14] == 'R' and cube[34] == 'W':
        bottomLeft()
        frontRight()
        leftDown()
        print('in bot 3\n')
    elif cube[14] == 'W' and cube[34] == 'R':
        bottomRight()
        bottomRight()
        print('in bot 3-\n')
    #bottom - 4 (bottom-back edge)
    elif cube[16] == 'W' and cube[43] == 'R':
        bottomRight()
        print('in bot 4\n')
    elif cube[16] == 'R' and cube[43] == 'W':
        backRight()
        leftUp()
        print('in bot 4-\n')

    print(cube[9:18])
    ##############################
    #BLUE-WHITE EDGE
    ##############################
    #top -- 1 (top-Back)
    if cube[1] == 'B' and cube[37] == 'W':
        topLeft()
        rightUp()
        backRight()
    elif cube[1] == 'W' and cube[37] == 'B':
        backRight()
        backRight()
    #top -- 2 (top-left edge)
    elif cube[3] == 'B' and cube[46] == 'W':
        topLeft()
        topLeft()
        rightUp()
        backRight()
    elif cube[3] == 'W' and cube[46] == 'B':
        topLeft()
        backRight()
        backRight()
    #top -- 3 (top-front edge)
    elif cube[7] == 'W' and cube[19] == 'B':
        topRight()
        topRight()
        backLeft()
        backLeft()
    elif cube[7] == 'B' and cube[19] == 'W':
        topRight()
        rightUp()
        backRight()
    #top -- 4 (top-right)
    elif cube[5] == 'W' and cube[28] == 'B':
        topRight()
        backLeft()
        backLeft()
    elif cube[5] == 'B' and cube[28] == 'W':
        rightUp()
        backRight()
    #middle -- 1 (back-left)
    elif cube[41] == 'W' and cube[48] == 'B':
        bottomRight()
        leftUp()
        bottomLeft()
    elif cube[41] == 'B' and cube[48] == 'W':
        backLeft()
    #middle -- 2 (front-left)
    elif cube[21] == 'W' and cube[50] == 'B':
        bottomLeft()
        leftDown()
        bottomRight()
    elif cube[21] == 'B' and cube[50] == 'W':
        bottomLeft()
        bottomLeft()
        frontLeft()
        bottomLeft()
        bottomLeft()
    #middle -- 3 (front-right)
    elif cube[23] == 'W' and cube[30] == 'B':
        bottomLeft()
        rightDown()
        bottomRight()
    elif cube[23] == 'B' and cube[30] == 'W':
        bottomRight()
        bottomRight()
        frontRight()
        bottomLeft()
        bottomLeft()
    #middle -- 4 (back-right)
    elif cube[32] == 'W' and cube[39] == 'B':
        backRight()
    elif cube[32] == 'B' and cube[39] == 'W':
        bottomLeft()
        rightUp()
        bottomRight()
    #bottom -- 1 (bottom-Left edge) not possible
    #elif cube[12] == 'B' and cube[52] == 'W':
        #leftDown()
        #backLeft()
    # elif cube[12] == 'W' and cube[52] == 'B':
    #       leftUp()
    #       leftUp()
    #       topLeft()
    #       backRight()
    #       backRight()
    #bottom - 2 (bottom-front edge)
    elif cube[25] == 'B' and cube[10] == 'W':
        frontLeft()
        frontLeft()
        topRight()
        topRight()
        backRight()
        backRight()
    elif cube[25] == 'W' and cube[10] == 'B':
        frontLeft()
        bottomLeft()
        rightDown()
        bottomRight()
    #bottom - 3 (bottom-right edge)
    elif cube[14] == 'W' and cube[34] == 'B':
        rightUp()
        bottomLeft()
        rightDown()
        bottomRight()
    elif cube[14] == 'B' and cube[34] == 'W':
        rightDown()
        backRight()
    #bottom - 4 (bottom-back edge)
    # THIS IS THE PREFERRED SPOT
    # elif cube[16] == 'W' and cube[43] == 'B':

    elif cube[16] == 'B' and cube[43] == 'W':
        backLeft()
        bottomLeft()
        rightUp()
        bottomRight()

    print(cube[9:18])
    ##############################
    #ORANGE-WHITE EDGE
    ##############################

    #TOP -- 1 (TOP BACK EDGE)
    if cube[1] == 'O' and cube[37] == 'W':
        topLeft()
        rightDown()
        bottomLeft()
        frontRight()
        bottomRight()
    elif cube[1] == 'W' and cube[37] == 'O':
        topLeft()
        rightUp()
        rightUp()
    #top -- 2 (top-left edge)
    elif cube[3] == 'O' and cube[46] == 'W':
        topRight()
        frontRight()
        rightDown()
    elif cube[3] == 'W' and cube[46] == 'O':
        topRight()
        topRight()
        rightDown()
        rightDown()
    #top -- 3 (top-front edge)
    elif cube[7] == 'W' and cube[19] == 'O':
        topRight()
        rightUp()
        rightUp()
    elif cube[7] == 'O' and cube[19] == 'W':
        frontRight()
        rightDown()
    #top -- 4 (top-right)
    elif cube[5] == 'W' and cube[28] == 'O':
        rightDown()
        rightDown()
    elif cube[5] == 'O' and cube[28] == 'W':
        topLeft()
        frontRight()
        rightDown()
    #middle -- 1 (back-left)
    elif cube[41] == 'W' and cube[48] == 'O':
        bottomLeft()
        bottomLeft()
        leftUp()
        bottomRight()
        bottomRight()
    elif cube[41] == 'O' and cube[48] == 'W':
        bottomRight()
        backLeft()
        bottomLeft()

    #middle -- 2 (front-left)
    elif cube[21] == 'W' and cube[50] == 'O':
        frontRight()
        frontRight()
        rightDown()
    elif cube[21] == 'O' and cube[50] == 'W':
        bottomLeft()
        frontLeft()
        bottomRight()
    #middle -- 3 (front-right)
    elif cube[23] == 'W' and cube[30] == 'O':
        rightDown()
    elif cube[23] == 'O' and cube[30] == 'W':
        bottomLeft()
        frontRight()
        bottomRight()
    #middle -- 4 (back-right)
    elif cube[32] == 'W' and cube[39] == 'O':
        bottomRight()
        backRight()
        bottomLeft()
    elif cube[32] == 'O' and cube[39] == 'W':
        rightDown()
    # #bottom -- 1 (bottom-Left edge) cannot be here
    # elif cube[12] == 'O' and cube[52] == 'W':
    #       leftUp()
    #       bottomRight()
    #       frontLeft()
    #       bottomLeft()
    # elif cube[12] == 'W' and cube[52] == 'O':
    #       leftUp()
    #       bottomRight()
    #       bottomRight()
    #       leftDown()
    #       bottomLeft()
    #       bottomLeft()
    #bottom - 2 (bottom-front edge)
    elif cube[25] == 'O' and cube[10] == 'W':
        frontLeft()
        bottomLeft()
        frontRight()
        bottomRight()
    elif cube[25] == 'W' and cube[10] == 'O':
        frontLeft()
        rightDown()

    #bottom - 3 (bottom-right edge)
    # Ideal Spot
    # elif cube[14] == 'W' and cube[34] == 'O':

    elif cube[14] == 'O' and cube[34] == 'W':
        rightUp()
        bottomLeft()
        frontRight()
        bottomRight()

    #bottom - 4 (bottom-back edge) - cannot be here
    # elif cube[16] == 'W' and cube[43] == 'O':
    #       backLeft()
    #       bottomLeft()
    #       backRight()
    #       bottomRight()
    # elif cube[16] == 'O' and cube[43] == 'W':
    #       backLeft()
    #       rightUp()

    ##############################
    #Green-WHITE EDGE
    ##############################

    #TOP -- 1 (TOP BACK EDGE)
    if cube[1] == 'G' and cube[37] == 'W':
        topLeft()
        rightDown()
        frontRight()
        rightUp()
    elif cube[1] == 'W' and cube[37] == 'G':
        topLeft()
        topLeft()
        frontRight()
        frontRight()
    #top -- 2 (top-left edge)
    elif cube[3] == 'G' and cube[46] == 'W':
        bottomLeft()
        leftDown()
        bottomRight()
        frontLeft()

    elif cube[3] == 'W' and cube[46] == 'G':
        topRight()
        frontLeft()
        frontLeft()
    #top -- 3 (top-front edge)
    elif cube[7] == 'W' and cube[19] == 'G':
        frontRight()
        frontRight()
    elif cube[7] == 'G' and cube[19] == 'W':
        frontRight()
        bottomRight()
        rightDown()
        bottomLeft()
    #top -- 4 (top-right)
    elif cube[5] == 'W' and cube[28] == 'G':
        topLeft()
        frontRight()
        frontRight()

    elif cube[5] == 'G' and cube[28] == 'W':
        topLeft()
        frontRight()
        bottomRight()
        rightDown()
        bottomLeft()
    #middle -- 1 (back-left)
    elif cube[41] == 'W' and cube[48] == 'G':
        bottomLeft()
        leftUp()
        bottomRight()

    elif cube[41] == 'G' and cube[48] == 'W':
        bottomRight()
        bottomRight()
        backLeft()
        bottomRight()
        bottomRight()
    #middle -- 2 (front-left)
    elif cube[21] == 'W' and cube[50] == 'G':
        bottomLeft()
        leftDown()
        bottomRight()
    elif cube[21] == 'G' and cube[50] == 'W':
        frontLeft()
    #middle -- 3 (front-right)
    elif cube[23] == 'W' and cube[30] == 'G':
        bottomRight()
        rightDown()
        bottomLeft()
    elif cube[23] == 'G' and cube[30] == 'W':
        frontRight()
    #middle -- 4 (back-right)
    elif cube[32] == 'W' and cube[39] == 'G':
        bottomLeft()
        bottomLeft()
        backRight()
        bottomLeft()
        bottomLeft()
    elif cube[32] == 'G' and cube[39] == 'W':
        bottomRight()
        rightUp()
        bottomLeft()

    #Bottom Edges Unneeded

    # # Front-bottom edge
    # print("Front Bottom:", cube[10], cube[25], "| Should be W G")

    # # Right-bottom edge
    # print("Right Bottom:", cube[14], cube[34], "| Should be W O")

    # # Back-bottom edge
    # print("Back Bottom:", cube[16], cube[43], "| Should be W B")

    # # Left-bottom edge
    # print("Left Bottom:", cube[12], cube[52], "| Should be W R")

    print(cube[9:18])