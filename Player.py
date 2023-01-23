from __future__ import annotations
from typing import List, Optional, Union,TYPE_CHECKING
from Card_CardType import Card, CardType, Queen
from Position import Position, AwokenQueenPosition, HandPosition, SleepingQueenPosition

if TYPE_CHECKING:
    from Hand import EvaluateAttackInterface, HandInterface

    from GameState_PlayerState import PlayerState
    from QueenCollection import QueenCollectionInterface, MoveQueenInterface


class Player:
    def __init__(self, hand: HandInterface, queenCollection: QueenCollectionInterface, movequeeninstance: MoveQueenInterface,
                 playerState: PlayerState, evaluateAttack: EvaluateAttackInterface):
        self.hand: HandInterface = hand
        self.awoken: QueenCollectionInterface = queenCollection
        self.state: PlayerState = playerState
        self.move_queen: MoveQueenInterface = movequeeninstance
        self.evaluate_attack: EvaluateAttackInterface = evaluateAttack

    def __repr__(self):
        return self.hand.getIndex()

    def play(self, cards: List[Position]) -> bool:
        hand_pos: List[HandPosition] = [pos for pos in cards if isinstance(pos,HandPosition)]
        sleeping_queens: List[SleepingQueenPosition] = [pos for pos in cards if isinstance(pos,SleepingQueenPosition)]
        awoken_queens: List[AwokenQueenPosition] = [pos for pos in cards if isinstance(pos,AwokenQueenPosition)]
        if len(hand_pos) == 1 and len(awoken_queens) == 1 and not sleeping_queens:
            card = hand_pos[0].getCardidx()
            allcards = self.hand.getCards()
            if allcards[card].getType() == CardType.Knight or allcards[card].getType() == CardType.Potion:
                attack_card = self.hand.pickCards(hand_pos)
                self.hand.removePickedCardsAndDraw(attack_card)
                self.evaluate_attack.play(attack_card[0], hand_pos[0], awoken_queens[0])
                self.update_state()
                return True
            else:
                return False
        elif hand_pos and not awoken_queens and not sleeping_queens:
            picked: List[Card] = self.hand.pickCards(hand_pos)
            countofNumbered = 0
            for one in picked:
                if one.getType() == CardType.Number:
                    countofNumbered += 1
            if len(picked) == countofNumbered or len(picked) == 1:
                self.hand.removePickedCardsAndDraw(picked)
                self.update_state()
                return self.evaluateNumberedCards(picked)
            elif countofNumbered != 0:
                self.hand.returnPickedCards(picked)
                return False
        elif len(hand_pos) == 1 and len(sleeping_queens) == 1 and not awoken_queens:
            card0: List[Card] = self.hand.pickCards(hand_pos)
            position: SleepingQueenPosition = sleeping_queens.pop()
            if card0[0].getType() == CardType.King:
                self.move_queen.play(position)
                self.awoken.addAwoken(self.move_queen.getLastMoved())
                self.hand.removePickedCardsAndDraw(card0)
                self.update_state()
                return True
            else:
                self.hand.returnPickedCards(card0)
                return False

        return False

    def getPlayerState(self) -> PlayerState:
        return self.state

    def update_state(self) -> None:
        self.state.awokenQueens = self.awoken.getQueens()
        self.state.cards = self.hand.getCards()

    def removeAwoken(self, position: AwokenQueenPosition) -> Optional[Queen]:
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


