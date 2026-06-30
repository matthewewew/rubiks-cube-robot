from cube import cube
from solver.moves import *

def solve_second_layer():
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


    #print(frontLeftEdge())
    #print(frontRightEdge())
    #print(backRightEdge())
    #print(backLeftEdge())

    #print("Should be: \n['G', 'R']\n['G', 'O']\n['O', 'B']\n['B', 'R']\n")