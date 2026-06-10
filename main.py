import moves
from moves import topRight, topLeft, frontLeft, frontRight, leftDown, leftUp, rightDown, rightUp,\
      rotateFrontFaceRight, rotateFrontFaceLeft, rotateFrontFaceUp, rotateFrontFaceDown, sexy, leftyAlg
# The order goes top, bottom, front, right, back, left
cube = ['Y','Y','Y','Y','Y','Y','Y','Y','Y','W','W','W','W','W','W','W','W','W','R','R','R','R','R','R','R','R','R','G','G','G','G','G','G','G','G','G','O','O','O','O','O','O','O','O','O','B','B','B','B','B','B','B','B','B']
#cube = ['Y','R','Y','Y','Y','R','B','B','W','W','O','R','W','W','W','W','B','G','R','O','G','B','R','G','O','G','B','R','Y','G','R','G','W','Y','G','R','O','W','O','O','O','G','Y','Y','O','B','O','W','Y','B','R','B','B','G']
#cube = ['t1','t2','t3','t4','t5','t6','t7','t8','t9','bot1','bot2','bot3','bot4','bot5','bot6','bot7','bot8','bot9','f1','f2','f3','f4','f5','f6','f7','f8','f9','r1','r2','r3','r4','r5','r6','r7','r8','r9','b1','b2','b3','b4','b5','b6','b7','b8','b9', 'l1','l2','l3','l4','l5','l6','l7','l8','l9']
moveHistory = []

moves.cube = cube
moves.moves = moveHistory

ogCube = cube.copy()

#Red and white edge
#top -- 1 (top)
if cube[1] == 'R' and cube[37] == 'W':
    topRight()
    leftDown()
    frontLeft()
    leftUp()
elif cube[1] == 'W' and cube[37] == 'R':
    topRight()
    topRight()
    frontRight()
    frontRight()
#top -- 2 (left)
elif cube[3] == 'R' and cube[46] == 'W':
    leftDown()
    frontLeft()
    leftUp()
elif cube[3] == 'W' and cube[46] == 'R':
    topRight()
    frontLeft()
    frontLeft()
#top -- 3 (bottom)
elif cube[7] == 'W' and cube[19] == 'R':
    frontLeft()
    frontLeft()
elif cube[7] == 'R' and cube[19] == 'W':
    topRight()
    leftDown()
    frontLeft()
    leftUp()
#top -- 4 (right)
elif cube[5] == 'W' and cube[28] == 'R':
    topLeft()
    frontLeft()
    frontLeft()
elif cube[5] == 'R' and cube[28] == 'W':
    rightDown()
    frontRight()
    rightUp()

#middle -- 1 (top left)
elif cube[41] == 'W' and cube[48] == 'R':
    leftDown()
    topRight()
    frontLeft()
    frontLeft()
elif cube[41] == 'R' and cube[48] == 'W':
    rightDown()
    rightDown()
    frontLeft()
    rightDown()
    rightDown()
#middle -- 2 (top right)




#Post White Cross. Assume yellow is on top, white is on bottom, green front.
ftrCorner = {cube[i] for i in (8, 20, 27)}
ftlCorner = {cube[i] for i in (6, 18, 47)}
fbotlCorner = {cube[i] for i in (9, 24, 53)}
fbotrCorner = {cube[i] for i in (11, 26, 33)}

btrCorner = {cube[i] for i in (2, 29, 36)}
btlCorner = {cube[i] for i in (0, 38, 45)}
bbotlCorner = {cube[i] for i in (15, 44, 51)}
bbotrCorner = {cube[i] for i in (17, 35, 42)}

while True:
    if ftrCorner == {'G', 'O', 'W'} or fbotrCorner == {'G', 'O', 'W'}: 
        while (cube[26] != 'G') or (cube[33] != 'O'):
            sexy()
        break
    elif fbotlCorner == {'G', 'O', 'W'}:
        rotateFrontFaceLeft()


        topLeft()
    


rotateFrontFaceUp()

print(ogCube == cube)

print(cube)
print(moveHistory)


