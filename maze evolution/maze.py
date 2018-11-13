
class Maze:

    def __init__(self):
        self.board = []
        board = open("mazes/m1.txt", "r")
        for line in board:
            l = []
            for i in line:
                l.append(i)
            self.board.append(l)
        board.close()

        self.player = (29,21)
        self.board[self.player[0]][self.player[1]] = 'p'
        self.moves = []
        self.state = 0



    def printBoard(self):
        for i in self.board:
            print(i)

    # scores a given position
    def score(self):
        if self.state == 1:
            return 1000
        return 900 - (self.player[0] * 30)


    def move(self, i):
        coord = list(self.player)
        if i == 0:
            coord[0] -= 1
        if i == 1:
            coord[1] += 1
        if i == 2:
            coord[0] += 1
        if i == 3:
            coord[1] -= 1
        if 30 > coord[0] >= 0 and 50 > coord[1] >= 0 and self.board[coord[0]][coord[1]] != 'x':
            temp = self.player
            self.player = coord
            if self.board[self.player[0]][self.player[1]] == 'g':
                print("YOU WIN !!")
                self.state = 1
            self.board[self.player[0]][self.player[1]] = 'p'

            self.board[temp[0]][temp[1]] = 'o'
            self.moves.append(i)



if __name__ == '__main__':
    m = Maze("m1")
    m.printBoard()
    while m.state == 0:
        move = input("make move")
        m.move(int(move))
        m.printBoard()
    print(m.moves)






