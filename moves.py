cube = []
moves = []

def topLeft():
    #creates temp variables for the top layer of cube
    f1 = cube[18]
    f2 = cube[19]
    f3 = cube[20]
    r1 = cube[27]
    r2 = cube[28]
    r3 = cube[29]
    b1 = cube[36]
    b2 = cube[37]
    b3 = cube[38]
    l1 = cube[45]
    l2 = cube[46]
    l3 = cube[47]
    t1 = cube[0]
    t2 = cube[1]
    t3 = cube[2]
    t4 = cube[3]
    t6 = cube[5]
    t7 = cube[6]
    t8 = cube[7]
    t9 = cube[8]


    #rotates cube
    cube[18] = r1
    cube[19] = r2
    cube[20] = r3
    cube[27] = b1
    cube[28] = b2
    cube[29] = b3
    cube[36] = l1
    cube[37] = l2
    cube[38] = l3
    cube[45] = f1
    cube[46] = f2
    cube[47] = f3
    cube[0] = t7
    cube[1] = t4
    cube[2] = t1
    cube[3] = t8
    cube[5] = t2
    cube[6] = t9
    cube[7] = t6
    cube[8] = t3
    #adds move to move array
    moves.append("tL")
def topRight():
    #creates variables for top of cube
    f1 = cube[18]
    f2 = cube[19]
    f3 = cube[20]
    r1 = cube[27]
    r2 = cube[28]
    r3 = cube[29]
    b1 = cube[36]
    b2 = cube[37]
    b3 = cube[38]
    l1 = cube[45]
    l2 = cube[46]
    l3 = cube[47]
    t1 = cube[0]
    t2 = cube[1]
    t3 = cube[2]
    t4 = cube[3]
    t6 = cube[5]
    t7 = cube[6]
    t8 = cube[7]
    t9 =  cube[8]
    #move cube
    cube[0] = t3
    cube[1] = t6
    cube[2] = t9
    cube[3] = t2
    cube[5] = t8
    cube[6] = t1
    cube[7] = t4
    cube[8] = t7
    cube[18] = l1
    cube[19] = l2
    cube[20] = l3
    cube[27] = f1
    cube[28] = f2
    cube[29] = f3
    cube[36] = r1
    cube[37] = r2
    cube[38] = r3
    cube[45] = b1
    cube[46] = b2
    cube[47] = b3
    #adds move to move list
    moves.append("tR")
def bottomLeft():
    #creates temp variables for the bottom layer of cube
    f7 = cube[24]
    f8 = cube[25]
    f9 = cube[26]
    r7 = cube[33]
    r8 = cube[34]
    r9 = cube[35]
    b7 = cube[42]
    b8 = cube[43]
    b9 = cube[44]
    l7 = cube[51]
    l8 = cube[52]
    l9 = cube[53]
    bot1 = cube[9]
    bot2 = cube[10]
    bot3 = cube[11]
    bot4 = cube[12]
    bot6 = cube[14]
    bot7 = cube[15]
    bot8 = cube[16]
    bot9 = cube[17]
    #rotates cube
    cube[24] = r7
    cube[25] = r8
    cube[26] = r9
    cube[33] = b7
    cube[34] = b8
    cube[35] = b9
    cube[42] = l7
    cube[43] = l8
    cube[44] = l9
    cube[51] = f7
    cube[52] = f8
    cube[53] = f9
    cube[9] = bot3
    cube[10] = bot6
    cube[11] = bot9
    cube[12] = bot2
    cube[14] = bot8
    cube[15] = bot1
    cube[16] = bot4
    cube[17] = bot7
    #adds move to move array
    moves.append("bL")
def bottomRight():
    #create temp variables for bottom of cube
    bot1 = cube[9]
    bot2 = cube[10]
    bot3 = cube[11]
    bot4 = cube[12]
    bot6 = cube[14]
    bot7 = cube[15]
    bot8 = cube[16]
    bot9 = cube[17]
    f7 = cube[24]
    f8 = cube[25]
    f9 = cube[26]
    r7 = cube[33]
    r8 = cube[34]
    r9 = cube[35]
    b7 = cube[42]
    b8 = cube[43]
    b9 = cube[44]
    l7 = cube[51]
    l8 = cube[52]
    l9 = cube[53]
    #rotate cube
    cube[9] = bot7
    cube[10] = bot4
    cube[11] = bot1
    cube[12] = bot8
    cube[14] = bot2
    cube[15] = bot9
    cube[16] = bot6
    cube[17] = bot3
    cube[24] = l7
    cube[25] = l8
    cube[26] = l9
    cube[33] = f7
    cube[34] = f8
    cube[35] = f9
    cube[42] = r7
    cube[43] = r8
    cube[44] = r9
    cube[51] = b7
    cube[52] = b8
    cube[53] = b9
    #append to moves
    moves.append("bR")
