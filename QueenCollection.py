from Card_CardType import Queen
from Position import SleepingQueenPosition,Position,AwokenQueenPosition
from random import shuffle
class QueenCollection:
    def add(self,queen:Queen):
        pass
    def removeQueen(self,position:SleepingQueenPosition):
        pass
    def getQueens(self): #map[Position,Queen]
        pass
class AwokenQueens(QueenCollection):
    def __init__(self):
        self.playeridx: int
    def addQueen(self,queen:Queen):
        pass
    def pickQueen(self, position:AwokenQueenPosition):
        pass

    def getplayerIndex(self):
        return self.playeridx

class SleepingQueens(QueenCollection):
    def __init__(self):
        self.sleeping_queens = [Queen(5), Queen(5), Queen(5), Queen(5), Queen(10), Queen(10), Queen(10), Queen(10),
                  Queen(15), Queen(15), Queen(15), Queen(20)]
        shuffle(self.sleeping_queens)

