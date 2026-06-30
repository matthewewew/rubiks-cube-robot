cube = []
moveHistory = []
standardNotationMoves = []

def load(state):
    cube[:] = state  # slice assignment, keeps the same list object
    moveHistory.clear()
    standardNotationMoves.clear()

def is_solved():
    return cube == [
        'Y','Y','Y','Y','Y','Y','Y','Y','Y',
        'W','W','W','W','W','W','W','W','W',
        'G','G','G','G','G','G','G','G','G',
        'O','O','O','O','O','O','O','O','O',
        'B','B','B','B','B','B','B','B','B',
        'R','R','R','R','R','R','R','R','R'
    ]