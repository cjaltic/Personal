from maze import *
import random
class Player:

    def __init__(self):
        self.location = (29,21)
        self.moves = []

    # n is how many moves
    def randomMoves(self, n):
        for i in range(n):
            self.moves.append(random.randint(0,3))
if __name__ == '__main__':
    p = Player()
    p.randomMoves(10)
    print(p.moves)



