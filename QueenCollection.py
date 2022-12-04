from Card_CardType import Queen
from Position import SleepingQueenPosition,Position
from typing import List,Optional

class QueenCollection:
    def __init__(self, collection= None):
        if collection is None:
            self.collection = list()
        else:
            self.collection: List[Queen] = collection

    def add(self,queen:Queen) -> None:
        if len(self.collection) == 12:
            for i in range(12):
                if self.collection[i] is None:
                    self.collection[i] = queen
                    return
        else:
            self.collection.append(queen)
            return

    def removeQueen(self,position: Position) -> Optional[Queen]:
        if len(self.collection) == 12:
            try:
                queen = self.collection[position.getCardIndex()]
                self.collection[position.getCardIndex()] = None
                return queen
            except IndexError:
                return None
        else:
            try:
                return self.collection.pop(position.getCardIndex())
            except IndexError:
                return None
    def getQueens(self) -> List[Queen]:
        return self.collection

class MoveQueen:
    def __init__(self,sleeping):
        self.sleeping_queens: QueenCollection= sleeping
    def play(self, targetQueen: Position) -> bool:
        if self.sleeping_queens.getQueens()[targetQueen.getCardIndex()] is not None:
                self.last = self.sleeping_queens.removeQueen(targetQueen)
                return True
        else:
            return False
    def getLastMoved(self):
        return self.last


