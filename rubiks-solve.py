def topLeft():
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


def midRight():
    f4 = cube[21]
    f5 = cube[22]
    f6 = cube[23]
    r4 = cube[30]
    r5 = cube[31]
    r6 = cube[32]
    b4 = cube[39]
    b5 = cube[40]
    b6 = cube[41]
    l4 = cube[48]
    l5 = cube[49]
    l6 = cube[50]

    cube[21] = l4
    cube[22] = l5
    cube[23] = l6
    cube[30] = f4
    cube[31] = f5
    cube[32] = f6
    cube[39] = r4
    cube[40] = r5
    cube[41] = r6
    cube[48] = b4
    cube[49] = b5
    cube[50] = b6


    moves.append("mR")

def midLeft():
    f4 = cube[21]
    f5 = cube[22]
    f6 = cube[23]
    r4 = cube[30]
    r5 = cube[31]
    r6 = cube[32]
    b4 = cube[39]
    b5 = cube[40]
    b6 = cube[41]
    l4 = cube[48]
    l5 = cube[49]
    l6 = cube[50]

    cube[21] = r4
    cube[22] = r5
    cube[23] = r6
    cube[30] = b4
    cube[31] = b5
    cube[32] = b6
    cube[39] = l4
    cube[40] = l5
    cube[41] = l6
    cube[48] = f4
    cube[49] = f5
    cube[50] = f6


    moves.append("mL")

def midUp():
    f2 = cube[19]
    f5 = cube[22]
    f8 = cube[25]
    r2 = cube[28]
    r5 = cube[31]
    r8 = cube[34]
    b2 = cube[37]
    b5 = cube[40]
    b8 = cube[43]
    l2 = cube[46]
    l5 = cube[49]
    l8 = cube[52]

    cube[19] = l2
    cube[22] = l5
    cube[25] = l8
    cube[28] = f2
    cube[31] = f5
    cube[34] = f8
    cube[37] = r2
    cube[40] = r5
    cube[43] = r8
    cube[46] = b2
    cube[49] = b5
    cube[52] = b8

    moves.append("mU")

def topRight():
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




    moves.append("tR")
def bottomLeft():
    #creates temp variables for the top layer of cube
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




# The order goes top, bottom, front, right, back, left
cube = ['T','T','T','T','T','T','T','T','T','BOT','BOT','BOT','BOT','BOT','BOT','BOT','BOT','BOT','F','F','F','F','F','F','F','F','F','R','R','R','R','R','R','R','R','R','B','B','B','B','B','B','B','B','B','L','L','L','L','L','L','L','L','L']
#cube = ['O','B','B','G','Y','W','G','B','G','Y','R','B','G','W','O','W','B','O','W','R','Y','R','R','O','G','G','O','R','G','R','W','G','B','Y','Y','B','Y','Y','G','W','O','W','W','O','B']['W","Y","R","R","B","Y","R","O","O"]
moves = []
midRight()


print(cube)
print(moves)



