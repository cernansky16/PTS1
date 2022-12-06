from Card_CardType import Card
from random import shuffle
from typing import List

class DrawingAndTrashPile:
    def __init__(self):
        self.drawing_pile = []
        self._trash_pile = []
        for i in range(1,11):
            for j in range(4):
                self.drawing_pile.append(Card(1, i))
        for i in range(4):
            self.drawing_pile.append(Card(2, 0))
            self.drawing_pile.append(Card(2, 0))
            self.drawing_pile.append(Card(3, 0))
            self.drawing_pile.append(Card(4, 0))
        for j in range(3):
            self.drawing_pile.append(Card(5, 0))
            self.drawing_pile.append(Card(6, 0))

        shuffle(self.drawing_pile)

    def discardAndDraw(self, discard:list[Card]) -> list[Card]:
        self.discardedThisTurn = discard
        new_cards: list[Card] = list()
        for x in discard:
            x.setHandPosition(None,None)
            self._trash_pile.append(x)
            if not self.drawing_pile:
                self.reset()
            new_cards.append(self.drawing_pile.pop(0))
        return new_cards

        # second solution
        # if len(discard) > len(self.drawing_pile):
        #     self.reset()
        # for x in discard:
        #      x.setHandPosition(None, None)
        #      self.trash_pile.append(x)
        #      card = self.drawing_pile.pop(0)
        #      new_cards.append(self.drawing_pile.pop(0))

    def getCardsDiscardedThisTurn(self) -> List[Card]:
        return self.discardedThisTurn

    def reset(self) -> None:
        shuffle(self._trash_pile)
        self.drawing_pile = self._trash_pile[:]
        self._trash_pile = list()
