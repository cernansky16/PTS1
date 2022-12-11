from Player import Player
from typing import List, Optional
from Piles import DrawingAndTrashPile
from GameState_PlayerState import GameState, PlayerState
from Hand import Hand
from random import shuffle
from Position import Position
from Card_CardType import Queen
from QueenCollection import QueenCollection, MoveQueen


class Game:
    def __init__(self, numofplayers):
        self.players = []
        self.numofplayers = numofplayers
        self.state = GameState()
        self.drawing_and_trash_pile = DrawingAndTrashPile()
        kralovne = [Queen(5), Queen(5), Queen(5), Queen(5), Queen(10), Queen(10), Queen(10), Queen(10),
                    Queen(15), Queen(15), Queen(15), Queen(20)]
        shuffle(kralovne)
        self.sleeping_queens = QueenCollection(kralovne)
        self._players_states: List[PlayerState] = list()
        if self.numofplayers == 2 or self.numofplayers == 3:
            self.required_points = 50
        if self.numofplayers == 4 or self.numofplayers == 5:
            self.required_points = 40

        for i in range(self.numofplayers):
            hand: Hand = Hand(i, self.drawing_and_trash_pile)
            self.players.append(Player(hand, MoveQueen(self.sleeping_queens)))
            for x in range(5):
                card = self.drawing_and_trash_pile.drawing_pile.pop()
                card.setHandPosition(x, i)
                self.players[i].hand.cards.append(card)

    def play(self, playerIdx: int, cards: List[Position]) -> Optional[GameState]:

        if self.players[playerIdx].play(cards):
            onturn = (playerIdx + 1) % self.numofplayers
            self.updateState(onturn)
            return self.state
        return None

    def updateState(self,on_turn) -> None:
        awokenqueens = list()
        for i in self._players_states:
            awokenqueens.append(i.awokenQueens)
        self.state.onTurn = on_turn
        self.state.numberOfPlayers = self.numofplayers
        self.state.sleepingQueens = self.sleeping_queens
        self.state.AwokenQueens = awokenqueens
        self.state.cardsDiscardedLastTurn = self.drawing_and_trash_pile.getCardsDiscardedThisTurn()


