board =    [['', '', ''],  # Define board as two dimensional array. Can make this scalable to any size with a bit or rework
            ['', '', ''],
            ['', '', '']]


def drawBoard():
    for i in range(len(board)):
        print(board[i][0] + '  |' + board[i][1] + '   |' + board[i][2]) # Draw board dynamically
        try:
            if (board[i + 1]):
                print('---------')
        except IndexError: # Except to trying to read null
            pass

def startPlayerVsPlayer():
    # start message here
    drawBoard()



def startPlayerVsComputer():
    # start message here
    drawBoard()




def main():
    optionSelection = ''
    while optionSelection not in [1, 2, 3]:
        optionSelection = int(input('Please select one:\n 1. Enter 1 to go against a player \n 2. Enter 2 to go against the computer \n 3. Enter 3 to Exit \n'))
        if (optionSelection == 1):
            selection = getPlayerSelection()
            startPlayerVsPlayer()
        elif(optionSelection == 2):
            selection = getPlayerSelection()
            startPlayerVsComputer()
        elif(optionSelection == 3):
            print('Farewell!')
        else:
            print ('Value is invalid. Please try again.')

def getPlayerSelection():
    playerSelection = input('First turn is selected randomly. Would you like to be X or O? ').capitalize()
    while playerSelection not in ['O','X']:
        playerSelection = input('Input was invalid. Please try again. ').capitalize()
    return playerSelection


main()