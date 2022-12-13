from Position import SleepingQueenPosition,AwokenQueenPosition
from Card_CardType import Card,Queen
from typing import Optional,List


class GameState:
    numberOfPlayers: int
    onTurn: int = 0
    sleepingQueens: List[SleepingQueenPosition]
    AwokenQueens: List[AwokenQueenPosition]
    cardsDiscardedLastTurn: List[Card]


class PlayerState: # urobit
    def __init__(self, cards, awokenQueens):
        self.cards: dict[int,Optional[Card]] = cards
        self.awokenQueens: dict[int, Queen] = awokenQueens
    def __repr__(self):
        return f"{self.cards} {self.awokenQueens}"
