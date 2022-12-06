from __future__ import annotations
from typing import Union,TYPE_CHECKING

if TYPE_CHECKING:
    from Player import Player

class SleepingQueenPosition:
    def __init__(self, cardIndex):
        self.cardIndex = cardIndex

    def getCardIndex(self) -> int:
        return self.cardIndex

class AwokenQueenPosition:
    def __init__(self, cardIndex, player):
        self.cardIndex = cardIndex
        self.player = player

    def getCardIndex(self) -> int:
        return self.cardIndex

    def getPlayer(self) -> Player:
        return self.player

class HandPosition:

    def __init__(self,card, player):
        self.cardIndex = card
        self.player = player

    def getCardIndex(self) -> int:
        return self.cardIndex

    def getPlayer(self) -> Player:
        return self.player


Position = Union[SleepingQueenPosition, AwokenQueenPosition, HandPosition]

