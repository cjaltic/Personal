from face import *
class Map:
    # map is the "map" of the cube state.  map has
    # a state which is a list of faces.  map can print
    # the map of the cube and rotate, changing state
    # later will have a hash attribute

    def __init__(self):
        front = [0,0,0,0]
        up = [1,1,1,1]
        right = [2,2,2,2]
        down = [3,3,3,3]
        left = [4,4,4,4]
        back = [5,5,5,5]
        self.state = [front, up, right, down, left, back]

    def isSolved(self):
        for i in self.state:
            if not i[0] == i[1] == i[2] == i[3]:
                return False
        return True

    def turnFront(self):
        f = Face([0,0,0,0])
        g = Face([0,0,0,0])
        h = Face([0,0,0,0])
        rotation = [f.asRows(self.state[1])[1], f.asCollums(self.state[2])[0],f.asRows(self.state[3])[0],f.asCollums(self.state[4])[1]]

        temp = Face(rotation)
        temp.rotateClockwise()

        f.rowToFace([g.asRows(self.state[1])[0], [temp.layout[0][1], temp.layout[0][0]]])
        self.state[1] = f.layout
        f.colToFace([temp.layout[1], g.asCollums(self.state[2])[1]])
        self.state[2] = f.layout
        f.rowToFace([[temp.layout[2][1], temp.layout[2][0]], g.asRows(self.state[3])[1]])
        self.state[3] = f.layout
        f.colToFace([g.asCollums(self.state[4])[0], temp.layout[3]])
        self.state[4] = f.layout
        self.state[0] = Face(self.state[0]).rotateClockwise()

    def turnUp(self):
        f = Face([0,0,0,0])
        g = Face([0,0,0,0])
        rotation = [f.asRows(self.state[0])[0], f.asRows(self.state[4])[0], f.asRows(self.state[5])[1], f.asRows(self.state[2])[0]]

        temp = Face(rotation)
        temp.rotateClockwise()

        f.rowToFace([temp.layout[0], g.asRows(self.state[0])[1]])
        self.state[0] = f.layout
        f.rowToFace([temp.layout[1], g.asRows(self.state[4])[1]])
        self.state[4] = f.layout
        f.rowToFace([g.asRows(self.state[5])[0], [temp.layout[2][1], temp.layout[2][0]]])
        self.state[5] = f.layout
        f.rowToFace([[temp.layout[3][1], temp.layout[3][0]], g.asRows(self.state[2])[1]])
        self.state[2] = f.layout
        self.state[1] = Face(self.state[1]).rotateClockwise()

    def turnRight(self):
        f = Face([0,0,0,0])
        g = Face([0,0,0,0])
        rotation = [f.asCollums(self.state[0])[1], f.asCollums(self.state[1])[1], f.asCollums(self.state[5])[1], f.asCollums(self.state[3])[1]]

        temp = Face(rotation)
        temp.rotateClockwise()

        f.colToFace([g.asCollums(self.state[0])[0], temp.layout[0]])
        self.state[0] = f.layout
        f.colToFace([g.asCollums(self.state[1])[0], temp.layout[1]])
        self.state[1] = f.layout
        f.colToFace([g.asCollums(self.state[5])[0], temp.layout[2]])
        self.state[5] = f.layout
        f.colToFace([g.asCollums(self.state[3])[0], temp.layout[3]])
        self.state[3] = f.layout
        self.state[2] = Face(self.state[2]).rotateClockwise()

    def turnDown(self):
        f = Face([0,0,0,0])
        g = Face([0,0,0,0])
        rotation = [f.asRows(self.state[0])[1], f.asRows(self.state[2])[1], f.asRows(self.state[5])[0], f.asRows(self.state[4])[1]]

        temp = Face(rotation)
        temp.rotateClockwise()


        f.rowToFace([g.asRows(self.state[0])[0], temp.layout[0]])
        self.state[0] = f.layout
        f.rowToFace([g.asRows(self.state[2])[0], temp.layout[1]])
        self.state[2] = f.layout
        f.rowToFace([[temp.layout[2][1], temp.layout[2][0]], g.asRows(self.state[5])[1]])
        self.state[5] = f.layout
        f.rowToFace([g.asRows(self.state[4])[0], [temp.layout[3][1], temp.layout[3][0]]])
        self.state[4] = f.layout
        self.state[3] = Face(self.state[3]).rotateClockwise()

    def turnLeft(self):
        f = Face([0,0,0,0])
        g = Face([0,0,0,0])
        rotation = [f.asCollums(self.state[1])[0], f.asCollums(self.state[0])[0], f.asCollums(self.state[3])[0], f.asCollums(self.state[5])[0]]

        temp = Face(rotation)
        temp.rotateClockwise()

        f.colToFace([temp.layout[0], g.asCollums(self.state[1])[1]])
        self.state[1] = f.layout
        f.colToFace([temp.layout[1], g.asCollums(self.state[0])[1]])
        self.state[0] = f.layout
        f.colToFace([temp.layout[2], g.asCollums(self.state[3])[1]])
        self.state[3] = f.layout
        f.colToFace([temp.layout[3], g.asCollums(self.state[5])[1]])
        self.state[5] = f.layout
        self.state[4] = Face(self.state[4]).rotateClockwise()

    def turnBack(self):
        f = Face([0,0,0,0])
        g = Face([0,0,0,0])
        rotation = [f.asRows(self.state[1])[0], f.asCollums(self.state[4])[0], f.asRows(self.state[3])[1], f.asCollums(self.state[2])[1]]

        temp = Face(rotation)
        temp.rotateClockwise()

        f.rowToFace([temp.layout[0], g.asRows(self.state[1])[1]])
        self.state[1] = f.layout
        f.colToFace([[temp.layout[1][1], temp.layout[1][0]], g.asCollums(self.state[4])[1]])
        self.state[4] = f.layout
        f.rowToFace([g.asRows(self.state[3])[0], temp.layout[2]])
        self.state[3] = f.layout
        f.colToFace([g.asCollums(self.state[2])[0], [temp.layout[3][1], temp.layout[3][0]]])
        self.state[2] = f.layout
        self.state[5] = Face(self.state[5]).rotateClockwise()

    # makeMove is a modifier that takes a move.  a move is a tuple containing int 0:5 saying which face
    # to rotate, and int 1:3 saying how many times to rotate
    def makeMove(self, move):
        f = move[0]

        for i in range(move[1]):
            if f == 0:
                m.turnFront()
            if f == 1:
                m.turnUp()
            if f == 2:
                m.turnRight()
            if f == 3:
                m.turnDown()
            if f == 4:
                m.turnLeft()
            if f == 5:
                m.turnBack()

    def printCube(self):
        for i in range(6):
            print("")
            if i == 0:
                print("Front -- 0")
            if i == 1:
                print("Up -- 1")
            if i == 2:
                print("Right -- 2")
            if i == 3:
                print("Down -- 3")
            if i == 4:
                print("Left -- 4")
            if i == 5:
                print("Back -- 5")
            Face(self.state[i]).printFace()


if __name__ == '__main__':
    m = Map()
    while(True):
        m.printCube()
        move = input('make a move')
        d = (int(move[0]), int(move[1]))
        m.makeMove(d)
