from __future__ import annotations
from typing import Union, TYPE_CHECKING

if TYPE_CHECKING:
    from Player import Player
from Card_CardType import CardType,Card
from Position import Position,HandPosition,AwokenQueenPosition
from typing import List,Optional
from GameState_PlayerState import GameState


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
        self.picked = list()
        for x in position:
            self.picked.append(self.cards.pop(x.getCardIndex()))
        return self.picked

    def removePickedCardsAndDraw(self):
        new_cards: List[Card] = self.drawing_and_trash_pile.discardAndDraw(self.picked)
        for i in new_cards:
            i.setHandPosition(len(self.cards), self.getIndex())
            self.cards.append(i)

    def returnPickedCards(self):
         for i in self.picked:
             self.cards.append(i)
         self.picked = list()

    def hasCardOfType(self, type: CardType) -> bool:
        for i in self.cards:
            if i.getType() == type:
                return True
        return False

    def getCards(self) -> List[Card]:
        return self.cards

class EvaluateAttack:
    def __init__(self,card:[Card],attacker: HandPosition, victim: AwokenQueenPosition):
        self.typeOfAttack: [Card] = card
        self.targetQueen = victim
        self.victim: Player = victim.getPlayer()
        self.attacker: Player = attacker.getPlayer()
        if self.typeOfAttack.getType() == 3:
            self.defenseCardType = CardType.Dragon
        if self.typeOfAttack.getType() == 4:
            self.defenseCardType = CardType.MagicWand

    def play(self, targetqueen: Position, targetplayeridx: int) -> bool:
        if targetplayeridx >= GameState.numberOfPlayers:
            return False
        if self.victim.hand.hasCardOfType(self.defenseCardType):
            for x in self.victim.hand.getCards():
                card: Card = x
                if card.getType() == self.defenseCardType:
                    pos = card.getHandPosition()

            self.victim.hand.pickCards(pos)
            return True
        else:
            queen = self.victim.awoken.removeQueen(targetqueen)
            if queen == None:
                return False
            self.attacker.awoken.add(queen)
            return True






