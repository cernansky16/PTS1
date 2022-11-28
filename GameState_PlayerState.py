from Position import HandPosition,SleepingQueenPosition,AwokenQueenPosition
from Card_CardType import Card,Queen
from typing import Optional

class GameState:
    numberOfPlayers: int
    onTurn: int
    sleepingQueens: set[SleepingQueenPosition]
    cards: dict[HandPosition, Optional[Card]]
    AwokenQueens: dict[AwokenQueenPosition]
    cardsDiscardedLastTurn: list[Card]
class PlayerState:
    def __init__(self,cards,awokenQueens):
        self.cards: dict[int,Optional[Card]] = cards
        self.awokenQueens:dict[int,Queen] = awokenQueens
    def __repr__(self):
        return f"{self.cards} {self.awokenQueens}"
