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

    cube[0] = t7
    cube[1] = t4
    cube[2] = t1
    cube[3] = t8
    cube[5] = t2
    cube[6] = t9
    cube[7] = t3
    cube[8] = t6
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

def midRight():
    f4 = cube[19]
    f5 = cube[20]
    f6 = cube[21]
    r4 = cube[28]
    r5 = cube[29]
    r6 = cube[30]
    b4 = cube[37]
    b5 = cube[38]
    b6 = cube[39]
    l4 = cube[46]
    l5 = cube[47]
    l6 = cube[48]

    cube[19] = l4
    cube[20] = l5
    cube[21] = l6
    cube[28] = f4
    cube[29] = f5
    cube[30] = f6
    cube[37] = r4
    cube[38] = r5
    cube[39] = r6
    cube[46] = b4
    cube[47] = b5
    cube[48] = b6

    moves.append("mR")

#Order goes top, bottom, front, right, back, left
cube = ['Y','Y','Y','Y','Y','Y','Y','Y','Y','W','W','W','W','W','W','W','W','W','R','R','R','R','R','R','R','R','R','G','G','G','G','G','G','G','G','G','O','O','O','O','O','O','O','O','O','B','B','B','B','B','B','B','B','B']
moves = []

topRight()

print(cube)
print(moves)