def rightUp():
    t3 = cube[2]
    t6 = cube[5]
    t9 = cube[8]
    f3 = cube[20]
    f6 = cube[23]
    f9 = cube[26]
    bot3 = cube[11]
    bot6 = cube[14]
    bot9 = cube[17]
    b1 = cube[36]
    b4 = cube[39]
    b7 = cube[42]
    r1 = cube[27]
    r2 = cube[28]
    r3 = cube[29]
    r4 = cube[30]
    r5 = cube[31]
    r6 = cube[32]
    r7 = cube[33]
    r8 = cube[34]
    r9 = cube[35]




    cube[20] = bot3
    cube[23] = bot6
    cube[26] = bot9
    cube[11] = b7
    cube[14] = b4
    cube[17] = b1
    cube[42] = t3
    cube[39] = t6
    cube[36] = t9
    cube[2] = f3
    cube[5] = f6
    cube[8] = f9
    cube[27] = r7
    cube[28] = r4
    cube[29] = r1
    cube[30] = r8
    cube[31] = r5
    cube[32] = r2
    cube[33] = r9
    cube[34] = r6
    cube[35] = r3
    moves.append("rU")
def rightDown():
    t3 = cube[2]
    t6 = cube[5]
    t9 = cube[8]
    f3 = cube[20]
    f6 = cube[23]
    f9 = cube[26]
    bot3 = cube[11]
    bot6 = cube[14]
    bot9 = cube[17]
    b1 = cube[36]
    b4 = cube[39]
    b7 = cube[42]
    r1 = cube[27]
    r2 = cube[28]
    r3 = cube[29]
    r4 = cube[30]
    r5 = cube[31]
    r6 = cube[32]
    r7 = cube[33]
    r8 = cube[34]
    r9 = cube[35]




    cube[20] = t3
    cube[23] = t6
    cube[26] = t9
    cube[11] = f3
    cube[14] = f6
    cube[17] = f9
    cube[42] = bot3
    cube[39] = bot6
    cube[36] = bot9
    cube[2] = b7
    cube[5] = b4
    cube[8] = b1
    cube[27] = r3
    cube[28] = r6
    cube[29] = r9
    cube[30] = r2
    cube[31] = r5
    cube[32] = r8
    cube[33] = r1
    cube[34] = r4
    cube[35] = r7
    moves.append("rD")
def leftUp():
    #temporary variables
    t1 = cube[0]
    t4 = cube[3]
    t7 = cube[6]
    f1 = cube[18]
    f4 = cube[21]
    f7 = cube[24]
    bot1 = cube[9]
    bot4 = cube[12]
    bot7 = cube[15]
    b3 = cube[38]
    b6 = cube[41]
    b9 = cube[44]
    l1 = cube[45]
    l2 = cube[46]
    l3 = cube[47]
    l4 = cube[48]
    l6 = cube[50]
    l7 = cube[51]
    l8 = cube[52]
    l9 = cube[53]
    #rotates cube
    cube[0] = f1
    cube[3] = f4
    cube[6] = f7
    cube[18] = bot1
    cube[21] = bot4
    cube[24] = bot7
    cube[9] = b9
    cube[12] = b6
    cube[15] = b3
    cube[38] = t7
    cube[41] = t4
    cube[44] = t1
    cube[45] = l3
    cube[46] = l6
    cube[47] = l9
    cube[48] = l2
    cube[50] = l8
    cube[51] = l1
    cube[52] = l4
    cube[53] = l7
    #adds move to moves array
    moves.append("lU")
