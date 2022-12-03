import enum
from Position import HandPosition

class CardType(enum.Enum):
    Number = 1
    King = 2
    Knight = 3
    SleepingPotion = 4
    Dragon = 5
    MagicWand = 6

class Queen:
    def __init__(self,points):
        self.points = points
    def __repr__(self):
        return self.points
    def getPoints(self):
        return self.points



class Card:
    def __init__(self,type,value):
        self.type: CardType = type
        self.value: int = value
    def __repr__(self):
        return f"{self.type} {self.value}"
    def setHandPosition(self,card0, player0):
        self.handPosition = HandPosition(card0, player0)
    def getValue(self):
        return self.value
    def getType(self):
        return self.type


