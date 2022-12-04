from GameState_PlayerState import PlayerState
from typing import List
from Card_CardType import Card
from Position import Position,AwokenQueenPosition,HandPosition,SleepingQueenPosition
from Hand import EvaluateAttack
from QueenCollection import QueenCollection
class Player:
    def __init__(self, hand,movequeeninstance):
        self.hand = hand
        self.awoken = QueenCollection()
        self.state = PlayerState(self.hand.cards, self.awoken)
        self.move_queen = movequeeninstance



    def __repr__(self):
        return self.hand.getIndex()

    def play(self, cards: List[Position]) -> bool:
        hand:List[HandPosition] = [pos for pos in cards if type(pos) == HandPosition]
        sleeping_queens: List[SleepingQueenPosition] = [pos for pos in cards if type(pos) == SleepingQueenPosition]
        awoken_queens: List[AwokenQueenPosition] = [pos for pos in cards if type(pos) == AwokenQueenPosition]
        if len(hand) == 1 and awoken_queens == 1 and not sleeping_queens:
            attack_card = self.hand.pickCards(hand)
            target = awoken_queens.pop()
            target_queen = target.getCardIndex()
            targetPlayer = target.getPlayer()
            self.hand.removePickedCardsAndDraw()
            a = EvaluateAttack(attack_card,target_queen,targetPlayer)
            return True
        if hand and not awoken_queens and not sleeping_queens:
            picked: List[Card] = self.hand.pickCards(cards)
            countofNumbered = 0
            for card in picked:
                if self.hand.cards[card.getType()] == 1:
                    countofNumbered += 1
            if len(picked) == countofNumbered:
                self.hand.removePickedCardsAndDraw()
                return self.evaluateNumberedCards(picked)
            elif countofNumbered != 0:
                return False
        elif len(hand) == 1 and len(sleeping_queens) == 1 and not awoken_queens:
            card: [Card] = self.hand.pickCards(hand)
            position: [Position] = sleeping_queens.pop()
            if card.getType() == 2:
                self.move_queen.play(position)
                self.awoken.add(self.move_queen.getLastMoved())
                self.hand.removePickedCardsAndDraw()
            return True
        else:
            return False

    def getPlayerState(self) -> PlayerState:
        return self.state

    def evaluateNumberedCards(self,cards: List[Card]) -> bool:
        cards = sorted(cards, key=lambda card: card.getValue())
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


