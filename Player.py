from GameState_PlayerState import PlayerState
from typing import List,Optional
from Card_CardType import Card,CardType,Queen
from Position import Position,AwokenQueenPosition,HandPosition,SleepingQueenPosition
from Hand import EvaluateAttack,Hand
from QueenCollection import QueenCollection,MoveQueen

class Player:
    def __init__(self, hand, movequeeninstance):
        self.hand: Hand = hand
        self.awoken: QueenCollection = QueenCollection()
        self.state: PlayerState = PlayerState(self.hand.cards, self.awoken)
        self.move_queen: MoveQueen = movequeeninstance

    def __repr__(self):
        return self.hand.getIndex()

    def play(self, cards: List[Position]) -> bool:
        hand_pos:List[HandPosition] = [pos for pos in cards if isinstance(pos,HandPosition)]
        sleeping_queens: List[SleepingQueenPosition] = [pos for pos in cards if isinstance(pos,SleepingQueenPosition)]
        awoken_queens: List[AwokenQueenPosition] = [pos for pos in cards if isinstance(pos,AwokenQueenPosition)]
        if len(hand_pos) == 1 and len(awoken_queens) == 1 and not sleeping_queens:
            index = hand_pos[0].getCardIndex()
            cards = self.hand.getCards()
            if cards[index].getType() == CardType.Knight or cards[index].getType() == CardType.Potion:
                attack_card = self.hand.pickCards(hand_pos)
                self.hand.removePickedCardsAndDraw(attack_card)
                a = EvaluateAttack(attack_card[0],hand_pos[0],awoken_queens[0])
                a.play()
                self.update_state()
                return True
            else:
                return False
        if hand_pos and not awoken_queens and not sleeping_queens:
            picked: List[Card] = self.hand.pickCards(hand_pos)
            countofNumbered = 0
            for card in picked:
                if card.getType() == CardType.Number:
                    countofNumbered += 1
            if len(picked) == countofNumbered or len(picked) == 1:
                self.hand.removePickedCardsAndDraw(picked)
                self.update_state()
                return self.evaluateNumberedCards(picked)
            elif countofNumbered != 0:
                self.hand.returnPickedCards(picked)
                return False
        elif len(hand_pos) == 1 and len(sleeping_queens) == 1 and not awoken_queens:
            card: [Card] = self.hand.pickCards(hand_pos)
            position: [Position] = sleeping_queens.pop()
            if card[0].getType() == CardType.King:
                self.move_queen.play(position)
                self.awoken.addAwoken(self.move_queen.getLastMoved())
                self.hand.removePickedCardsAndDraw(card)
                self.update_state()
                return True
            else:
                self.hand.returnPickedCards(card)
                return False
        else:
            return False

    def getPlayerState(self) -> PlayerState:
        return self.state

    def update_state(self) -> None:
        self.state.awokenQueens = self.awoken
        self.state.cards = self.hand.getCards()

    def removeAwoken(self, position: Position) -> Optional[Queen]:
        return self.awoken.removeAwokenQueen(position)

    def addAwoken(self, queen: Queen) -> None:
        self.awoken.addAwoken(queen)

    def evaluateNumberedCards(self,cards: List[Card]) -> bool:
        cards = sorted(cards, key=lambda card: card.getValue())
        if not cards:
            return False
        for i in cards:
            if i.getType() != CardType.Number:
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
            for x in cards[:length-1]:
                left_side_of_equation += x.getValue()
            if left_side_of_equation == cards[-1].getValue():
                return True
            else:
                return False


