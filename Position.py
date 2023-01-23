from typing import Union


class SleepingQueenPosition:
    def __init__(self, cardIndex: int):
        self.cardIndex = cardIndex

    def getCardIndex(self) -> int:
        return self.cardIndex


class AwokenQueenPosition:
    def __init__(self, cardIndex: int, player: int):
        self.cardIndex = cardIndex
        self.player = player

    def getCardIndex(self) -> int:
        return self.cardIndex

    def getPlayerIdx(self) -> int:
        return self.player

class HandPosition:

    def __init__(self, cardidx: int, player: int):
        self.cardIdx: int = cardidx
        self.playeridx: int = player

    def __repr__(self):
        return f"{self.cardIdx} {self.playeridx}"

    def getCardidx(self) -> int:
        return self.cardIdx

    def getPlayerIdx(self) -> int:
        return self.playeridx


Position = Union[SleepingQueenPosition, AwokenQueenPosition, HandPosition]