def leftDown():
    #temporary variables
    t1 = cube[0]
    t4 = cube[3]
    t7 = cube[6]
    f1 = cube[18]
    f4 = cube[21]
    f7 = cube[24]
    bot1 = cube[9]
    bot4 = cube[12]
    bot7 = cube[15]
    b3 = cube[38]
    b6 = cube[41]
    b9 = cube[44]
    l1 = cube[45]
    l2 = cube[46]
    l3 = cube[47]
    l4 = cube[48]
    l6 = cube[50]
    l7 = cube[51]
    l8 = cube[52]
    l9 = cube[53]
    #rotates cube
    cube[0] = b9
    cube[3] = b6
    cube[6] = b3
    cube[18] = t1
    cube[21] = t4
    cube[24] = t7
    cube[9] = f1
    cube[12] = f4
    cube[15] = f7
    cube[38] = bot7
    cube[41] = bot4
    cube[44] = bot1
    cube[45] = l7
    cube[46] = l4
    cube[47] = l1
    cube[48] = l8
    cube[50] = l2
    cube[51] = l9
    cube[52] = l6
    cube[53] = l3
    #adds move to moves array
    moves.append("lD")
    
def frontRight():
    t7 = cube[6]
    t8 = cube[7]
    t9 = cube[8]
    r1 = cube[27]
    r4 = cube[30]
    r7 = cube[33]
    bot1 = cube[9]
    bot2 = cube[10]
    bot3 = cube[11]
    l3 = cube[47]
    l6 = cube[50]
    l9 = cube[53]
    f1 = cube[18]
    f2 = cube[19]
    f3 = cube[20]
    f4 = cube[21]
    f5 = cube[22]
    f6 = cube[23]
    f7 = cube[24]
    f8 = cube[25]
    f9 = cube[26]




    cube[27] = t7
    cube[30] = t8
    cube[33] = t9
    cube[11] = r1
    cube[10] = r4
    cube[9]  = r7
    cube[53] = bot3
    cube[50] = bot2
    cube[47] = bot1
    cube[6] = l9
    cube[7] = l6
    cube[8] = l3
    cube[18] = f7
    cube[19] = f4
    cube[20] = f1
    cube[21] = f8
    cube[22] = f5
    cube[23] = f2
    cube[24] = f9
    cube[25] = f6
    cube[26] = f3
    moves.append("fR")
def frontLeft():
    t7 = cube[6]
    t8 = cube[7]
    t9 = cube[8]
    r1 = cube[27]
    r4 = cube[30]
    r7 = cube[33]
    bot1 = cube[9]
    bot2 = cube[10]
    bot3 = cube[11]
    l3 = cube[47]
    l6 = cube[50]
    l9 = cube[53]
    f1 = cube[18]
    f2 = cube[19]
    f3 = cube[20]
    f4 = cube[21]
    f5 = cube[22]
    f6 = cube[23]
    f7 = cube[24]
    f8 = cube[25]
    f9 = cube[26]




    cube[27] = bot3
    cube[30] = bot2
    cube[33] = bot1
    cube[11] = l9
    cube[10] = l6
    cube[9]  = l3
    cube[53] = t7
    cube[50] = t8
    cube[47] = t9
    cube[6] = r1
    cube[7] = r4
    cube[8] = r7
    cube[18] = f3
    cube[19] = f6
    cube[20] = f9
    cube[21] = f2
    cube[22] = f5
    cube[23] = f8
    cube[24] = f1
    cube[25] = f4
    cube[26] = f7
    moves.append("fL")
def backRight():
    #create temp variables for back of cube
    t1 = cube[0]
    t2 = cube[1]
    t3 = cube[2]
    bot7 = cube[15]
    bot8 = cube[16]
    bot9 = cube[17]
    r3 = cube[29]
    r6 = cube[32]
    r9 = cube[35]
    b1 = cube[36]
    b2 = cube[37]
    b3 = cube[38]
    b4 = cube[39]
    b6 = cube[41]
    b7 = cube[42]
    b8 = cube[43]
    b9 = cube[44]
    l1 = cube[45]
    l4 = cube[48]
    l7 = cube[51]
    #rotate cube
    cube[0] = l7
    cube[1] = l4
    cube[2] = l1
    cube[15] = r9
    cube[16] = r6
    cube[17] = r3
    cube[29] = t1
    cube[32] = t2
    cube[35] = t3
    cube[36] = b3
    cube[37] = b6
    cube[38] = b9
    cube[39] = b2
    cube[41] = b8
    cube[42] = b1
    cube[43] = b4
    cube[44] = b7
    cube[45] = bot7
    cube[48] = bot8
    cube[51] = bot9
    moves.append("backR")
