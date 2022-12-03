from Card_CardType import CardType,Card
from Position import Position,HandPosition
from typing import List
from GameState_PlayerState import GameState


class Hand:
    def __init__(self,idx,drawing_pile):
        self.playerIdx: int = idx
        self.drawing_and_trash_pile = drawing_pile
        self.cards: list[Card] = list()
        self.picked: list[Card] = list()

    def getIndex(self):
        return self.playerIdx

    def pickCards(self,position:List[HandPosition]):
        if not position:
            return None
        self.picked = list()
        for x in position:
            self.picked.append(self.cards.pop(x.getCardIndex()))
        return self.picked
    def removePickedCardsAndDraw(self):
        #one solution
        for x in self.picked:
            self.drawing_and_trash_pile.trash_pile.append(x)
            if not self.drawing_and_trash_pile.drawing_pile:
                self.drawing_and_trash_pile.reset()
            card = self.drawing_and_trash_pile.drawing_pile.pop(0)
            card.setHandPosition(len(self.cards),self.getIndex())
            self.cards.append(card)


        # second solution
        # if len(self.picked) > len(self.drawing_and_trash_pile.drawing_pile):
        #     self.drawing_and_trash_pile.reset()
        # for x in self.picked:
        #     self.drawing_and_trash_pile.trash_pile.append(x)
        #     card = self.drawing_and_trash_pile.drawing_pile.pop(0)
        #     card.setHandPosition(len(self.cards),self.getIndex())
        #     self.cards.append(card)
    def returnPickedCards(self):
         for i in self.picked:
             self.cards.append(i)
    def hasCardOfType(self,type:CardType):
        for i in self.cards:
            if i.getType() == type:
                return True
        return False
    def getCards(self):
        return self.cards
class EvaluateAttack:
    def __init__(self,card:[Card],playerToAttack):
        self.typeOfAttack: [Card] = card
        self.playerToAttack = playerToAttack
        if self.typeOfAttack.getType() == 3:
            self.defenseCardType = 5
        if self.typeOfAttack.getType() == 4:
            self.defenseCardType = 6

    def play(self,targetqueen:Position,targetplayeridx: int) -> bool:
        if targetplayeridx >= GameState.numberOfPlayers:
            return False






