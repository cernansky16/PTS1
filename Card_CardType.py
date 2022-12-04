import enum
from Position import Position,HandPosition
from dataclasses import dataclass

@dataclass
class CardType(enum.Enum):
    Number = 1
    King = 2
    Knight = 3
    SleepingPotion = 4
    Dragon = 5
    MagicWand = 6

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

    def __init__(self,type,value):
        self.type: CardType = type
        self.value: int = value

    def __repr__(self):
        return f"{self.type} {self.value}"

    def setHandPosition(self,card0, player0) -> None:
        self.handPosition = HandPosition(card0, player0)

    def getHandPosition(self) -> Position:
        return self.handPosition

    def getValue(self) -> int:
        return self.value

    def getType(self) -> CardType:
        return self.type

