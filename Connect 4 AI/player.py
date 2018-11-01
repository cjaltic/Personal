# Ben Duggan and Connor Altic

import math

class Player:

    def __init__(self, depthLimit, isPlayerOne):

        self.isPlayerOne = isPlayerOne
        self.depthLimit = depthLimit

    # Returns a heuristic for the board position
    # Good positions for 0 pieces should be positive and good positions for 1 pieces
    # should be negative
    # this is really bad but whatever
    def heuristic(self, board):
        return self.heuristicTest(board)
        me = 0
        you = 1
        meValues = []
        youValues = []
        countMe = 0
        countYou = 0
        bonusMe = bonusYou = 0
        # horizontal-right checking
        for i in range(board.WIDTH - 3):
            for j in range(board.HEIGHT):
                meValues.append(countMe)
                youValues.append(countYou)
                countMe = 0
                countYou = 0
                for v in range(0,4):
                    x = i + v
                    y = j
                    if x < len(board.board) and y < len(board.board[x]):
                        if board.board[x][y] == me:
                            countMe = countMe + 1
                            if countYou == 3:
                                bonusMe = bonusMe + 1
                            countYou = 0
                        if board.board[x][y] == you:
                            countYou = countYou + 1
                            if countMe == 3:
                                bonusYou = bonusYou + 1
                            countMe = 0
        # horizontal-left checking
        for i in range(3,board.WIDTH):
            for j in range(board.HEIGHT):
                meValues.append(countMe)
                youValues.append(countYou)
                countMe = 0
                countYou = 0
                for v in range(0,4):
                    x = i - v
                    y = j
                    if 0 <= x < len(board.board) and y < len(board.board[x]):
                        if board.board[x][y] == me:
                            countMe = countMe + 1
                            if countYou == 3:
                                bonusMe = bonusMe + 1
                            countYou = 0
                        if board.board[x][y] == you:
                            countYou = countYou + 1
                            if countMe == 3:
                                bonusYou = bonusYou + 1
                            countMe = 0
        # vertical-up checking
        for i in range(board.WIDTH):
            for j in range(board.HEIGHT - 3):
                meValues.append(countMe)
                youValues.append(countYou)
                countMe = 0
                countYou = 0
                for v in range(0,4):
                    x = i
                    y = j + v
                    if x < len(board.board) and y < len(board.board[x]):
                        if board.board[x][y] == me:
                            countMe = countMe + 1
                            if countYou == 3:
                                bonusMe = bonusMe + 1
                            countYou = 0
                        if board.board[x][y] == you:
                            countYou = countYou + 1
                            if countMe == 3:
                                bonusYou = bonusYou + 1
                            countMe = 0
        # vertical-down checking
        for i in range(board.WIDTH):
            for j in range(3,board.HEIGHT):
                meValues.append(countMe)
                youValues.append(countYou)
                countMe = 0
                countYou = 0
                for v in range(0,4):
                    x = i
                    y = j - v
                    if x < len(board.board) and 0 <= y < len(board.board[x]):
                        if board.board[x][y] == me:
                            countMe = countMe + 1
                            if countYou == 3:
                                bonusMe = bonusMe + 1
                            countYou = 0
                        if board.board[x][y] == you:
                            countYou = countYou + 1
                            if countMe == 3:
                                bonusYou = bonusYou + 1
                            countMe = 0
        # northwest checking
        for i in range(3,board.WIDTH):
            for j in range(board.HEIGHT - 3):
                meValues.append(countMe)
                youValues.append(countYou)
                countMe = 0
                countYou = 0
                for v in range(0,4):
                    x = i - v
                    y = j + v
                    if 0 <= x < len(board.board) and 0 <= y < len(board.board[x]):
                        if board.board[x][y] == me:
                            countMe = countMe + 1
                            if countYou == 3:
                                bonusMe = bonusMe + 1
                            countYou = 0
                        if board.board[x][y] == you:
                            countYou = countYou + 1
                            if countMe == 3:
                                bonusYou = bonusYou + 1
                            countMe = 0
        # northeast checking
        for i in range(board.WIDTH - 3):
            for j in range(board.HEIGHT - 3):
                meValues.append(countMe)
                youValues.append(countYou)
                countMe = 0
                countYou = 0
                for v in range(0,4):
                    x = i + v
                    y = j + v
                    if 0 <= x < len(board.board) and 0 <= y < len(board.board[x]):
                        if board.board[x][y] == me:
                            countMe = countMe + 1
                            if countYou == 3:
                                bonusMe = bonusMe + 1
                            countYou = 0
                        if board.board[x][y] == you:
                            countYou = countYou + 1
                            if countMe == 3:
                                bonusYou = bonusYou + 1
                            countMe = 0
        # southeast checking
        for i in range(board.WIDTH - 3):
            for j in range(3,board.HEIGHT):
                meValues.append(countMe)
                youValues.append(countYou)
                countMe = 0
                countYou = 0
                for v in range(0,4):
                    x = i + v
                    y = j - v
                    if 0 <= x < len(board.board) and 0 <= y < len(board.board[x]):
                        if board.board[x][y] == me:
                            countMe = countMe + 1
                            if countYou == 3:
                                bonusMe = bonusMe + 1
                            countYou = 0
                        if board.board[x][y] == you:
                            countYou = countYou + 1
                            if countMe == 3:
                                bonusYou = bonusYou + 1
                            countMe = 0
        # southwest checking
        for i in range(3,board.WIDTH):
            for j in range(3,board.HEIGHT):
                meValues.append(countMe)
                youValues.append(countYou)
                countMe = 0
                countYou = 0
                for v in range(0,4):
                    x = i - v
                    y = j - v
                    if 0 <= x < len(board.board) and 0 <= y < len(board.board[x]):
                        if board.board[x][y] == me:
                            countMe = countMe + 1
                            if countYou == 3:
                                bonusMe = bonusMe + 1
                            countYou = 0
                        if board.board[x][y] == you:
                            countYou = countYou + 1
                            if countMe == 3:
                                bonusYou = bonusYou + 1
                            countMe = 0

        # now use these two values to calculate heuristic value
        countGood = 0
        countBad = 0
        for value in meValues:
            if value == 1:
                countGood = countGood + 1
            if value == 2:
                countGood = countGood + 3
            if value == 3:
                countGood = countGood + 9
            if value == 4:
                countGood = countGood + 100
        for value in youValues:
            if value == 1:
                countBad = countBad + 1
            if value == 2:
                countBad = countBad + 3
            if value == 3:
                countBad = countBad + 9
            if value == 4:
                countBad = countBad + 100
        countGood = countGood + (bonusMe * 90)
        countBad = countBad + (bonusYou * 90)
        boardValue = countGood - countBad
        if board.numMoves % 2 == 0:
            boardValue = boardValue * -1

        return boardValue

    def heuristicTest(self, board):
        if board.isTerminal() == 1:
            return 5000
        if board.isTerminal() == 2:
            return -5000
        countO = 0
        countX = 0
        count = 0
        for i in range(board.WIDTH):
            for j in range(len(board.board[i])):
                if j < len(board.board[i]):
                    for h in range(8):

                        for v in range(0,4):
                            x = i
                            y = j
                            if h == 0:
                                x = i + v
                                y = j
                            if h == 1:
                                x = i - v
                                y = j
                            if h == 2:
                                x = i
                                y = j + v
                            if h == 3:
                                x = i
                                y = j - v
                            if h == 4:
                                x = i + v
                                y = j + v
                            if h == 5:
                                x = i - v
                                y = j - v
                            if h == 6:
                                x = i + v
                                y = j - v
                            if h == 7:
                                x = i - v
                                y = j + v
                            if 0 <= x < len(board.board) and 0 <= y < len(board.board[x]):
                                if board.board[x][y] == 0:
                                    countO = countO + 1
                                if board.board[x][y] == 1:
                                    countX = countX + 1
                        if countX == 1 and countO == 0:
                            count = count - 1
                        if countX == 2 and countO == 0:
                            count = count - 10
                        if countX == 3 and countO == 0:
                            count = count - 50
                        if countO == 1 and countX == 0:
                            count = count + 1
                        if countO == 1 and countX == 2:
                            count = count + 10
                        if countO == 1 and countX == 3:
                            count = count + 100
                        if countO == 2 and countX == 0:
                            count = count + 10
                        if countO == 2 and countX == 1:
                            count = count - 10
                        if countO == 3 and countX == 0:
                            count = count + 50
                        if countO == 3 and countX == 1:
                            count = count - 100
                        countX = countO = 0
        return count


