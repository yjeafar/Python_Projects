import random as r

class Player():

    def getPlayerSelection(self):
        self.p1Selection = input('First turn is selected randomly. Would you like to be X or O? ').capitalize()
        while self.p1Selection not in ['O','X']:
            self.p1Selection = input('Input was invalid. Please try again. ').capitalize() # Accessing Player sets the class to have that value
        if (self.p1Selection == 'X'):                                                      # Assigning self is for the instance
            self.p2Selection = 'O'
        else: 
            self.p2Selection = 'X'

    def getUserTurn(self):
        game = Game(self)
        row = -1
        col = -1
        boardRows = range(len(game.board))
        boardCols = range(len(game.board[0]))

        while not game.setBoardValue(row, col):
            if (row != -1 or col != -1):
                print('There is already a value there. Please try again. ')

            row = int(input('Which row do you choose? '))
            while row not in range((len(boardRows) + 1)):
                row = int(input('This is not a valid row. Please try again. '))

            col = int(input('Which column do you choose? '))
            while col not in range((len(boardCols) + 1)):
                col = int(input('This is not a valid column. Please try again. '))

        return game


class Game(Player):

    p1Turn = False # Boolean to keep track of whos turn it is

    board =  [[' ', ' ', ' '],  # Define board as two dimensional array. Can make this scalable to any size with a bit or rework
              [' ', ' ', ' '],
              [' ', ' ', ' ']]

    def __init__(self, player):
        self.player = player


    def drawBoard(self):
        print('  1', '  2', '  3' )
        for i in range(len(Game.board)):
            print(i + 1, Game.board[i][0] + ' |' + Game.board[i][1] + '  |' + Game.board[i][2]) # Draw board dynamically
            try:
                if (Game.board[i + 1]):
                    print(' -----------')
            except IndexError: # Except to keep going if next index is null
                pass


    def startPlayerVsPlayer(self, rand):
        playerTurn = rand
        playerWin = False
        turnsPlayed = 1 # Keep track of number of turns
        while not playerWin and turnsPlayed != 9: # Hard coded 9 because that's the size of board, could be dynamic
            print('Player ' + str(playerTurn) + "'s turn")
            playerTurn = self.getPlayerTurn(playerTurn)
            self.drawBoard()
            self.player.getUserTurn()
            playerTurn += 1
            playerWin = self.checkWin()
        if turnsPlayed == 9 and not playerWin:
            print('Tie Game!')
        else:
            print('Player ' + str(playerTurn) + ' has won!')

        self.drawBoard() # Shows board for last time after user wins or there is a tie


    def startPlayerVsComputer(self, rand):
        self.drawBoard()
        if (rand == 1):
            print("Player 1's turn")
            p1Turn = True
        else: 
            print ("Computer's turn")
    
    def setBoardValue(self, row, col):
        if row == -1 or col == -1: # This represents the first turn
            return False
        
        if (Game.board[row - 1][col - 1] == ' '): # Check if value is empty
            if Game.p1Turn:
                Game.board[row - 1][col - 1] = self.player.p1Selection # If empty and it's p1's turn, put p1's value in the index
            else:
                Game.board[row - 1][col - 1] = self.player.p2Selection # If empty and it's p2's turn, put p2's value in the index
            return True
        return False

    def checkWin(self):
        win = False
        cols = []  # Holds columns to check vertical win
        diag = []  # Holds diagonal values to check diagonal win
        boardLength = range(len(Game.board)) # Range of board, repeated multiple times below

        for row in Game.board:
            if checkWinningRow(row):  # Checks for horizontal winner
                return True

        for row in boardLength:         # Checks for vertical winner. Puts all columns in an array and uses same check as horizontal
            for col in Game.board:
                cols.append(col[row])   # Add column to array
            if checkWinningRow(cols):   # If length is the same as the vertical length and all of those values are consecutive, nonempty
               return True              # values, then there is a vertical winner      
                                                   
        for index in boardLength:                   # Since diag can be won when index is (0,0), (1,1), (2,2), etc, this adds all diagonals in an array and 
            diag.append(Game.board[index][index])   # checks if array is the same. Checks top left to bottom right (\)
            if checkWinningRow(diag):
                return True

        for i, j in enumerate(reversed(boardLength)): # Enumerate instead of using zip (combining two lists) to get the range of 1 to board size. See Pythong3Tutoial for example
            diag.append(Game.board[i][j]) # Add values to list, use row to check if there is a winner. Check top right to bottom left (/)
            if checkWinningRow(diag):
                return True
        
        return False

    def checkWinningRow(self, row):
        if row.count(row[0]) == len(row) and row[0] != ' ': # Gets first value in row, if that's non-empty and the same length as the row, then there is a winner         
            return True                                     
        return False


    def getPlayerTurn(self, playerTurn):
        if (playerTurn == 1):
            Game.p1Turn = True
            return 2
        else:
            Game.p1Turn = False
            return 1
        

def main():
    player = Player()
    game = Game(player)
    optionSelection = ''
    rand = r.randrange(1, 3) # Choose either 1 or 2. 2 represents computer/player 2 depending on gamemode
    while optionSelection not in [1, 2, 3]:
        optionSelection = int(input('Please select one:\n 1. Enter 1 to go against a player \n 2. Enter 2 to go against the computer \n 3. Enter 3 to Exit \n'))
        if (optionSelection == 1):
            player.getPlayerSelection()
            game.startPlayerVsPlayer(rand)
        elif(optionSelection == 2):
            player.getPlayerSelection()
            game.startPlayerVsComputer(rand)
        elif(optionSelection == 3):
            print('Farewell!')
        else:
            print ('Value is invalid. Please try again.')

main()