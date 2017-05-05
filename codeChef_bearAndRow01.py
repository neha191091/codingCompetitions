#import numpy as np

# Problem
# Limak is a little polar bear. He is playing a video game and he needs your help.
# There is a row with N cells, each either empty or occupied by a soldier, denoted by '0' and '1' respectively. The goal of the game is to move all soldiers to the right (they should occupy some number of rightmost cells).
# The only possible command is choosing a soldier and telling him to move to the right as far as possible. Choosing a soldier takes 1 second, and a soldier moves with the speed of a cell per second. The soldier stops immediately if he is in the last cell of the row or the next cell is already occupied. Limak isn't allowed to choose a soldier that can't move at all (the chosen soldier must move at least one cell to the right).
# Limak enjoys this game very much and wants to play as long as possible. In particular, he doesn't start a new command while the previously chosen soldier moves. Can you tell him, how many seconds he can play at most?

# Input
# The first line of the input contains an integer T denoting the number of test cases. The description of T test cases follows.
# The only line of each test case contains a string S describing the row with N cells. Each character is either '0' or '1', denoting an empty cell or a cell with a soldier respectively.

# Output
# For each test case, output a single line containing one integer â�� the maximum possible number of seconds Limak will play the game.

numCases = int(input())
print(numCases)
for i in range(0, numCases):
    caseArray = input()
    firstPos = cost = 0
    lenArray = len(caseArray)
    while (firstPos < lenArray and caseArray[firstPos] != '1'):
        firstPos = firstPos + 1
    if (firstPos < lenArray):
        consOne = 1
        consZero = 0
        while (firstPos + consOne - 1 < lenArray - 1):
            i = firstPos + consOne
            consZero = 0
            while (i < lenArray and caseArray[i] == '1'):
                consOne = consOne + 1
                i = i + 1
            while (i < lenArray and caseArray[i] == '0'):
                consZero = consZero + 1
                i = i + 1
            if (consZero != 0):
                costupdate = consOne * (consZero + 1)
            else:
                costupdate = 0
            cost = cost + costupdate
            firstPos = firstPos + consZero
    print(cost)