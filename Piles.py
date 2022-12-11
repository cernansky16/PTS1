from Card_CardType import Card,CardType
from random import shuffle
from typing import List

class DrawingAndTrashPile:
    def __init__(self):
        self.drawing_pile = []
        self._trash_pile = []
        for i in range(1,11):
            for j in range(4):
                self.drawing_pile.append(Card(CardType.Number, i))
        for i in range(4):
            self.drawing_pile.append(Card(CardType.King, 0))
            self.drawing_pile.append(Card(CardType.King, 0))
            self.drawing_pile.append(Card(CardType.Knight, 0))
            self.drawing_pile.append(Card(CardType.Potion, 0))
        for j in range(3):
            self.drawing_pile.append(Card(CardType.Dragon, 0))
            self.drawing_pile.append(Card(CardType.Wand, 0))

        shuffle(self.drawing_pile)

    def discardAndDraw(self, discard:list[Card]) -> list[Card]:
        # second solution
        # if len(discard) > len(self.drawing_pile):
        #     self.reset()
        self.discardedThisTurn = discard
        new_cards: list[Card] = list()
        for x in discard:
            x.setHandPosition(None,None)
            self._trash_pile.append(x)
            if not self.drawing_pile:
                self.reset()
            new_cards.append(self.drawing_pile.pop(0))
        return new_cards

    def reset(self) -> None:
        shuffle(self._trash_pile)
        self.drawing_pile = self._trash_pile[:]
        self._trash_pile = list()

    def getCardsDiscardedThisTurn(self) -> List[Card]:
        return self.discardedThisTurn


