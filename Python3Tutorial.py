board =  [['1', '1', '2'],
          ['2', '1', '2'],
          ['2', '2', '1']]

# diag = []

# for index in range(len(board)):
#     diag.append(board[index][index])
# for i in diag:
#     print(i)

boardLength = range(len(board))
diagonalValues = zip(boardLength, reversed((boardLength)))

for i, j in diagonalValues:
    print(i, j)
    
print()

for i, j in enumerate(reversed(boardLength)): # Same thing as loop above but looks much cleaner this way and simpler
    print(i, j)



# Alt + Shift + up or down to add cursor
# (0,0), (1,1), (2,2) or (0,2), (1,1), (2,0)

