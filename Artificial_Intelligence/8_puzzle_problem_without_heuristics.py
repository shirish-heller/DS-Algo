import copy
# Takes input as the starting state and the goal state
def solve_8_puzzle(StartState, GoalState):
    # print8Puzzle(StartState)
    # for rowIndex, row in enumerate(StartState):
    #     for colIndex, col in enumerate(row):
    #         if(col == ''):
    #             # empty space found
    queue = [(StartState, None)]
    visited = []
    totalVariationsProcessed = 0
    while (len(queue)!=0):
        totalVariationsProcessed+=1
        successorRight = successorLeft = successorDown = successorUp = None
        currentData = queue.pop()
        currentState = currentData[0]
        visited.append(currentState)
        invalidDirection = currentData[1]
        emptySpaceFound = False
        for rowIndex, row in enumerate(currentState):
            for colIndex, col in enumerate(row):
                if(col == ''): 
                # empty space found
                    emptySpaceFound=True
                    break
            if emptySpaceFound: break

        if(colIndex+1<len(currentState[0]) and invalidDirection !='R'):
            # right Exists
            successorRight = copy.deepcopy(currentState)
            rightElm = successorRight[rowIndex][colIndex+1]
            successorRight[rowIndex][colIndex] = rightElm
            successorRight[rowIndex][colIndex+1] = ''

            if successorRight not in visited:
                if(successorRight == GoalState):
                    print("Puzzle is solved!!\n", print8Puzzle(successorRight))
                    return True
                else:
                    queue.insert(0, (successorRight, 'L'))
            else: print("Already visited!")
        if(colIndex-1>=0 and invalidDirection !='L'):
            # left Exists
            successorLeft =  copy.deepcopy(currentState)
            leftElm = successorLeft[rowIndex][colIndex-1]
            successorLeft[rowIndex][colIndex] = leftElm
            successorLeft[rowIndex][colIndex-1] = ''
            if successorLeft not in visited:
                if(successorLeft == GoalState):
                    print("Puzzle is solved!!\n", print8Puzzle(successorLeft))
                    return True
                else:
                    queue.insert(0, (successorLeft, 'R'))
            else: print("Already visited!")

        if(rowIndex+1<len(StartState) and invalidDirection !='D'):
            # down Exists
            successorDown = copy.deepcopy(currentState)
            downElm = successorDown[rowIndex+1][colIndex]
            successorDown[rowIndex][colIndex] = downElm
            successorDown[rowIndex+1][colIndex] = ''
            if successorDown not in visited:
                if(successorDown == GoalState):
                    print("Puzzle is solved!!\n", print8Puzzle(successorDown))
                    return True
                else:
                    queue.insert(0, (successorDown, 'U'))
            else: print("Already visited!")
                
        if(rowIndex-1>=0 and invalidDirection !='U'):
            # up Exists
            successorUp =  copy.deepcopy(currentState)
            upElm = successorUp[rowIndex-1][colIndex]
            successorUp[rowIndex][colIndex] = upElm
            successorUp[rowIndex-1][colIndex] = ''
            if successorUp not in visited:
                if(successorUp == GoalState):
                    print("Puzzle is solved!!\n", print8Puzzle(successorUp))
                    return True
                else:
                    queue.insert(0, (successorUp, 'D'))
            else: print("Already visited!")

        print(totalVariationsProcessed)
    
    print("---Didn't Find Shit")
    return True

# ******************************************************************************************************************************************************
# ******************************************************************************************************************************************************
def print8Puzzle(arr):
    for row in arr:
        print(row)
    print("=====================")

# TheStartState = [[6,2,5],
#                 [1,8,''], 
#                 [7,4,3]]
TheStartState = [[1, 2, 3],
                ['', 4, 6],
                [5, 7, 8]]

# GoalState = [[7,6,5],
#             [8,'',4],
#             [1,2,3]]
GoalState = [[1, 4, 3],
            [5, 2, 6],
            [7,'', 8]]

solve_8_puzzle(TheStartState, GoalState)