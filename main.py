import moves
from moves import topRight, topLeft, frontLeft, frontRight, leftDown, leftUp, rightDown, rightUp,\
      backLeft, backRight, bottomLeft, bottomRight,\
      rotateFrontFaceRight, rotateFrontFaceLeft, rotateFrontFaceUp, rotateFrontFaceDown,\
      sexyFront, sexyRight, sexyLeft, sexyBack, sexyTop, sexyBot,\
      leftyFront, leftyBack, leftyTop, leftyBot, leftyLeft, leftyRight,\
      tPermFront, tPermRight, tPermBack, tPermLeft, upsideDownSexyFront,\
      upsideDownSexyBack, upsideDownSexyLeft, upsideDownSexyRight,\
      invLeftyBack, invLeftyFront, invLeftyLeft, invLeftyRight, invSexyBack,\
      invSexyFront, invSexyLeft, invSexyRight, uPermBack, uPermFront, uPermLeft,\
      uPermRight, luPermBack, luPermFront, luPermLeft, luPermRight
# The order goes top, bottom, front, right, back, left
#cube = ['Y','Y','Y','Y','Y','Y','Y','Y','Y','W','W','W','W','W','W','W','W','W','R','R','R','R','R','R','R','R','R','G','G','G','G','G','G','G','G','G','O','O','O','O','O','O','O','O','O','B','B','B','B','B','B','B','B','B']
#cube = ['Y','R','Y','Y','Y','R','B','B','W','W','O','R','W','W','W','W','B','G','R','O','G','B','R','G','O','G','B','R','Y','G','R','G','W','Y','G','R','O','W','O','O','O','G','Y','Y','O','B','O','W','Y','B','R','B','B','G']
#cube = ['t1','t2','t3','t4','t5','t6','t7','t8','t9','bot1','bot2','bot3','bot4','bot5','bot6','bot7','bot8','bot9','f1','f2','f3','f4','f5','f6','f7','f8','f9','r1','r2','r3','r4','r5','r6','r7','r8','r9','b1','b2','b3','b4','b5','b6','b7','b8','b9', 'l1','l2','l3','l4','l5','l6','l7','l8','l9']
count = 0

#random scramble
cube = [
'Y', 'Y', 'B', 'Y', 'Y', 'Y', 'R', 'Y', 'B', 
'O', 'W', 'O', 'W', 'W', 'W', 'W', 'W', 'W', 
'Y', 'R', 'R', 'G', 'G', 'G', 'G', 'G', 'Y', 
'Y', 'B', 'W', 'O', 'O', 'O', 'B', 'O', 'O', 
'R', 'O', 'G', 'B', 'B', 'B', 'B', 'B', 'R', 
'O', 'G', 'G', 'R', 'R', 'R', 'G', 'R', 'W']

#test case for white cross

# cube = [
#     'Y','Y','G','B','Y','G','B','G','O',
#     'W','W','G','W','W','W','B','W','O',
#     'W','R','G','O','G','B','R','G','W',
#     'W','O','Y','Y','O','R','R','O','G',
#     'R','G','B','Y','B','B','Y','B','O',
#     'R','R','O','O','R','Y','Y','R','B'
# ]

#Post first layer test case:

# cube = [
# 'Y', 'R', 'O', 'B', 'Y', 'R', 'B', 'G', 'O', 
# 'W', 'Y', 'W', 'W', 'W', 'W', 'B', 'W', 'B', 
# 'R', 'R', 'W', 'G', 'G', 'B', 'G', 'G', 'G', 
# 'B', 'B', 'Y', 'O', 'O', 'O', 'O', 'G', 'O', 
# 'G', 'Y', 'R', 'Y', 'B', 'O', 'Y', 'B', 'Y', 
# 'G', 'Y', 'W', 'W', 'R', 'O', 'R', 'R', 'R']

#Blank cube green front
# cube = [
#      'Y','Y','Y','Y','Y','Y','Y','Y','Y',
#      'W','W','W','W','W','W','W','W','W',
#      'G','G','G','G','G','G','G','G','G',
#      'O','O','O','O','O','O','O','O','O',
#      'B','B','B','B','B','B','B','B','B',
#      'R','R','R','R','R','R','R','R','R' 
# ]

