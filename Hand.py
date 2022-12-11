from __future__ import annotations
from Card_CardType import Card,Queen,CardType
from Position import HandPosition,AwokenQueenPosition
from typing import List,Optional,TYPE_CHECKING

if TYPE_CHECKING:
    from Piles import DrawingAndTrashPile

class Hand:
    def __init__(self,idx: int,drawing_pile: DrawingAndTrashPile):
        self.playerIdx: int = idx
        self.drawing_and_trash_pile = drawing_pile
        self.cards: List[Card] = list()
        self.picked: List[Card] = list()

    def getIndex(self) -> int:
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
            self.cards.append(i)
        i = 0
        player = self.cards[0].getHandPosition().player
        for x in self.cards:
            x.setHandPosition(i, player)
            i += 1

    def positionOfCardOfType(self, type) -> Optional[HandPosition]:
        idx = 0
        for card in self.cards:
            if card.type == type:
                return card.getHandPosition()
            idx += 1
        return None

    def returnPickedCards(self,picked) -> None:
          for i in picked:
              self.cards.append(i)
          i = 0
          player = self.cards[0].getHandPosition().player
          for x in self.cards:
              x.setHandPosition(i, player)
              i += 1

    def hasCardOfType(self, type: int) -> bool:
        for i in self.cards:
            if i.getType() == type:
                return True
        return False

    def getCards(self) -> List[Card]:
        return self.cards

class EvaluateAttack:
    def __init__(self, card: Card, attacker: HandPosition, victim: AwokenQueenPosition):
        self.typeOfAttack: [Card] = card
        self.targetQueen = victim
        self.victim = victim.getPlayer()
        self.victim_hand = victim.getPlayer().hand
        self.attacker = attacker.getPlayer()
        if self.typeOfAttack.getType() == CardType.Knight:
            self.defenseCardType = CardType.Dragon
        elif self.typeOfAttack.getType() == CardType.Potion:
            self.defenseCardType = CardType.Wand

    def play(self) -> bool:
        if self.victim_hand.hasCardOfType(self.defenseCardType):
            pos = self.victim_hand.positionOfCardOfType(self.defenseCardType)
            picked = self.victim_hand.pickCards([pos])
            self.victim_hand.removePickedCardsAndDraw(picked)
            return True
        else:
            if self.typeOfAttack.getType() == CardType.Knight:
                queen: Queen = self.victim.removeAwoken(self.targetQueen)
                self.victim.update_state()
                self.attacker.addAwoken(queen)
                return True
            elif self.typeOfAttack.getType() == CardType.Potion:
                queen = self.victim.removeAwoken(self.targetQueen)
                self.victim.update_state()
                self.victim.move_queen.add(queen)
                return True







