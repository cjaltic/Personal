# Ben Duggan and Connor Altic

from board import Board
from player import *
#import requests


class Game:


    def __init__(self, startBoard, player1, player2):
        self.startBoard = startBoard
        self.player1 = player1
        self.player2 = player2

    ########################################################################
    #                     Simulate a Local Game
    ########################################################################

    def simulateLocalGame(self):

        board = Board(orig=self.startBoard)
        isPlayer1 = True

        while(True):

            #finds the move to make
            if isPlayer1:
                move = self.player1.findMove(board)
            else:
                move = self.player2.findMove(board)

            #makes the move
            board.makeMove(move)
            board.print()

            #determines if the game is over or not
            isOver = board.isTerminal()
            if isOver == 0:
                print("It is a draw!")
                break
            elif isOver == 1:
                print("Player 1 wins!")
                break
            elif isOver == 2:
                print("Player 2 wins!")
                break
            else:
                isPlayer1 = not isPlayer1


    
    def playAgainstInstructor(self, difficulty):

        if difficulty < 0 or difficulty > 5:
            print("Difficulty must be between 0 and 5")
            return

        board = Board(orig=self.startBoard)
        isPlayer1 = True

        session = requests.get(instructorURL + "/startgame/" + str(difficulty)).cookies

        while (True):

            # finds the move to make
            if isPlayer1:
                move = self.player1.findMove(board)
            else:
                r = requests.get(instructorURL + "/getresponse/" + str(board.lastMove[1]), cookies=session)
                session = r.cookies
                move = int(r.text)

            # makes the move
            board.makeMove(move)
            board.print()

            # determines if the game is over or not
            isOver = board.isTerminal()
            if isOver == 0:
                print("It is a draw!")
                break
            elif isOver == 1:
                print("Player 1 wins!")
                break
            elif isOver == 2:
                print("Player 2 wins!")
                break
            else:
                isPlayer1 = not isPlayer1


if __name__ == "__main__":

    ##########
    ## How to run a local game
    ##########

    # Create a new, empty board
    b = Board()

    # Create player one by calling the
    # player class corresponding to the 
    # search algorithm the player uses.
    p1 = PlayerMM(5, True)  # 5 is the depth

    # Same for player 2
    p2 = PlayerMM(5, False)  # 5 is the depth


    b1 = [[1,1,1],[0],[0],[0],[],[],[]]
    b2 = [[1,1],[0],[0],[0],[1],[],[]]
    b3 = [[0,0,0],[1],[1],[1],[],[],[]]
    b4 = [[0,0],[1],[1],[1],[0],[],[]]

    b.board = b4
    b.numMoves = 6
    b.lastMove = (1,5)
    print(p2.heuristic(b))
    b.print()

    # Create the game instance using the
    # board and players you've made.

    #g = Game(b, p1, p2)

    # uncomment this line to play!
    #g.simulateLocalGame()
    """
    b.makeMove(0)
    b.makeMove(0)

    b.makeMove(1)
    b.makeMove(0)

    b.makeMove(2)
    b.makeMove(5)

    b.makeMove(5)
    b.print()
    print(str(p2.findMove(b)))
    """
    """
    b1 = [[],[],[],[],[0],[0],[0]]
    b.board = b1
    b.numMoves = 3
    b.lastMove = (0,4)
    print(p1.heuristic(b))

    
    b.print()

    print(str(p2.findMove(b)))

    for i in range(0, b.WIDTH):
        b.makeMove(i)
    
    b.print()

    p2.findMove(b).print()
    """



    # uncomment this section to play against
    # the instructor
    """

    ##########
    ## How to play against the instructor board
    ##########

    # Create a new, empty board
    b = Board()

    # Create your player by calling the
    # player class corresponding to the 
    # search algorithm the player uses.
    p1 = PlayerAB(5, True) # 5 is the depth

    # Create the game instance using the
    # board and players you've made.
    g = Game(b, p1, None) # you don't need a p2

    # call playAgainstInstructor() and 
    # give it a difficulty. 
    g.playAgainstInstructor(5)
    """
