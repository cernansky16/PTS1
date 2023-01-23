from __future__ import annotations
from Player import Player
from typing import List, Optional,TYPE_CHECKING
from Piles import DrawingAndTrashPile, Strategy1
from GameState_PlayerState import GameState, PlayerState
from Hand import Hand, EvaluateAttack
from random import shuffle
from Card_CardType import Queen
from QueenCollection import QueenCollection, MoveQueen

if TYPE_CHECKING:
    from GameObservable_GameAdaptor import GameFinished
    from Position import Position

class Game:
    def __init__(self, numofplayers: int):
        self.players = []
        self.numofplayers = numofplayers
        self.state = GameState()
        self.drawing_and_trash_pile = DrawingAndTrashPile(Strategy1())
        kralovne = [Queen(5), Queen(5), Queen(5), Queen(5), Queen(10), Queen(10), Queen(10), Queen(10),
                    Queen(15), Queen(15), Queen(15), Queen(20)]
        shuffle(kralovne)
        self.sleeping_queens = QueenCollection(kralovne)
        self._players_states: List[PlayerState] = list()
        if self.numofplayers == 2 or self.numofplayers == 3:
            self.required_points = 50
            self.required_queens = 5
        if self.numofplayers == 4 or self.numofplayers == 5:
            self.required_points = 40
            self.required_queens = 4

        for i in range(self.numofplayers):
            hand: Hand = Hand(i, self.drawing_and_trash_pile)
            self.players.append(Player(hand, QueenCollection(), MoveQueen(self.sleeping_queens), PlayerState(),
                                       EvaluateAttack()))
            # for x in range(5):
            #     card = self.drawing_and_trash_pile.drawing_pile.pop() #asi zmenit
            #     card.setHandPosition(x, i)
            #     self.players[i].hand.cards.append(card)
            hand.draw5Cards()
            # self.players[i].hand.cards.append(card)
        for i in range(numofplayers):
            self.players[i].evaluate_attack.set_players(self.players)

    def play(self, playerIdx: int, cards: List[Position]) -> GameState:

        if self.players[playerIdx].play(cards):
            onturn = (playerIdx + 1) % self.numofplayers
            self.updateState(onturn)
        return self.state


    def updateState(self,on_turn) -> None:
        awokenqueens = list()
        for i in self._players_states:
            awokenqueens.append(i.awokenQueens)
        self.state.onTurn = on_turn
        self.state.numberOfPlayers = self.numofplayers
        self.state.sleepingQueens = self.sleeping_queens
        self.state.AwokenQueens = awokenqueens
        self.state.cardsDiscardedLastTurn = self.drawing_and_trash_pile.getCardsDiscardedThisTurn()




