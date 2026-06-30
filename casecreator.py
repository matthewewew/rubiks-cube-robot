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
cube = ['Y','Y','Y','Y','Y','Y','Y','Y','Y',
        'W','W','W','W','W','W','W','W','W',
        'G','G','G','G','G','G','G','G','G',
        'O','O','O','O','O','O','O','O','O',
        'B','B','B','B','B','B','B','B','B',
        'R','R','R','R','R','R','R','R','R']

moveHistory = []
standardNotationMoves = []
standardNotationMovesStr = ""

moves.cube = cube
moves.moves = moveHistory
moves.moves2 = standardNotationMoves

ogCube = cube.copy()

#PASTE IN SCRAMBLE HERE:


sexyFront()
sexyBack()
bottomLeft()
bottomLeft()
sexyLeft()
rightUp()
leftDown()
topRight()
sexyFront()
frontRight()
frontRight()
backRight()

for i in range(len(standardNotationMoves)):   
      standardNotationMovesStr += standardNotationMoves[i]
      standardNotationMovesStr += ", "

print(standardNotationMovesStr)

print("cube_state.load([")

for i in range(54):
    end = ", "
    if i == 53:
        end = ""

    print(f"'{cube[i]}'", end=end)

    if (i + 1) % 9 == 0 and i != 53:
        print()
print("])")