def backLeft():
    #create temp variables for back of cube
    t1 = cube[0]
    t2 = cube[1]
    t3 = cube[2]
    bot7 = cube[15]
    bot8 = cube[16]
    bot9 = cube[17]
    r3 = cube[29]
    r6 = cube[32]
    r9 = cube[35]
    b1 = cube[36]
    b2 = cube[37]
    b3 = cube[38]
    b4 = cube[39]
    b6 = cube[41]
    b7 = cube[42]
    b8 = cube[43]
    b9 = cube[44]
    l1 = cube[45]
    l4 = cube[48]
    l7 = cube[51]
    #rotate cube
    cube[0] = r3
    cube[1] = r6
    cube[2] = r9
    cube[15] = l1
    cube[16] = l4
    cube[17] = l7
    cube[29] = bot9
    cube[32] = bot8
    cube[35] = bot7
    cube[36] = b7
    cube[37] = b4
    cube[38] = b1
    cube[39] = b8
    cube[41] = b2
    cube[42] = b9
    cube[43] = b6
    cube[44] = b3
    cube[45] = t3
    cube[48] = t2
    cube[51] = t1
    moves.append("backL")

def rotateFrontFaceRight():
    t1 = cube[0]
    t2 = cube[1]
    t3 = cube[2]
    t4 = cube[3]
    t5 = cube[4]
    t6 = cube[5]
    t7 = cube[6]
    t8 = cube[7]
    t9 = cube[8]
    bot1 = cube[9]
    bot2 = cube[10]
    bot3 = cube[11]
    bot4 = cube[12]
    bot5 = cube[13]
    bot6 = cube[14]
    bot7 = cube[15]
    bot8 = cube[16]
    bot9 = cube[17]
    f1 = cube[18]
    f2 = cube[19]
    f3 = cube[20]
    f4 = cube[21]
    f5 = cube[22]
    f6 = cube[23]
    f7 = cube[24]
    f8 = cube[25]
    f9 = cube[26]
    r1 = cube[27]
    r2 = cube[28]
    r3 = cube[29]
    r4 = cube[30]
    r5 = cube[31]
    r6 = cube[32]
    r7 = cube[33]
    r8 = cube[34]
    r9 = cube[35]
    b1 = cube[36]
    b2 = cube[37]
    b3 = cube[38]
    b4 = cube[39]
    b5 = cube[40]
    b6 = cube[41]
    b7 = cube[42]
    b8 = cube[43]
    b9 = cube[44]
    l1 = cube[45]
    l2 = cube[46]
    l3 = cube[47]
    l4 = cube[48]
    l5 = cube[49]
    l6 = cube[50]
    l7 = cube[51]
    l8 = cube[52]
    l9 = cube[53]

    cube[0] = t3
    cube[1] = t6
    cube[2] = t9
    cube[3] = t2
    cube[4] = t5
    cube[5] = t8
    cube[6] = t1
    cube[7] = t4
    cube[8] = t7
    cube[9] = bot7
    cube[10] = bot4
    cube[11] = bot1
    cube[12] = bot8
    cube[13] = bot5
    cube[14] = bot2
    cube[15] = bot9
    cube[16] = bot6
    cube[17] = bot3
    cube[18] = l1
    cube[19] = l2
    cube[20] = l3
    cube[21] = l4
    cube[22] = l5
    cube[23] = l6
    cube[24] = l7
    cube[25] = l8
    cube[26] = l9
    cube[27] = f1
    cube[28] = f2
    cube[29] = f3
    cube[30] = f4
    cube[31] = f5
    cube[32] = f6
    cube[33] = f7
    cube[34] = f8
    cube[35] = f9
    cube[36] = r1
    cube[37] = r2
    cube[38] = r3
    cube[39] = r4
    cube[40] = r5
    cube[41] = r6
    cube[42] = r7
    cube[43] = r8
    cube[44] = r9
    cube[45] = b1
    cube[46] = b2
    cube[47] = b3
    cube[48] = b4
    cube[49] = b5
    cube[50] = b6
    cube[51] = b7
    cube[52] = b8
    cube[53] = b9

