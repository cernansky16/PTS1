from __future__ import annotations
from typing import List, Optional, TYPE_CHECKING
from Card_CardType import Card, Queen, CardType
if TYPE_CHECKING:
    from Piles import DrawingAndTrashPile
    from Player import Player
    from Position import HandPosition, AwokenQueenPosition



class HandInterface:

    def getIndex(self) -> int:
        return 0

    def pickCards(self, position: List[HandPosition]) -> List[Card]:
        return []

    def draw5Cards(self) -> None:
        pass

    def setCards(self,  list0: List[Card],n: int)->None:
        pass

    def removePickedCardsAndDraw(self, picked: List[Card]) -> None:
        pass

    def positionOfCardOfType(self, type: CardType) -> Optional[HandPosition]:
        pass

    def returnPickedCards(self, picked: List[Card]) -> None:
        pass

    def setPositions(self)->None:
        pass

    def hasCardOfType(self, type: CardType) -> bool:
        return False

    def getCards(self) -> List[Card]:
        return []


class Hand(HandInterface):

    def __init__(self, idx: int, drawing_pile: DrawingAndTrashPile):
        self.playerIdx: int = idx
        self.drawing_and_trash_pile: DrawingAndTrashPile = drawing_pile
        self.cards: List[Card] = list()
        self.picked: List[Card] = list()

    def getIndex(self) -> int:
        return self.playerIdx

    def setCards(self, list0: List[Card], n: int = 5) -> None:
        if n != 5:
            self.cards[n] = list0.pop()
            self.cards[n].setHandPosition(n, self.playerIdx)
            return
        self.cards = list0
        self.setPositions()


    def draw5Cards(self) -> None:
        self.cards = self.drawing_and_trash_pile.draw5(self.playerIdx)
        self.setPositions()

    def setPositions(self) -> None:
        i = 0
        for card in self.cards:
            card.setHandPosition(i, self.playerIdx)
            i += 1

    def pickCards(self, position: List[HandPosition]) -> List[Card]:
        if not position:
            return []
        picked: List[Card] = []
        for x in position:
            if x.getCardidx() > 5:
                 return []
            picked.append(self.cards[x.getCardidx()])
        i = 0 # i is to assure that the card is poped at the right positions
        for x in position:
            self.cards.pop(x.getCardidx()-i)
            i += 1
        return picked

    def removePickedCardsAndDraw(self, picked: List[Card]) -> None:
        new_cards: List[Card] = self.drawing_and_trash_pile.discardAndDraw(picked)
        for i in new_cards:
            self.cards.append(i)
        counter = 0
        player = self.cards[0].getHandPosition().getPlayerIdx()
        for x in self.cards:
            x.setHandPosition(counter, player)
            counter += 1

    def positionOfCardOfType(self, type: CardType) -> Optional[HandPosition]:
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
          player = self.cards[0].getHandPosition().getPlayerIdx()
          for x in self.cards:
              x.setHandPosition(i, player)
              i += 1

    def hasCardOfType(self, type: CardType) -> bool:
        for i in self.cards:
            if i.getType() == type:
                return True
        return False

    def getCards(self) -> List[Card]:
        return self.cards


class EvaluateAttackInterface:
    def set_players(self, players: List[Player]) -> None:
        pass

    def play(self, card: Card, attacker: HandPosition, victim: AwokenQueenPosition) -> bool:
        return False


class EvaluateAttack(EvaluateAttackInterface):
    def set_players(self, players: List[Player]) -> None:
        self.players: List[Player] = players

    def play(self, card: Card, attacker0: HandPosition, victim0: AwokenQueenPosition) -> bool:
        typeOfAttack: Card = card
        targetQueen = victim0
        attacker = self.players[attacker0.getPlayerIdx()]
        victim = self.players[victim0.getPlayerIdx()]
        victim_hand = victim.hand
        if victim == attacker:
            return False
        if typeOfAttack.getType() == CardType.Knight:
            defenseCardType = CardType.Dragon
        elif typeOfAttack.getType() == CardType.Potion:
            defenseCardType = CardType.Wand
        else:
            return False
        if victim_hand.hasCardOfType(defenseCardType):
            pos = victim_hand.positionOfCardOfType(defenseCardType)
            if pos is None:
                return False
            picked = victim_hand.pickCards([pos])
            victim_hand.removePickedCardsAndDraw(picked)
            return True
        else:
            queen: Optional[Queen] = victim.removeAwoken(targetQueen)
            if typeOfAttack.getType() == CardType.Knight:

                if queen is None:
                    return False
                victim.update_state()
                attacker.addAwoken(queen)
                return True
            elif typeOfAttack.getType() == CardType.Potion:
                if queen is None:
                    return False
                victim.update_state()
                victim.move_queen.add(queen)
                return True
            else:
                return False







