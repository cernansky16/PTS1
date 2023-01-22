from Card_CardType import Queen
from Position import SleepingQueenPosition,AwokenQueenPosition
from typing import List, Optional,Union


class QueenCollectionInterface:
    def addAwoken(self, queen: Queen) -> None:
        pass

    def addSleeping(self, queen: Queen) -> None:
        pass

    def removeAwokenQueen(self, position: AwokenQueenPosition) -> Optional[Queen]:
        pass

    def removeSleepingQueen(self, position: SleepingQueenPosition) -> Optional[Queen]:
        pass

    def getQueens(self) -> List[Queen]:
        return []


class QueenCollection(QueenCollectionInterface):
    def __init__(self, collection=None):
        if collection is None:
            self.collection = list()
        else:
            self.collection: List[Queen] = collection

    def addAwoken(self, queen: Queen) -> None:
        self.collection.append(queen)

    def addSleeping(self,queen: Queen) -> None:
        """puts queen at the first free position"""
        for i in range(12):
            if self.collection[i] is None:
                self.collection[i] = queen
                return

    def removeAwokenQueen(self, position: AwokenQueenPosition) -> Optional[Queen]:
        try:
            return self.collection.pop(position.getCardIndex())
        except IndexError:
            return None

    def removeSleepingQueen(self, position: SleepingQueenPosition) -> Optional[Queen]:
        try:
            queen = self.collection[position.getCardIndex()]
            self.collection[position.getCardIndex()] = None
            return queen
        except IndexError:
            return None

    def getQueens(self) -> List[Queen]:
        return self.collection

class MoveQueenInterface:
    def play(self, targetQueen: Union[SleepingQueenPosition,AwokenQueenPosition]) -> bool:
        return False

    def add(self, queen: Queen) -> None:
        pass

    def getLastMoved(self):
        pass


class MoveQueen(MoveQueenInterface):

    def __init__(self, sleeping):
        self.sleeping_queens: QueenCollection = sleeping
        
    def play(self, targetQueen: Union[SleepingQueenPosition,AwokenQueenPosition]) -> bool:
        queens = self.sleeping_queens.getQueens()
        if queens[targetQueen.getCardIndex()] is not None:
            self.last = self.sleeping_queens.removeSleepingQueen(targetQueen)
            return True
        else:
            return False

    def add(self, queen: Queen) -> None:
        self.sleeping_queens.addSleeping(queen)

    def getLastMoved(self):
        return self.last