#Post f2l yellow cross cube

# cube = [
#       'Y','Y','Y','Y','Y','Y','O','Y','R',
#       'W','W','W','W','W','W','W','W','W',
#       'G','G','G','G','G','G','G','G','G',
#       'Y','O','O','O','O','O','O','O','O',
#       'B','R','B','B','B','B','B','B','B',
#       'R','B','Y','R','R','R','R','R','R' 
# ]

#Yellow top f2l solved

# cube = [
#       'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y',
#       'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W',
#       'R', 'G', 'R', 'G', 'G', 'G', 'G', 'G', 'G',
#       'G', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O',
#       'B', 'B', 'G', 'B', 'B', 'B', 'B', 'B', 'B',
#       'O', 'R', 'B', 'R', 'R', 'R', 'R', 'R', 'R'
# ]

#Final yellow edges
# cube = [
#       'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y',
#       'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W',
#       'G', 'O', 'G', 'G', 'G', 'G', 'G', 'G', 'G',
#       'O', 'G', 'O', 'O', 'O', 'O', 'O', 'O', 'O',
#       'B', 'R', 'B', 'B', 'B', 'B', 'B', 'B', 'B',
#       'R', 'B', 'R', 'R', 'R', 'R', 'R', 'R', 'R'
# ]


moveHistory = []
standardNotationMoves = []
standardNotationMovesStr = ""

moves.cube = cube
moves.moves = moveHistory
moves.moves2 = standardNotationMoves

ogCube = cube.copy()

#Check if Solved cube
def cubeSolved():
    return cube == [
        'Y','Y','Y','Y','Y','Y','Y','Y','Y',
        'W','W','W','W','W','W','W','W','W',
        'G','G','G','G','G','G','G','G','G',
        'O','O','O','O','O','O','O','O','O',
        'B','B','B','B','B','B','B','B','B',
        'R','R','R','R','R','R','R','R','R'
    ]

#######################################
#START OF WHITE CROSS CODE; RED-WHITE EDGE
####################################### 
#top -- 1 (top-back)
if cube[1] == 'R' and cube[37] == 'W':
    topRight()
    leftDown()
    bottomLeft()
    frontLeft()
    bottomRight()
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
    print(cube[46])
    leftDown()
    leftDown()
    print('in top 2-\n')
#top -- 3 (bottom)
elif cube[7] == 'W' and cube[19] == 'R':
    frontLeft()
    frontLeft()
    print('in top 3\n')
elif cube[7] == 'R' and cube[19] == 'W':
    topRight()
    leftDown()
    frontLeft()
    leftUp()
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
    rightUp()
    print('in top 4-\n')
#middle -- 1 (back-left)
elif cube[41] == 'W' and cube[48] == 'R':
    leftUp()
    print('in mid 1\n')
elif cube[41] == 'R' and cube[48] == 'W':
    bottomRight()
    backLeft()
    bottomLeft()
    
    print('in mid 1-\n')
#middle -- 2 (front-left)
elif cube[21] == 'W' and cube[50] == 'R':
     leftDown()
     print('in mid 2\n')
elif cube[21] == 'R' and cube[50] == 'W':
     leftDown()
     leftDown()
     bottomRight()
     backLeft()
     bottomRight()
     print('in mid 2-\n')
#middle -- 3 (front-right)
elif cube[23] == 'W' and cube[30] == 'R':
     bottomLeft()
     bottomLeft()
     rightDown()
     bottomRight()
     bottomRight()
     print('in mid 3\n')
elif cube[23] == 'R' and cube[30] == 'W':
     bottomLeft()
     frontRight()
     bottomRight()
     print('in mid 3-\n')
#middle -- 4 (back-right)
elif cube[32] == 'W' and cube[39] == 'R':
     bottomRight()
     backRight()
     bottomLeft()
     print('in mid 4\n')
elif cube[32] == 'R' and cube[39] == 'W':
     bottomRight()
     backRight()
     bottomLeft()
     print('in mid 4-\n')
