import moves
from moves import topRight, topLeft, frontLeft, frontRight, leftDown, leftUp, rightDown, rightUp,\
      rotateFrontFaceRight, rotateFrontFaceLeft, rotateFrontFaceUp, rotateFrontFaceDown,\
      sexyFront, sexyRight, sexyLeft, sexyBack, sexyTop, sexyBot,\
      leftyFront, leftyBack, leftyTop, leftyBot, leftyLeft, leftyRight
# The order goes top, bottom, front, right, back, left
#cube = ['Y','Y','Y','Y','Y','Y','Y','Y','Y','W','W','W','W','W','W','W','W','W','R','R','R','R','R','R','R','R','R','G','G','G','G','G','G','G','G','G','O','O','O','O','O','O','O','O','O','B','B','B','B','B','B','B','B','B']
#cube = ['Y','R','Y','Y','Y','R','B','B','W','W','O','R','W','W','W','W','B','G','R','O','G','B','R','G','O','G','B','R','Y','G','R','G','W','Y','G','R','O','W','O','O','O','G','Y','Y','O','B','O','W','Y','B','R','B','B','G']
#cube = ['t1','t2','t3','t4','t5','t6','t7','t8','t9','bot1','bot2','bot3','bot4','bot5','bot6','bot7','bot8','bot9','f1','f2','f3','f4','f5','f6','f7','f8','f9','r1','r2','r3','r4','r5','r6','r7','r8','r9','b1','b2','b3','b4','b5','b6','b7','b8','b9', 'l1','l2','l3','l4','l5','l6','l7','l8','l9']

#test case for white cross

cube = [
    'Y','B','W','Y','Y','O','W','G','R',
    'W','W','W','W','W','W','O','W','Y',
    'B','Y','Y','O','G','O','O','G','R',
    'B','B','B','G','O','R','G','O','O',
    'O','Y','R','G','B','R','G','B','Y',
    'G','R','R','B','R','Y','B','R','G'
]

moveHistory = []
standardNotationMoves = []

moves.cube = cube
moves.moves = moveHistory
moves.moves2 = standardNotationMoves

ogCube = cube.copy()

# Red and white edge
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

#Post White Cross. Assume yellow is on top, green front.

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

while (cube[26] != 'G') or (cube[33] != 'O') or (cube[11] != 'W'):
    
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

print(ogCube == cube)
print(cube)
print(moveHistory)
print("Number of moves: ", len(moveHistory))


