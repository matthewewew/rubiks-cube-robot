import moves
# The order goes top, bottom, front, right, back, left
cube = ['Y','Y','Y','Y','Y','Y','Y','Y','Y','W','W','W','W','W','W','W','W','W','R','R','R','R','R','R','R','R','R','G','G','G','G','G','G','G','G','G','O','O','O','O','O','O','O','O','O','B','B','B','B','B','B','B','B','B']
#cube = ['O','B','B','G','Y','W','G','B','G','Y','R','B','G','W','O','W','B','O','W','R','Y','R','R','O','G','G','O','R','G','R','W','G','B','Y','Y','B','Y','Y','G','W','O','W','W','O','B','W','Y','R','R','B','Y','R','O','O']
#cube = ['t1','t2','t3','t4','t5','t6','t7','t8','t9','bot1','bot2','bot3','bot4','bot5','bot6','bot7','bot8','bot9','f1','f2','f3','f4','f5','f6','f7','f8','f9','r1','r2','r3','r4','r5','r6','r7','r8','r9','b1','b2','b3','b4','b5','b6','b7','b8','b9', 'l1','l2','l3','l4','l5','l6','l7','l8','l9']
moveHistory = []

moves.cube = cube
moves.moves = moveHistory

ogCube = cube.copy()

# moves.sexy()
# moves.sexy()
# moves.sexy()
# moves.sexy()
# moves.sexy()
# moves.sexy()
moves.rightUp()
moves.rightDown()


print(ogCube == cube)

print(cube)
print(moveHistory)