#bottom -- 1 (bottom-Left edge)
elif cube[12] == 'R' and cube[52] == 'W':
     leftDown()
     bottomRight()
     backLeft()
     bottomLeft()
     print('in bot 1\n')
     #Another Elif not needed because it would be where 
     #its supposed to be
     
#bottom - 2 (bottom-front edge)
elif cube[25] == 'W' and cube[10] == 'R':
      frontRight()
      leftDown()
      print('in bot 2\n')
elif cube[25] == 'R' and cube[10] == 'W':
      frontRight()
      frontRight()
      topLeft()
      leftDown()
      leftDown()
      print('in bot 2-\n')
#bottom - 3 (bottom-right edge)
elif cube[14] == 'R' and cube[34] == 'W':
      rightDown()
      bottomRight()
      bottomRight()
      rightUp()
      bottomLeft()
      bottomLeft()
      print('in bot 3\n')
elif cube[14] == 'W' and cube[34] == 'R':
     rightDown()
     bottomRight()
     backRight()
     bottomLeft()
     print('in bot 3-\n')
#bottom - 4 (bottom-back edge)
elif cube[16] == 'W' and cube[43] == 'R':
     backLeft()
     backLeft()
     topRight()
     leftDown()
     leftDown()
     print('in bot 4\n')
elif cube[16] == 'R' and cube[43] == 'W':
      backRight()
      leftUp()
      print('in bot 4-\n')

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
      backLeft()
      bottomRight()
      leftUp()
      bottomLeft()
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
      bottomRight()
      rightUp()
      bottomLeft()
      backRight()
#top -- 4 (top-right)
elif cube[5] == 'W' and cube[28] == 'B':
      bottomRight()
      rightUp()
      rightUp()
      bottomLeft()
elif cube[5] == 'B' and cube[28] == 'W':
      bottomRight()
      rightUp()
      bottomLeft()
      backRight()
#middle -- 1 (back-left)
elif cube[41] == 'W' and cube[48] == 'B':
      bottomLeft()
      leftUp()
      bottomRight()
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
      bottomRight()
      rightDown()
      bottomLeft()
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
      bottomRight()
      rightUp()
      bottomLeft()
#bottom -- 1 (bottom-Left edge)
elif cube[12] == 'B' and cube[52] == 'W':
      leftDown()
      backLeft()
elif cube[12] == 'W' and cube[52] == 'B':
      leftUp()
      leftUp()
      topLeft()
      backRight()
      backRight()
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
      bottomRight()
      rightDown()
      bottomLeft()
#bottom - 3 (bottom-right edge)
elif cube[14] == 'W' and cube[34] == 'B':
      rightUp()
      bottomRight()
      rightDown()
      bottomLeft()
elif cube[14] == 'B' and cube[34] == 'W':
      rightDown()
      backRight()
#bottom - 4 (bottom-back edge)
# THIS IS THE PREFERRED SPOT
# elif cube[16] == 'W' and cube[43] == 'B':

elif cube[16] == 'B' and cube[43] == 'W':
      backLeft()
      bottomRight()
      rightUp()
      bottomLeft()

##############################
#ORANGE-WHITE EDGE
##############################

#TOP -- 1 (TOP BACK EDGE)
if cube[1] == 'O' and cube[37] == 'W':
      topLeft()
      rightDown()
      bottomRight()
      frontRight()
      bottomLeft()
elif cube[1] == 'W' and cube[37] == 'O':
      topLeft()
      rightUp()
      rightUp()
#top -- 2 (top-left edge)
elif cube[3] == 'O' and cube[46] == 'W':
      topRight()
      topRight()
      rightUp()
      bottomLeft()
      backRight()
      bottomRight()
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
      bottomRight()
      frontRight()
      bottomLeft()
      rightDown()
#top -- 4 (top-right)
elif cube[5] == 'W' and cube[28] == 'O':
      rightDown()
      rightDown()
elif cube[5] == 'O' and cube[28] == 'W':
      rightUp()
      bottomLeft()
      backRight()
      bottomRight()
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
      bottomRight()
      bottomRight()
      leftDown()
      bottomLeft()
      bottomLeft()
elif cube[21] == 'O' and cube[50] == 'W':
      bottomRight()
      frontLeft()
      bottomLeft()
