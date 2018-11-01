# Ben Duggan and Connor Altic

#######################        BOARD CLASS        ###########################
# The Board class is the data structure that holds the Connect 4 boards and the game operations

# The Connect 4 board is 7 cells wide and 6 cells tall

# The underlying data structure is a 2-d list
# The first dimension is the column; the second dimension is the row
# Note: each column ONLY contains pieces (no empty cell). Thus, the array is jagged.

# Every cell in the above list contains either a 0 or a 1. Player 1 is represented by 0 tiles, and Player
# 2 is represented by 1 tiles. Yes, this is confusing, but it helps with the efficiency of the code.
#
##############################################################################
class Board(object):

    #static class variables - shared across all instances
    HEIGHT = 6
    WIDTH = 7

    def __init__(self, orig=None, hash=None):

        #copy
        if(orig):
            self.board = [list(col) for col in orig.board]
            self.numMoves = orig.numMoves
            self.lastMove = orig.lastMove
            return

        #creates from hash - NOTE: Does not understand move order
        elif(hash):
            self.board = []
            self.numMoves = 0
            self.lastMove = None

            #convert to base 3
            digits = []
            while hash:
                digits.append(int(hash % 3))
                hash //= 3

            col = []

            for item in digits:

                #2 indicates new column
                if item == 2:
                    self.board.append(col)
                    col = []

                #otherwise directly append base number
                else:
                    col.append(item)
                    self.numMoves += 1
            return

        #create new
        else:
            self.board = [[] for x in range(self.WIDTH)]
            self.numMoves = 0
            self.lastMove = None
            return


    ########################################################################
    #                           Mutations
    ########################################################################

    # Puts a pirce in the appropriate column and checks to see if it was a winning move
    # Pieces are either 1 or 0; automatically decided
    # NOTE: does NOT check if the move is valid
    def makeMove(self, column):
        #update board data
        piece = self.numMoves % 2
        self.lastMove = (piece, column)
        self.numMoves += 1
        self.board[column].append(piece)


    ########################################################################
    #                           Observations
    ########################################################################

    # Generates a list of the valid children of the board
    # A child is of the form (move_to_make_child, child_object)
    def children(self):
        children = []
        for i in range(7):
            if len(self.board[i]) < 6:
                child = Board(self)
                child.makeMove(i)
                children.append((i, child))
        return children

    # Returns:
    #  -1 if game is not over
    #   0 if the game is a draw
    #   1 if player 1 wins
    #   2 if player 2 wins
    def isTerminal(self):
        if self.numMoves < 4:
            return -1

        move = self.lastMove[0]
        moveCord = self.lastMove[1], len(self.board[self.lastMove[1]])-1

        def tryInt(board, x, y):
            try:
                if x < 0 or y < 0:
                    return -1
                return board.board[x][y]
            except:
                return -1

        # Horizontal
        maxMoves = 0
        if tryInt(self, 0, moveCord[1]) == move: maxMoves += 1 #0
        else: maxMoves = 0
        if maxMoves == 4:
            if move == 0: return 1
            else: return 2
        if tryInt(self, 1, moveCord[1]) == move: maxMoves += 1 #1
        else: maxMoves = 0
        if maxMoves == 4:
            if move == 0: return 1
            else: return 2
        if tryInt(self, 2, moveCord[1]) == move: maxMoves += 1 #2
        else: maxMoves = 0
        if maxMoves == 4:
            if move == 0: return 1
            else: return 2
        if tryInt(self, 3, moveCord[1]) == move: maxMoves += 1 #3
        else: maxMoves = 0
        if maxMoves == 4:
            if move == 0: return 1
            else: return 2
        if tryInt(self, 4, moveCord[1]) == move: maxMoves += 1 #4
        else: maxMoves = 0
        if maxMoves == 4:
            if move == 0: return 1
            else: return 2
        if tryInt(self, 5, moveCord[1]) == move: maxMoves += 1 #5
        else: maxMoves = 0
        if maxMoves == 4:
            if move == 0: return 1
            else: return 2
        if tryInt(self, 6, moveCord[1]) == move: maxMoves += 1 #6
        else: maxMoves = 0
        if maxMoves == 4:
            if move == 0: return 1
            else: return 2

        # Vertical
        maxMoves = 0
        if tryInt(self, moveCord[0], 0) == move: maxMoves += 1 #0
        else: maxMoves = 0
        if maxMoves == 4:
            if move == 0: return 1
            else: return 2
        if tryInt(self, moveCord[0], 1) == move: maxMoves += 1 #1
        else: maxMoves = 0
        if maxMoves == 4:
            if move == 0: return 1
            else: return 2
        if tryInt(self, moveCord[0], 2) == move: maxMoves += 1 #2
        else: maxMoves = 0
        if maxMoves == 4:
            if move == 0: return 1
            else: return 2
        if tryInt(self, moveCord[0], 3) == move: maxMoves += 1 #3
        else: maxMoves = 0
        if maxMoves == 4:
            if move == 0: return 1
            else: return 2
        if tryInt(self, moveCord[0], 4) == move: maxMoves += 1 #4
        else: maxMoves = 0
        if maxMoves == 4:
            if move == 0: return 1
            else: return 2
        if tryInt(self, moveCord[0], 5) == move: maxMoves += 1 #5
        else: maxMoves = 0
        if maxMoves == 4:
            if move == 0: return 1
            else: return 2
        if tryInt(self, moveCord[0], 6) == move: maxMoves += 1 #6
        else: maxMoves = 0
        if maxMoves == 4:
            if move == 0: return 1
            else: return 2

        # Top left to bottom Right
        maxMoves = 0
        if tryInt(self, moveCord[0]-3, moveCord[1]+3) == move: maxMoves += 1 #0
        else: maxMoves = 0
        if maxMoves == 4:
            if move == 0: return 1
            else: return 2
        if tryInt(self, moveCord[0]-2, moveCord[1]+2) == move: maxMoves += 1 #1
        else: maxMoves = 0
        if maxMoves == 4:
            if move == 0: return 1
            else: return 2
        if tryInt(self, moveCord[0]-1, moveCord[1]+1) == move: maxMoves += 1 #2
        else: maxMoves = 0
        if maxMoves == 4:
            if move == 0: return 1
            else: return 2
        if tryInt(self, moveCord[0], moveCord[1]) == move: maxMoves += 1 #3
        else: maxMoves = 0
        if maxMoves == 4:
            if move == 0: return 1
            else: return 2
        if tryInt(self, moveCord[0]+1, moveCord[1]-1) == move: maxMoves += 1 #4
        else: maxMoves = 0
        if maxMoves == 4:
            if move == 0: return 1
            else: return 2
        if tryInt(self, moveCord[0]+2, moveCord[1]-2) == move: maxMoves += 1 #5
        else: maxMoves = 0
        if maxMoves == 4:
            if move == 0: return 1
            else: return 2
        if tryInt(self, moveCord[0]+3, moveCord[1]-3) == move: maxMoves += 1 #6
        else: maxMoves = 0
        if maxMoves == 4:
            if move == 0: return 1
            else: return 2

        # Bottom left to top right
        maxMoves = 0
        if tryInt(self, moveCord[0]-3, moveCord[1]-3) == move: maxMoves += 1 #0
        else: maxMoves = 0
        if maxMoves == 4:
            if move == 0: return 1
            else: return 2
        if tryInt(self, moveCord[0]-2, moveCord[1]-2) == move: maxMoves += 1 #1
        else: maxMoves = 0
        if maxMoves == 4:
            if move == 0: return 1
            else: return 2
        if tryInt(self, moveCord[0]-1, moveCord[1]-1) == move: maxMoves += 1 #2
        else: maxMoves = 0
        if maxMoves == 4:
            if move == 0: return 1
            else: return 2
        if tryInt(self, moveCord[0], moveCord[1]) == move: maxMoves += 1 #3
        else: maxMoves = 0
        if maxMoves == 4:
            if move == 0: return 1
            else: return 2
        if tryInt(self, moveCord[0]+1, moveCord[1]+1) == move: maxMoves += 1 #4
        else: maxMoves = 0
        if maxMoves == 4:
            if move == 0: return 1
            else: return 2
        if tryInt(self, moveCord[0]+2, moveCord[1]+2) == move: maxMoves += 1 #5
        else: maxMoves = 0
        if maxMoves == 4:
            if move == 0: return 1
            else: return 2
        if tryInt(self, moveCord[0]+3, moveCord[1]+3) == move: maxMoves += 1 #6
        else: maxMoves = 0
        if maxMoves == 4:
            if move == 0: return 1
            else: return 2

        if self.isFull():
            return 0
        else:
            return -1

    # Retuns a unique decimal number for each board object based on the
    # underlying data
    # NOTE: it is not important that you understand how this works
    def hash(self):

        power = 0
        hash = 0

        for column in self.board:

            # add 0 or 1 depending on piece
            for piece in column:
                hash += piece * (3 ** power)
                power += 1

            # add a 2 to indicate end of column
            hash += 2 * (3 ** power)
            power += 1

        return hash


    # Return true iff the game is full
    def isFull(self):
        return self.numMoves == 42

    # Prints out a visual representation of the board
    # X's are 1's and 0's are 0s
    def print(self):
        print("")
        print("+" + "---+" * self.WIDTH)
        for rowNum in range(self.HEIGHT - 1, -1, -1):
            row = "|"
            for colNum in range(self.WIDTH):
                if len(self.board[colNum]) > rowNum:
                    row += " " + ('X' if self.board[colNum][rowNum] else 'O') + " |"
                else:
                    row += "   |"
            print(row)
            print("+" + "---+" * self.WIDTH)

if __name__ == "__main__":

    ##########
    ## How to run a local game
    ##########

    # Create a new, empty board
    b = Board()



    b1 = [[1,1],[],[0,0,0,1],[],[],[],[]]
    b2 = [[1,1,1],[],[0,0,0],[],[],[],[]]
    b3 = [[0],[],[0,0,0,0],[],[1,1,1,0],[],[]]
    b4 = [[1],[],[0,0,1],[],[1,1,1],[],[]]
    b.board = b4
    b.numMoves = 7
    b.lastMove = (1,0)
    print(str(b.isTerminalTest()))

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
