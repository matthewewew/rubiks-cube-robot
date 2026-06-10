import moves
# The order goes top, bottom, front, right, back, left
cube = ['Y','Y','Y','Y','Y','Y','Y','Y','Y','W','W','W','W','W','W','W','W','W','R','R','R','R','R','R','R','R','R','G','G','G','G','G','G','G','G','G','O','O','O','O','O','O','O','O','O','B','B','B','B','B','B','B','B','B']
#cube = ['O','B','B','G','Y','W','G','B','G','Y','R','B','G','W','O','W','B','O','W','R','Y','R','R','O','G','G','O','R','G','R','W','G','B','Y','Y','B','Y','Y','G','W','O','W','W','O','B','W','Y','R','R','B','Y','R','O','O']
#cube = ['t1','t2','t3','t4','t5','t6','t7','t8','t9','bot1','bot2','bot3','bot4','bot5','bot6','bot7','bot8','bot9','f1','f2','f3','f4','f5','f6','f7','f8','f9','r1','r2','r3','r4','r5','r6','r7','r8','r9','b1','b2','b3','b4','b5','b6','b7','b8','b9', 'l1','l2','l3','l4','l5','l6','l7','l8','l9']
moveHistory = []

moves.cube = cube
moves.moves = moveHistory

ogCube = cube.copy()

middles = [cube[4], cube[13], cube[22], cube[31], cube[40], cube[49]]
middlePositions = [4, 13, 22, 31, 40, 49]

edges = [cube[1], cube[3], cube[5], cube[7], cube[10], cube[12], cube[14], cube[16], cube[19], cube[21], cube[23], cube[25], cube[28], cube[30], cube[32], cube[34], cube[37], cube[39], cube[41], cube[43], cube[46], cube[48], cube[50], cube[52]]
edgePositions = [1, 3, 5, 7, 10, 12, 14, 16, 19, 21, 23, 25, 28, 30, 32, 34, 37, 39, 41, 43, 46, 48, 50, 52]

corners = [cube[0], cube[2], cube[6], cube[8], cube[9], cube[11], cube[15], cube[17], cube[18], cube[20], cube[24], cube[26], cube[27], cube[29], cube[33], cube[35], cube[36], cube[38], cube[42], cube[44], cube[45], cube[47], cube[51], cube[53]]
cornerPositions = [0, 2, 6, 8, 9, 11, 15, 17, 18, 20, 24, 26, 27, 29, 33, 35, 36, 38, 42, 44, 45, 47, 51, 53]

for i in range(len(middles)):
    if middles[i] == 'Y':
        daisyCenter = middlePositions[i]


print(ogCube == cube)

print(cube)
print(moveHistory)
print(daisyCenter)

