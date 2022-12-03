from Card_CardType import Card
from random import shuffle

class DrawingAndTrashPile:

    def __init__(self):
        self.drawing_pile = []
        self.trash_pile = []
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

    def discardAndDraw(self,discard:list[Card]): #-> list[Card]
        pass
    def newTurn(self):
        pass
    def getCardsDiscardedThisTurn(self):
        pass
    def reset(self):
        shuffle(self.trash_pile)
        self.drawing_pile = self.trash_pile[:]
        self.trash_pile = list()
