from map import*
from cube import*
class beginnersmethod:

    def __init__(self, map):
        self.cube = map
        self.moveCount = 0
        self.log = []

    def makeMove(self, move):
        self.log.append(move)
        self.cube.makeMove(move)
        self.moveCount = self.moveCount + 1

    def flipCorner(self,i):
        c = Cube(self.cube)
        while c.cube[4].ore != 0 and c.cube[4].id == i:
            self.makeMove((4,3))
            self.makeMove((1,3))
            self.makeMove((4,1))
            self.makeMove((1,1))
            self.makeMove((4,3))
            self.makeMove((1,3))
            self.makeMove((4,1))
            self.makeMove((1,1))
            c = Cube(self.cube)

    # find and put piece 4 into place
    def firstPiece(self):
        c = Cube(self.cube)
        # if its in the upper layer
        i = c.findPiece(4)
        if i == 4:
            self.flipCorner(4)
            return
        if i < 4:
            if c.cube[0].id == 4:
                self.makeMove((4,2))
            if c.cube[1].id == 4:
                self.makeMove((2,1))
                self.makeMove((3,2))
            if c.cube[2].id == 4:
                self.makeMove((0,2))
            if c.cube[3].id == 4:
                self.makeMove((4,1))
        else:
            if c.cube[5].id == 4:
                self.makeMove((3,3))
            if c.cube[6].id == 4:
                self.makeMove((3,2))
            if c.cube[7].id == 4:
                self.makeMove((3,1))
        self.flipCorner(4)
    def secondPiece(self):
        c = Cube(self.cube)
        i = c.findPiece(5)
        if i > 5:
            if i == 7:
                self.makeMove((5,1))
            self.makeMove((2,1))
        if i < 4:
            while c.cube[2].id != 5:
                self.makeMove((1,1))
                c = Cube(self.cube)
            self.makeMove((2,3))
        self.makeMove((3,3))
        self.flipCorner(5)
        self.makeMove((3,1))
    def thirdPiece(self):
        c = Cube(self.cube)
        i = c.findPiece(6)
        if i == 6:
            pass
        if i == 7:
            self.makeMove((5,1))
        if i < 4:
            while c.cube[1].id != 6:
                self.makeMove((1,1))
                c = Cube(self.cube)
            self.makeMove((5,3))
        self.makeMove((3,2))
        self.flipCorner(6)
        self.makeMove((3,2))
    def fourthPiece(self):
        c = Cube(self.cube)
        i = c.findPiece(7)
        if i < 4:
            while c.cube[0].id != 7:
                self.makeMove((1,1))
                c = Cube(self.cube)
            self.makeMove((4,1))
            self.makeMove((1,1))
            self.makeMove((4,3))
        self.makeMove((3,1))
        self.flipCorner(7)

    def oLL(self):
        correct = 0
        for i in self.cube.state[1]:
            if i == 1:
                correct = correct + 1
        if correct == 4:
            return
        if correct == 2:
            c = Cube(self.cube)

            if (self.cube.state[1][1] == 1 and self.cube.state[1][3] == 1) or (self.cube.state[1][0] == 1 and self.cube.state[1][2] == 1):
                while self.cube.state[2][1] != 1:
                    self.makeMove((1,1))
                    c = Cube(self.cube)
            c = Cube(self.cube)
            while c.cube[0].ore != 0 or c.cube[3].ore != 0:
                self.makeMove((1,1))
                c = Cube(self.cube)
            c = Cube(self.cube)
            if self.cube.state[0][1] == 1:
                self.makeMove((4,3))
                self.makeMove((1,3))
                self.makeMove((4,1))
                self.makeMove((1,1))
                self.makeMove((2,1))
                self.makeMove((1,3))
                self.makeMove((2,3))
                self.makeMove((0,1))
            else:
                self.makeMove((1,2))
                self.makeMove((0,1))
                self.makeMove((2,1))
                self.makeMove((1,1))
                self.makeMove((2,3))
                self.makeMove((1,3))
                self.makeMove((0,3))
        if correct == 1:
            while self.cube.state[1][3] != 1:
                self.makeMove((1,1))
            if self.cube.state[0][1] == 1:
                self.makeMove((2,1))
                self.makeMove((1,1))
                self.makeMove((2,3))
                self.makeMove((1,1))
                self.makeMove((2,1))
                self.makeMove((1,2))
                self.makeMove((2,3))
            else:
                self.makeMove((1,2))
                self.makeMove((2,1))
                self.makeMove((1,2))
                self.makeMove((2,3))
                self.makeMove((1,3))
                self.makeMove((2,1))
                self.makeMove((1,3))
                self.makeMove((2,3))
        if correct == 0:
            if (self.cube.state[2][0] == 1 and self.cube.state[2][1] == 1) or (self.cube.state[0][0] == 1 and self.cube.state[0][1] == 1):
                while self.cube.state[0][0] != 1:
                    self.makeMove((1,1))
                self.makeMove((2,2))
                self.makeMove((1,2))
                self.makeMove((2,1))
                self.makeMove((1,2))
                self.makeMove((2,2))
            else:
                while self.cube.state[0][1] != 1 and self.cube.state[4][1] != 1:
                    self.makeMove((1,1))
                self.makeMove((0,1))
                self.makeMove((2,1))
                self.makeMove((1,1))
                self.makeMove((2,3))
                self.makeMove((1,3))
                self.makeMove((2,1))
                self.makeMove((1,1))
                self.makeMove((2,3))
                self.makeMove((1,3))
                self.makeMove((0,3))

    def pLL(self):
        if self.cube.state[4][0] == self.cube.state[4][1] and self.cube.state[0][0] == self.cube.state[0][1]:
            pass
        elif self.cube.state[4][0] == self.cube.state[4][1] or self.cube.state[0][0] == self.cube.state[0][1] or self.cube.state[2][0] == self.cube.state[2][1] or self.cube.state[5][2] == self.cube.state[5][3]:
            while self.cube.state[4][0] != self.cube.state[4][1]:
                self.makeMove((1,1))
            self.makeMove((2,1))
            self.makeMove((1,1))
            self.makeMove((2,3))
            self.makeMove((1,3))
            self.makeMove((2,3))
            self.makeMove((0,1))
            self.makeMove((2,2))
            self.makeMove((1,3))
            self.makeMove((2,3))
            self.makeMove((1,3))
            self.makeMove((2,1))
            self.makeMove((1,1))
            self.makeMove((2,3))
            self.makeMove((0,3))
        else:
            self.makeMove((0,1))
            self.makeMove((2,1))
            self.makeMove((1,3))
            self.makeMove((2,3))
            self.makeMove((1,3))
            self.makeMove((2,1))
            self.makeMove((1,1))
            self.makeMove((2,3))
            self.makeMove((0,3))
            self.makeMove((2,1))
            self.makeMove((1,1))
            self.makeMove((2,3))
            self.makeMove((1,3))
            self.makeMove((2,3))
            self.makeMove((0,1))
            self.makeMove((2,1))
            self.makeMove((0,3))
        while not self.cube.isSolved():
            self.makeMove((1,1))

        for i in range(5):
            self.makeMove((6,1))
            self.makeMove((7,1))
            self.makeMove((8,3))







if __name__ == '__main__':
    m = Map()
    m.scramble(2)







