import enum

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
    def getPoints(self):
        return self.points
class Card:
    type: CardType
    value: int
