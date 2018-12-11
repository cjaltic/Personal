import pygame
from maze import *
from player import *

class GUI():
    def __init__(self, maze):
        pygame.display.set_caption("Maze Evolution")
        self.x = maze.player[1]
        self.y = maze.player[0]
        self.win = pygame.display.set_mode((500,300))
        self.board = maze.board
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j] == 'g':
                    pygame.draw.rect(self.win, (255,255,0), (j*10,i*10, 10,10))
                if self.board[i][j] == 'o':
                    pygame.draw.rect(self.win, (255, 255, 224), (j * 10, i * 10, 10, 10))
                if self.board[i][j] == 'x':
                    pygame.draw.rect(self.win, (255, 218, 185), (j * 10, i * 10, 10, 10))
                if self.board[i][j] == 'p':
                    pygame.draw.rect(self.win, (173,255,47), (j * 10, i * 10, 10, 10))
        pygame.display.update()
        self.size = 10

    def update(self, maze):
        self.x = maze.player[1]
        self.y = maze.player[0]
        self.board = maze.board


    def draw(self):
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j] == 'g':
                    pygame.draw.rect(self.win, (255,255,0), (j*10,i*10, 10,10))
                if self.board[i][j] == 'o':
                    pygame.draw.rect(self.win, (255, 255, 224), (j * 10, i * 10, 10, 10))
                if self.board[i][j] == 'x':
                    pygame.draw.rect(self.win, (255, 218, 185), (j * 10, i * 10, 10, 10))
                if self.board[i][j] == 'p':
                    pygame.draw.rect(self.win, (173,255,47), (j * 10, i * 10, 10, 10))
        pygame.display.update()







if __name__ == '__main__':
    m = Maze()
    g = GUI(m)
    scores = []
    players = []
    for i in range(200):
        p = Player()
        p.randomMoves(50)
        players.append(p)

    r = True
    while r:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                r = False

        if m.board[m.player[0] - 1][m.player[1]] == 'o' :
            m.move(0)
            print(0)
        elif m.board[m.player[0]][m.player[1] + 1] == 'o':
            m.move(1)
            print(1)
        else:
            m.move(3)
            print(3)
        g.update(m)
        g.draw()
        pygame.time.delay(100)


    for i in range(200):
        p = Player()
        p.randomMoves(5)
        players.append(p)

    run = True
    x = 1
    for p in players:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        keys = pygame.key.get_pressed()
        for n in p.moves:
            m.move(n)
            pygame.time.delay(10)
            g.draw()
            g.update(m)

        print(m.score())
        scores.append(m.score())
        pygame.time.delay(100)
        if keys[pygame.K_LEFT]:
            m.move(3)
        if keys[pygame.K_DOWN]:
            m.move(2)
        if keys[pygame.K_RIGHT]:
            m.move(1)
        if keys[pygame.K_UP]:
            m.move(0)
        g.update(m)
        g.draw()
        m = Maze()
    index = 0
    max = 0
    for i in range(len(scores)):
        if scores[i] > max:
            max = scores[i]
            index = i
    print(index)
    print(max)
    m = Maze()
    g.update(m)
    for i in players[index].moves:
        m.move(n)
        g.update(m)
        pygame.time.delay(1000)
        