#middle -- 3 (front-right)
elif cube[23] == 'W' and cube[30] == 'O':
      rightDown()
elif cube[23] == 'O' and cube[30] == 'W':
      bottomRight()
      frontRight()
      bottomLeft()
#middle -- 4 (back-right)
elif cube[32] == 'W' and cube[39] == 'O':
      bottomLeft()
      backRight()
      bottomRight()
elif cube[32] == 'O' and cube[39] == 'W':
      rightDown()
#bottom -- 1 (bottom-Left edge)
elif cube[12] == 'O' and cube[52] == 'W':
      leftUp()
      bottomRight()
      frontLeft()
      bottomLeft()
elif cube[12] == 'W' and cube[52] == 'O':
      leftUp()
      bottomRight()
      bottomRight()
      leftDown()
      bottomLeft()
      bottomLeft()
#bottom - 2 (bottom-front edge)
elif cube[25] == 'O' and cube[10] == 'W':
      frontLeft()
      bottomRight()
      frontRight()
      bottomLeft()
elif cube[25] == 'W' and cube[10] == 'O':
      frontLeft()
      rightDown()

#bottom - 3 (bottom-right edge)
# Ideal Spot
# elif cube[14] == 'W' and cube[34] == 'O':

elif cube[14] == 'O' and cube[34] == 'W':
      rightUp()
      bottomRight()
      frontRight()
      bottomLeft()

#bottom - 4 (bottom-back edge)
elif cube[16] == 'W' and cube[43] == 'O':
      backLeft()
      bottomLeft()
      backRight()
      bottomRight()
elif cube[16] == 'O' and cube[43] == 'W':
      backLeft()
      rightUp()

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
      bottomLeft()
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
      bottomLeft()
      rightDown()
      bottomRight()
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

# Front-bottom edge
print("Front Bottom:", cube[10], cube[25], "| Should be W G")

# Right-bottom edge
print("Right Bottom:", cube[14], cube[34], "| Should be W O")

# Back-bottom edge
print("Back Bottom:", cube[16], cube[43], "| Should be W B")

# Left-bottom edge
print("Left Bottom:", cube[12], cube[52], "| Should be W R")


########################################################
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
            
            

#########################################
# POST FIRST LAYER: Creating Second Layer
#########################################

#Defining each edge for second layer solve
def topFrontEdge():
      return [cube[i] for i in (7, 19)]

def topRightEdge():
      return [cube[i] for i in (5, 28)]

def topBackEdge():
      return [cube[i] for i in (1, 37)]

def topLeftEdge():
      return [cube[i] for i in (3, 46)]

def frontRightEdge():
      return [cube[i] for i in (23, 30)]

def backRightEdge():
      return [cube[i] for i in (32, 39)]

def backLeftEdge():
      return [cube[i] for i in (41, 48)]

def frontLeftEdge():
      return [cube[i] for i in (21, 50)]


