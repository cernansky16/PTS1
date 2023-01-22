from __future__ import annotations
from typing import Union,TYPE_CHECKING

if TYPE_CHECKING:
    from Player import Player
    from Card_CardType import Card

class SleepingQueenPosition:
    def __init__(self, cardIndex: int):
        self.cardIndex = cardIndex

    def getCardIndex(self) -> int:
        return self.cardIndex


class AwokenQueenPosition:
    def __init__(self, cardIndex, player: int):
        self.cardIndex = cardIndex
        self.player = player

    def getCardIndex(self) -> int:
        return self.cardIndex

    def getPlayerIdx(self) -> int:
        return self.player

class HandPosition:

    def __init__(self, cardidx: int, player: int):
        self.cardIdx = cardidx
        self.playeridx = player

    def __repr__(self):
        return f"{self.cardIdx} {self.playeridx}"

    def getCardidx(self) -> int:
        return self.cardIdx

    def getPlayerIdx(self) -> int:
        return self.playeridx


Position = Union[SleepingQueenPosition, AwokenQueenPosition, HandPosition]

