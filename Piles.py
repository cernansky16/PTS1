from Card_CardType import Card, CardType
from random import shuffle
from typing import List


class StrategyInterface:
    @staticmethod
    def not_enough_cards(cards_to_discard: List[Card], draw_pile: List[Card], trash_pile:List[Card]) -> List[Card]:
        return []


class Strategy2(StrategyInterface):
    @staticmethod
    def not_enough_cards(cards_to_discard: List[Card], draw_pile: List[Card], trash_pile: List[Card]) -> List[Card]:

        shuffle(trash_pile)
        draw_pile = trash_pile[:]
        trash_pile = list()
        trash_pile.extend(cards_to_discard)
        draw = draw_pile[:len(cards_to_discard)]
        draw_pile = draw_pile[len(cards_to_discard):]
        return draw


class Strategy1(StrategyInterface):
    @staticmethod
    def not_enough_cards(cards_to_discard: List[Card], draw_pile: List[Card], trash_pile: List[Card]) -> List[Card]:
        in_draw_pile = len(draw_pile)
        trash_pile.extend(cards_to_discard)
        to_draw = draw_pile[:len(cards_to_discard)]
        draw_pile = draw_pile[:len(cards_to_discard)]
        shuffle(trash_pile)
        draw_pile = trash_pile[:]
        trash_pile = list()
        to_draw.extend(draw_pile[:len(cards_to_discard)-in_draw_pile])
        draw_pile = draw_pile[len(cards_to_discard)-in_draw_pile:]
        return to_draw


class DrawingAndTrashPile:
    def __init__(self, strategy: Strategy1):
        self.strategy: Strategy1 = strategy
        self.drawing_pile: List[Card] = []
        self.trash_pile: List[Card] = []
        for i in range(1, 11):
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

    def draw5(self, idx)-> List[Card]:
        to_return = list()
        for x in range(5):
            card = self.drawing_pile.pop()  # asi zmenit
            to_return.append(card)
        return to_return

    def discardAndDraw(self, discard: list[Card]) -> list[Card]:

        self.discardedThisTurn = discard
        new_cards: list[Card] = list()

        if len(discard) >= len(self.drawing_pile):
            for card in discard:
                card.setHandPosition(-1, -1)

            return self.strategy.not_enough_cards(discard, self.drawing_pile, self.trash_pile)
        for x in discard:
            x.setHandPosition(-1, -1)
            self.trash_pile.append(x)

            new_cards.append(self.drawing_pile.pop(0))
        return new_cards

    def getCardsDiscardedThisTurn(self) -> List[Card]:
        return self.discardedThisTurn