class PlayerHuman(Player):
    def __init(self, depthLimit=5, isPlayerOne=True):
        super().__init__(depthLimit, isPlayerOne)

    def findMove(self, board):
        print("Enter a column number (1-", str(board.WIDTH), "): ")
        return int(input())-1

class PlayerMM(Player):
    def __init__(self, depthLimit, isPlayerOne):
        super().__init__(depthLimit, isPlayerOne)

    def minmax(self, board, depth):
        terminal = board.isTerminal()
        if terminal == 0: return None, 0
        if terminal == 1: return None, 100 * (depth+1)
        if terminal == 2: return None, -100 * (depth+1)

        if depth == 0:
            return None, self.heuristic(board)

        best_move = None
        best_score = None

        for move in board.children():
            score = self.minmax(move[1], depth-1)[1]

            #print("depth: ", str(depth), "score: ", score)
            #move[1].print()

            if best_move is None or (board.numMoves%2==0 and score > best_score) or (board.numMoves%2==1 and score < best_score):
                best_score = score
                best_move = move[0]

        return best_move, best_score


    #returns the optimal column to move in by implementing the Minimax algorithm
    def findMove(self, board):
        x = self.minmax(board, self.depthLimit)
        print(str(x[1]))
        return x[0]

class PlayerAB(Player):
    def __init__(self, depthLimit, isPlayerOne):
        super().__init__(depthLimit, isPlayerOne)

    def alphabeta(self, board, depth, alpha=-32768, beta=32768):
        if board.isTerminal() == 0: return None, 0
        if board.isTerminal() == 1: return None, 100 * (depth+1)
        if board.isTerminal() == 2: return None, -100 * (depth+1)

        if depth == 0:
            return None, self.heuristic(board)

        best_move = None
        best_score = None

        for move in board.children():
            score = self.alphabeta(move[1], depth-1, alpha, beta)[1]

            #print("depth: ", str(depth), "score: ", score)
            #move[1].print()


            if board.numMoves%2==0:
                if best_move is None or score > best_score:
                    best_score = score
                    best_move = move[0]

                    if score > alpha:
                        alpha = score
                        if alpha >= beta:
                            break
            else:
                if best_move is None or score < best_score:
                    best_score = score
                    best_move = move[0]

                    if score < beta:
                        beta = score
                        if alpha >= beta:
                            break

        return best_move, best_score

    #TODO
    #returns the optimal column to move in by implementing the Alpha-Beta algorithm
    def findMove(self, board):
        return self.alphabeta(board, self.depthLimit)[0]

class PlayerABDP(Player):

    def __init__(self, depthLimit, isPlayerOne):
        super().__init__(depthLimit, isPlayerOne)

        self.resolved = {}

    #TODO
    #returns the optimal column to move in by implementing the Alpha-Beta algorithm with dynamic programming
    def findMove(self, board):
        pass



#######################################################
###########Example Subclass for Testing
#######################################################

#This will inherit your findMove from above, but will override the heuristic function with
#a new one; you can swap out the type of player by changing X in "class TestPlayer(X):"
class TestPlayer(PlayerMM):

    def __init__(self, depthLimit, isPlayerOne):
        super().__init__(depthLimit, isPlayerOne)

    #define your new heuristic here
    def heurisitic(self):
        pass


if __name__ == '__main__':
    pass

