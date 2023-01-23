
from QueenCollection import QueenCollection
from Card_CardType import Card, Queen
from typing import List,Optional


class GameState:
    numberOfPlayers: int
    onTurn: int = 0
    sleepingQueens: QueenCollection
    AwokenQueens: List[List[Optional[Queen]]]
    cardsDiscardedLastTurn: List[Card]


class PlayerState:
    def __init__(self)->None:
        self.cards: List[Card] = []
        self.awokenQueens: List[Optional[Queen]] = []
    def __repr__(self)->str:
        return f"{self.cards} {self.awokenQueens}"
