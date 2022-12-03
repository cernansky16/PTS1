from QueenCollection import AwokenQueens
from GameState_PlayerState import PlayerState
from typing import List
from Card_CardType import Card
from Position import Position
from Hand import EvaluateAttack
class Player:
    def __init__(self, hand):
        self.hand = hand
        self.state = PlayerState(self.hand.cards,AwokenQueens())

    def __repr__(self):
        return self.hand.getIndex()

    def play(self, cards: List[Position]):
        picked: List[Card] = self.hand.pickCards(cards)
        if len(picked) == 1:
            card: [Card] = picked.pop()
            if card.getType() == 1:
                self.evaluateNumberedCards(picked)
            if card.getType() == 2:
                #zobud kralovnu
                pass
            elif card.getType() == 3:
                attack = EvaluateAttack(card)#indexofplayer)

            elif card.getType() == 4:
                attack = EvaluateAttack(card)#,indexofplayer)


        else:
            for card in picked:
                if card.getType() != 1:
                    return
            else:
                self.evaluateNumberedCards(picked)
        self.hand.removePickedCardsAndDraw(picked)

    def getPlayerState(self):
        return self.state

    def evaluateNumberedCards(self,cards: List[Card]):
        cards = sorted(cards,key=lambda card: card.getValue())
        print(cards)
        if not cards:
            return False
        for i in cards:
            if i.getType() != 1:
                return False
        length = len(cards)
        if length == 1:
            return True
        elif length == 2:
            if cards[0].getValue() == cards[1].getValue():
                return True
            return False
        else:
            left_side_of_equation = 0
            for x in cards[:length-2]:
                left_side_of_equation += x.getValue()
            if left_side_of_equation == cards[-1].getValue():
                return True
            else:
                return False

class MoveQueen:
    pass
