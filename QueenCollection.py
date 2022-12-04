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
        self.collection.append(queen)

    def removeQueen(self,position:SleepingQueenPosition) -> Optional[Queen]:
        try:
            return self.collection.pop(position.getCardIndex())
        except IndexError:
            return None
    def getQueens(self) -> List[Queen]:
        return self.collection

class MoveQueen:
    def __init__(self,sleeping):
        self.sleeping_queens = sleeping
    def play(self, targetQueen: Position,attack) -> bool:
        if self.sleeping_queens[targetQueen.getCardIndex()] is not None:
                self.last = self.sleeping_queens[targetQueen.getCardIndex()]
                self.sleeping_queens[targetQueen.getCardIndex()] = None
                return True
        else:
            return False
    def getLastMoved(self):
        return self.last
