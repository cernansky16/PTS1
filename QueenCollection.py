from __future__ import annotations


from typing import List, Optional,Union,TYPE_CHECKING
if TYPE_CHECKING:
    from Position import SleepingQueenPosition, AwokenQueenPosition
    from Card_CardType import Queen
class QueenCollectionInterface:
    def addAwoken(self, queen: Optional[Queen]) -> None:
        pass

    def addSleeping(self, queen: Queen) -> None:
        pass

    def removeAwokenQueen(self, position: AwokenQueenPosition) -> Optional[Queen]:
        pass

    def removeSleepingQueen(self, position: SleepingQueenPosition) -> Optional[Queen]:
        pass

    def getQueens(self) -> List[Optional[Queen]]:
        return []


class QueenCollection(QueenCollectionInterface):
    def __init__(self, collection=None)->None:
        if collection is None:
            self.collection: List[Optional[Queen]] = list()
        else:
            self.collection = collection

    def addAwoken(self, queen: Optional[Queen]) -> None:
        if queen is None:
            return
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
            if queen is None:
                return None
            self.collection[position.getCardIndex()] = None
            return queen
        except IndexError:
            return None
    def __getitem__(self, item:int)->Optional[Queen]:
        return self.collection[item]

    def getQueens(self) -> List[Optional[Queen]]:
        return self.collection


class MoveQueenInterface:
    def play(self, targetQueen: SleepingQueenPosition) -> bool:
        return False

    def add(self, queen: Queen) -> None:
        pass

    def getLastMoved(self):
        pass


class MoveQueen(MoveQueenInterface):

    def __init__(self, sleeping)->None:
        self.sleeping_queens: QueenCollection = sleeping
        
    def play(self, targetQueen: SleepingQueenPosition) -> bool:
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