while((frontLeftEdge() != ['G','R']) or (frontRightEdge() != ['G','O'])\
       or (backRightEdge() != ['O','B']) or (backLeftEdge() != ['B','R'])):
      

      #Solve for blue orange corner:
      target = {'B', 'O'}

      if set(topFrontEdge()) == target:
            if cube[19] == 'B':
                  topRight()
                  topRight()
                  invLeftyBack()
                  invSexyRight()
                  
            else:
                  topRight()
                  invSexyRight()
                  invLeftyBack()
                  
            
      elif set(topRightEdge()) == target:
            if cube[28] == 'B':
                  topRight()
                  invLeftyBack()
                  invSexyRight()
                  
            else:
                  invSexyRight()
                  invLeftyBack()
            
      elif set(topBackEdge()) == target:
            if cube[37] == 'B':
                  invLeftyBack()
                  invSexyRight()
            else:
                  topLeft()
                  invSexyRight()
                  invLeftyBack()
                  

      elif set(topLeftEdge()) == target:
            if cube[46] == 'B':
                  topLeft()
                  invLeftyBack()
                  invSexyRight()
                  
            else:
                  topLeft()
                  topLeft()
                  invSexyRight()
                  invLeftyBack()
      
      elif set(frontRightEdge()) == target:
            invSexyFront()
            invLeftyRight()
            

      elif backRightEdge() == ['B','O']:
            invSexyRight()
            invLeftyBack()
            

      elif set(backLeftEdge()) == target:
            invSexyBack()
            invLeftyLeft()
            

      elif set(frontLeftEdge()) == target:
            invLeftyFront()
            invSexyLeft()
            
      #Solve for blue red corner:
      target = {'B', 'R'}

      if set(topFrontEdge()) == target:
            if cube[19] == 'B':
                  topRight()
                  topRight()
                  invSexyBack()
                  invLeftyLeft()
            else:
                  topLeft()
                  invLeftyLeft()
                  invSexyBack()
            
      elif set(topRightEdge()) == target:
            if cube[28] == 'B':
                  topRight()
                  invSexyBack()
                  invLeftyLeft()
            else:
                  topRight()
                  topRight()
                  invLeftyLeft()
                  invSexyBack()

      elif set(topBackEdge()) == target:
            if cube[37] == 'B':
                  invSexyBack()
                  invLeftyLeft()
            else:
                  topRight()
                  invLeftyLeft()
                  invSexyBack()
            
      elif set(topLeftEdge()) == target:
            if cube[46] == 'B':
                  topLeft()
                  invSexyBack()
                  invLeftyLeft()
            else:
                  invLeftyLeft()
                  invSexyBack()

      elif set(frontRightEdge()) == target:
            invSexyFront()
            invLeftyRight()

      elif set(backRightEdge()) == target:
            invSexyRight()
            invLeftyBack()
            
      elif backLeftEdge() == ['R','B']:
            invSexyBack()
            invLeftyLeft()

      elif set(frontLeftEdge()) == target:
            invLeftyFront()
            invSexyLeft()
      
      #Solve for orange green corner:
      target = {'O', 'G'}

      if set(topFrontEdge()) == target:
            if cube[19] == 'O':
                  topRight()
                  invLeftyRight()
                  invSexyFront()
            else:
                  invSexyFront()
                  invLeftyRight()
            
      elif set(topRightEdge()) == target:
            if cube[28] == 'O':
                  invLeftyRight()
                  invSexyFront()
            else:
                  topLeft()
                  invSexyFront()
                  invLeftyRight()

      elif set(topBackEdge()) == target:
            if cube[37] == 'O':
                  topLeft()
                  invLeftyRight()
                  invSexyFront()
            else:
                  topLeft()
                  topLeft()
                  invSexyFront()
                  invLeftyRight()
            
      elif set(topLeftEdge()) == target:
            if cube[46] == 'O':
                  topLeft()
                  topLeft()
                  invLeftyRight()
                  invSexyFront()
            else:
                  topRight()
                  invSexyFront()
                  invLeftyRight()

      elif frontRightEdge() == ['O','G']:
            invSexyFront()
            invLeftyRight()

      elif set(backRightEdge()) == target:
            invSexyRight()
            invLeftyBack()
            
      elif set(backLeftEdge()) == target:
            invSexyBack()
            invLeftyLeft()

      elif set(frontLeftEdge()) == target:
            invLeftyFront()
            invSexyLeft()

            #Solve for red green corner:
      target = {'R', 'G'}

      if set(topFrontEdge()) == target:
            if cube[19] == 'R':
                  topLeft()
                  invSexyLeft()
                  invLeftyFront()
            else:
                  invLeftyFront()
                  invSexyLeft()
            
      elif set(topRightEdge()) == target:
            if cube[28] == 'R':
                  topLeft()
                  topLeft()
                  invSexyLeft()
                  invLeftyFront()
            else:
                  topLeft()
                  invLeftyFront()
                  invSexyLeft()

      elif set(topBackEdge()) == target:
            if cube[37] == 'R':
                  topRight()
                  invSexyLeft()
                  invLeftyFront()
            else:
                  topRight()
                  topRight()
                  invLeftyFront()
                  invSexyLeft()
            
      elif set(topLeftEdge()) == target:
            if cube[46] == 'R':
                  invSexyLeft()
                  invLeftyFront()
            else:
                  topRight()
                  invLeftyFront()
                  invSexyLeft()

      elif set(frontRightEdge()) == target:
            invSexyFront()
            invLeftyRight()

      elif set(backRightEdge()) == target:
            invSexyRight()
            invLeftyBack()
            
      elif set(backLeftEdge()) == target:
            invSexyBack()
            invLeftyLeft()

      elif frontLeftEdge() == ['R','G']:
            invLeftyFront()
            invSexyLeft()

      count += 1

      if count >= 100:
            break



