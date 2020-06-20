import random as r

class Player():

    p1Selection = ''

    p2Selection = ''

    def getPlayerSelection(self):
        self.p1Selection = input('First turn is selected randomly. Would you like to be X or O? ').capitalize()
        while self.p1Selection not in ['O','X']:
            self.p1Selection = input('Input was invalid. Please try again. ').capitalize() # Accessing Player sets the class to have that value
        if (self.p1Selection == 'X'):                                                      # Assigning self is for the instance
            self.p2Selection = 'O'
        else: 
            self.p2Selection = 'X'

    def getUserTurn(self, board):
        game = Game(self)
        row = -1
        col = -1
        boardRows = range(len(board))
        boardCols = range(len(board[0]))

        while game.checkIfEmpty(row, col):
            # print('There is already a value there. Please try again. ')

            row = int(input('Which row do you choose? '))
            while row not in range(len(boardRows)):
                row = int(input('This is not a valid row. Please try again. '))

            col = int(input('Which column do you choose? '))
            while col not in range(len(boardCols)):
                col = int(input('This is not a valid column. Please try again. '))

            game.setBoardValue(row, col)


class Game(Player):

    p1Turn = False # Boolean to keep track of whos turn it is

    def __init__(self, player):
        self.board = [['', '', ''],  # Define board as two dimensional array. Can make this scalable to any size with a bit or rework
                      ['', '', ''],
                      ['', '', '']]

        self.player = player


    def drawBoard(self):
        print('   1', '  2', '  3')
        for i in range(len(self.board)):
            print(i + 1, self.board[i][0] + '   |' + self.board[i][1] + '   |' + self.board[i][2]) # Draw board dynamically
            try:
                if (self.board[i + 1]):
                    print('  -----------')
            except IndexError: # Except to keep going if next index is null
                pass


    def startPlayerVsPlayer(self, rand):
        print('Player ' + str(rand) + "'s turn")
        if (rand == 1):
            Game.p1Turn = True
        self.drawBoard()
        self.player.getUserTurn(self.board)


    def startPlayerVsComputer(self, rand):
        self.drawBoard()
        if (rand == 1):
            print("Player 1's turn")
            p1Turn = True
            Player.getUserTurn()
        else: 
            print ("Computer's turn")

    
    def setBoardValue(self, row, col):
        if self.p1Turn:
            self.board[row - 1][col - 1] = self.player.p1Selection
            return True
        else:
            self.board[row - 1][col - 1] = self.player.p1Selection
            return True
        return False

    def checkIfEmpty(self, row, col):
        if (not self.board[row - 1][col - 1]):
            return True
        return False

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