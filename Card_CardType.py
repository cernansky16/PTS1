import enum
from Position import HandPosition
from dataclasses import dataclass

CardType = enum.Enum("CardType", ["Number", "King", "Knight", "Potion", "Dragon", "Wand"])

@dataclass
class Queen:
    def __init__(self,points):
        self.points = points

    def __repr__(self):
        return f"{self.points}"

    def getPoints(self) -> int:
        return self.points

@dataclass
class Card:

    def __init__(self, type, value)->None:
        self.type: CardType = type
        self.value: int = value
        self._handPosition = HandPosition(-1, -1)

    def __repr__(self)->str:
        return f"{self.type} {self.value}"

    def setHandPosition(self, card0, player0) -> None:
         self._handPosition = HandPosition(card0, player0)

    def getHandPosition(self) -> HandPosition:
         return self._handPosition

    def getValue(self) -> int:
        return self.value

    def getType(self) -> CardType:
        return self.type