print(frontLeftEdge())
print(frontRightEdge())
print(backRightEdge())
print(backLeftEdge())

print("Should be: \n['G', 'R']\n['G', 'O']\n['O', 'B']\n['B', 'R']")



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
      
      #Check for infinite loop
      count += 1
      if(count == 100):
            print(cube)
            for i in range(len(standardNotationMoves)):   
                  standardNotationMovesStr += standardNotationMoves[i]
                  standardNotationMovesStr += ", "
            print(standardNotationMovesStr)
            print("stuck in yellow cross")
            exit()

      
###########################
# POST F2L AND YELLOW CROSS
########################### 

#Solving Yellow Corners
while(cube[0] != 'Y' or cube[2] != 'Y' or cube[6] != 'Y' or cube[8] != 'Y'):
      while(cube[6] != 'Y'):
            upsideDownSexyFront()
      topRight()

            #Check for infinite loop
      count += 1
      if(count == 100):
            print(cube)
            for i in range(len(standardNotationMoves)):   
                  standardNotationMovesStr += standardNotationMoves[i]
                  standardNotationMovesStr += ", "
            print(moveHistory)
            print(standardNotationMovesStr)
            print("stuck in yellow corners")
            break

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
     

#testing:
print(
    frontHeadlights(),
    rightHeadlights(),
    backHeadlights(),
    leftHeadlights()
)

#Checking that corners are in right place

while(ftlCorner() != {'Y','R','G'} or\
      ftrCorner() != {'Y','O','G'} or\
      btrCorner() != {'Y','O','B'} or\
      btlCorner() != {'Y','R','B'}):

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
               
      #Check for infinite loop
      count += 1
      if(count == 100):
            print(cube)
            print("stuck in t perm")
            break

# #Full front top bars for final moves
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
while not (isGBar(frontBar()) or isOBar(rightBar()) or isBBar(backBar()) or isRBar(leftBar())):
      print("1")
      #Check for green bar for final moves
      if isGBar(frontBar()) or isGBar(rightBar()) or isGBar(backBar()) or isGBar(leftBar()):         
            if rightBar() == ['G', 'G', 'G']:
                  topLeft()
                  #print("1")

            if backBar() == ['G', 'G', 'G']:
                  topLeft()
                  topLeft()
                  #print("2")

            if leftBar() == ['G', 'G', 'G']:
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

            if leftBar() == ['O', 'O', 'O']:
                  topLeft()
                  topLeft()
                  #print("6")

            if frontBar() == ['O', 'O', 'O']:
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
            if leftBar() == ['B', 'B', 'B']:
                  topLeft()
                  #print("9")

            if frontBar() == ['B', 'B', 'B']:
                  topLeft()
                  topLeft()
                  #print("10")

            if rightBar() == ['B', 'B', 'B']:
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
            if frontBar() == ['R', 'R', 'R']:
                  topLeft()
                  #print("13")

            if rightBar() == ['R', 'R', 'R']:
                  topLeft()
                  topLeft()
                  #print("14")

            if backBar() == ['R', 'R', 'R']:
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
      
      #Check for infinite loop
      count += 1
      if(count == 100):
            print(cube)
            print("stuck in u perm")


#Check for misaligned top:
while not cubeSolved():
      topRight()

      count += 1
      if count > 100:
            print('Stuck in final step')
            break

            

print(ogCube == cube)
print(cube)



print(moveHistory)
print("Number of moves: ", len(moveHistory))

for i in range(len(standardNotationMoves)):   
      standardNotationMovesStr += standardNotationMoves[i]
      standardNotationMovesStr += ", "

print(standardNotationMovesStr)

#testing tPerms
# cube = ogCube.copy()
# moves.cube = cube

# tPermLeft()
# print(cube)

for i in range(0, 54, 9):
    print(cube[i:i+9])
