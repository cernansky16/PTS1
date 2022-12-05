from __future__ import annotations
from typing import TYPE_CHECKING

from Card_CardType import Card,Queen
from Position import HandPosition,AwokenQueenPosition
from typing import List,Optional

class Hand:
    def __init__(self,idx,drawing_pile):
        self.playerIdx: int = idx
        self.drawing_and_trash_pile = drawing_pile
        self.cards: List[Card] = list()
        self.picked: List[Card] = list()

    def getIndex(self) ->int :
        return self.playerIdx

    def pickCards(self, position: List[HandPosition]) -> Optional[List[Card]]:
        if not position:
            return None
        picked : List[Card] = []
        for x in position:
            if x.getCardIndex() > 5:
                return None
            picked.append(self.cards[x.getCardIndex()])
        i = 0 # i is to assure that the card is poped at the right positions
        for x in position:
            self.cards.pop(x.getCardIndex()-i)
            i += 1
        return picked

    def removePickedCardsAndDraw(self,picked) -> None:
        new_cards: List[Card] = self.drawing_and_trash_pile.discardAndDraw(picked)
        for i in new_cards:
            i.setHandPosition(len(self.cards), self.getIndex())
            self.cards.append(i)
    def IndexOfCardOfType(self,type) -> int:
        idx = 0
        for card in self.cards:
            if card.type == type:
                return idx
            idx += 1
        return -1

    # def returnPickedCards(self) -> None:
    #      for i in self.picked:
    #          self.cards.append(i)
    #      self.picked = list()

    def hasCardOfType(self, type: int) -> bool:
        for i in self.cards:
            if i.getType() == type:
                return True
        return False

    def getCards(self) -> List[Card]:
        return self.cards

class EvaluateAttack:
    def __init__(self,card:Card,attacker: HandPosition, victim: AwokenQueenPosition):
        self.typeOfAttack: [Card] = card
        self.targetQueen = victim
        self.victim = victim.getPlayer()
        self.attacker = attacker.getPlayer()
        if self.typeOfAttack.getType() == 3:
            self.defenseCardType = 5
        elif self.typeOfAttack.getType() == 4:
            self.defenseCardType = 6

    def play(self) -> bool:
        if self.victim.hand.hasCardOfType(self.defenseCardType):
            idx = self.victim.hand.IndexOfCardOfType(self.defenseCardType)
            pos = self.victim.hand.cards[idx].getHandPosition()
            picked = self.victim.hand.pickCards([pos])
            self.victim.hand.removePickedCardsAndDraw(picked)
            return True
        else:
            if self.typeOfAttack.getType() == 3:
                queen: Queen = self.victim.awoken.removeQueen(self.targetQueen)
                print(queen)
                self.victim.update_state()
                self.attacker.awoken.add(queen)
                return True
            elif self.typeOfAttack.getType() == 4:
                queen = self.victim.awoken.removeQueen(self.targetQueen)
                self.victim.update_state()
                self.victim.move_queen.sleeping_queens.add(queen)
                return True







