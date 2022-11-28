from Card_CardType import CardType
from Position import  Position
from Card_CardType import Card
class Hand:
    def __init__(self,idx,cards):
        self.playerIdx: int = idx
        self.cards: list[Card] = cards
    def getIndex(self):
        return f"{self.playerIdx}"

    def pickCards(self):
        pass
    def removePickedCardsAndDraw(self):
        pass
    def returnPickedCards(self):
        pass
    def hasCardOfType(self,type:CardType):
        for i in self.cards:
            if i.type == type:
                return True
        return False
    def getCards(self):
        return self.cards
class EvaluateAttack:
    defenseCardType: CardType
    def play(self,targetqueen:Position,targetplayeridx: int): bool




