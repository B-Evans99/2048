from random import *
from math import *


class Board:
    def __init__(self):
        self.grid = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
        self.addRandom()
        self.addRandom()
        self.score = 0

    def checkGameOver(self):
        for g in self.grid:
            for c in g:
                if(c == 0):
                    return False
        return True

    def won(self):
        for g in self.grid:
            for c in g:
                if(c == 2048):
                    self.score = 1000000
                    return True
        return False

    def addRandom(self):
        while(True):
            row = floor(random()*4)
            box = floor(random()*4)
            if(self.grid[row][box] == 0):
                self.grid[row][box] = 2
                break

    def rotateBoard(self):
        self.grid = list(zip(*self.grid[::-1]))
        grid = []
        for g in self.grid:
            grid.append(list(g))
        self.grid = grid

    def move(self, direction):
        # rotate board
        if(direction == "UP"):
            self.rotateBoard()
            self.rotateBoard()
            self.rotateBoard()
        if(direction == "RIGHT"):
            self.rotateBoard()
            self.rotateBoard()
        if(direction == 'DOWN'):
            self.rotateBoard()

        # move left
        grid = []
        for g in self.grid:
            row = []
            for c in g:
                if(c != 0):
                    row.append(c)
            row = row + [0]*(4 - len(row))
            for (i, c) in enumerate(row[:-1]):
                if(c != 0 and row[i+1] == c):
                    row[i] = row[i] * 2
                    self.score += row[i]
                    row[i+1] = 0
            final = []
            for c in row:
                if(c != 0):
                    final.append(c)
            final = final + [0]*(4 - len(final))
            grid.append(row)
        change = self.grid != grid
        self.grid = grid

        if(direction == "UP"):
            self.rotateBoard()
        if(direction == "RIGHT"):
            self.rotateBoard()
            self.rotateBoard()
        if(direction == "DOWN"):
            self.rotateBoard()
            self.rotateBoard()
            self.rotateBoard()
        return change

    def print(self):
        print("")
        for g in self.grid:
            for c in g:
                x = str(c).rjust(4, ' ')
                print(x, end="")
            print("")
        print("\n\n")


class Control:
    def __init__(self):
        self.board = Board()
        self.gameOver = False

    def result(self):
        return False

    def gameWon(self):
        self.gameOver = True

    def gameLost(self):
        self.gameOver = True

    def isGameOver(self):
        return self.gameOver

    def getScore(self):
        return self.board.score

    def move(self, direction):
        if(self.board.won()):
            self.gameWon()
        elif(self.board.checkGameOver()):
            self.gameLost()
        else:
            success = self.board.move(direction)
            if(success):
                self.board.addRandom()
            return success

    def getInputs(self):
        ret = []
        for r in self.board.grid:
            for c in r:
                ret.append(c)
        return ret


control = Control()
