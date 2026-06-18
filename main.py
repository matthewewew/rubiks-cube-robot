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

#test case for white cross

# cube = [
#     'Y','Y','G','B','Y','G','B','G','O',
#     'W','W','G','W','W','W','B','W','O',
#     'W','R','G','O','G','B','R','G','W',
#     'W','O','Y','Y','O','R','R','O','G',
#     'R','G','B','Y','B','B','Y','B','O',
#     'R','R','O','O','R','Y','Y','R','B'
# ]

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

cube = [
      'Y','Y','Y','Y','Y','Y','O','Y','R',
      'W','W','W','W','W','W','W','W','W',
      'G','G','G','G','G','G','G','G','G',
      'Y','O','O','O','O','O','O','O','O',
      'B','R','B','B','B','B','B','B','B',
      'R','B','Y','R','R','R','R','R','R' 
]

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

########################################################
#Post White Cross. Assume yellow is on top, green front.
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
      
      #Check for infinite loop
      count += 1
      if(count == 3):
            print(cube)
            print("stuck in yellow cross")
            break
      
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
while(isGBar(frontBar()) or isOBar(rightBar()) or isBBar(backBar()) or isRBar(leftBar())):
      
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
            

# print(ogCube == cube)
#print(cube)



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