def rotateFrontFaceUp():
    t1 = cube[0]
    t2 = cube[1]
    t3 = cube[2]
    t4 = cube[3]
    t5 = cube[4]
    t6 = cube[5]
    t7 = cube[6]
    t8 = cube[7]
    t9 = cube[8]
    bot1 = cube[9]
    bot2 = cube[10]
    bot3 = cube[11]
    bot4 = cube[12]
    bot5 = cube[13]
    bot6 = cube[14]
    bot7 = cube[15]
    bot8 = cube[16]
    bot9 = cube[17]
    f1 = cube[18]
    f2 = cube[19]
    f3 = cube[20]
    f4 = cube[21]
    f5 = cube[22]
    f6 = cube[23]
    f7 = cube[24]
    f8 = cube[25]
    f9 = cube[26]
    r1 = cube[27]
    r2 = cube[28]
    r3 = cube[29]
    r4 = cube[30]
    r5 = cube[31]
    r6 = cube[32]
    r7 = cube[33]
    r8 = cube[34]
    r9 = cube[35]
    b1 = cube[36]
    b2 = cube[37]
    b3 = cube[38]
    b4 = cube[39]
    b5 = cube[40]
    b6 = cube[41]
    b7 = cube[42]
    b8 = cube[43]
    b9 = cube[44]
    l1 = cube[45]
    l2 = cube[46]
    l3 = cube[47]
    l4 = cube[48]
    l5 = cube[49]
    l6 = cube[50]
    l7 = cube[51]
    l8 = cube[52]
    l9 = cube[53]

    cube[0] = f1
    cube[1] = f2
    cube[2] = f3
    cube[3] = f4
    cube[4] = f5
    cube[5] = f6
    cube[6] = f7
    cube[7] = f8
    cube[8] = f9
    cube[9] = b9
    cube[10] = b8
    cube[11] = b7
    cube[12] = b6
    cube[13] = b5
    cube[14] = b4
    cube[15] = b3
    cube[16] = b2
    cube[17] = b1
    cube[18] = bot1
    cube[19] = bot2
    cube[20] = bot3
    cube[21] = bot4
    cube[22] = bot5
    cube[23] = bot6
    cube[24] = bot7
    cube[25] = bot8
    cube[26] = bot9
    cube[27] = r7
    cube[28] = r4
    cube[29] = r1
    cube[30] = r8
    cube[31] = r5
    cube[32] = r2
    cube[33] = r9
    cube[34] = r6
    cube[35] = r3
    cube[36] = t9
    cube[37] = t8
    cube[38] = t7
    cube[39] = t6
    cube[40] = t5
    cube[41] = t4
    cube[42] = t3
    cube[43] = t2
    cube[44] = t1
    cube[45] = l3
    cube[46] = l6
    cube[47] = l9
    cube[48] = l2
    cube[49] = l5
    cube[50] = l8
    cube[51] = l1
    cube[52] = l4
    cube[53] = l7

def rotateFrontFaceDown():
    rotateFrontFaceUp()
    rotateFrontFaceUp()
    rotateFrontFaceUp()

def rotateFrontFaceLeft():
    rotateFrontFaceRight()
    rotateFrontFaceRight()
    rotateFrontFaceRight()

def sexyFront():
    rightUp()
    topLeft()
    rightDown()
    topRight()

def sexyRight():
    backLeft()
    topLeft()
    backRight()
    topRight()

def sexyBack():
    leftDown()
    topLeft()
    leftUp()
    topRight()

def sexyLeft():
    frontRight()
    topLeft()
    frontLeft()
    topRight()

def sexyTop():
    rightUp()
    backLeft()
    rightDown()
    backRight()

def sexyBot():
    rightUp()
    frontRight()
    rightDown()
    frontLeft()

def leftyFront():
    leftUp()
    topLeft()
    leftDown()
    topRight()

def leftyRight():
    frontLeft()
    topRight()
    frontRight()
    topLeft()

def leftyBack():
    rightDown()
    topRight()
    rightUp()
    topLeft()

def leftyLeft():
    backRight()
    topRight()
    backLeft()
    topLeft()

def leftyTop():
    leftUp()
    backRight()
    leftDown()
    backLeft()

def leftyBot():
    leftUp()
    frontLeft()
    leftDown()
    frontRight()