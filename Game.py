from Player import Player
from typing import List,Optional
from Piles import DrawingAndTrashPile
from GameState_PlayerState import GameState, PlayerState
from Hand import Hand
from random import shuffle
from Position import Position
from Card_CardType import Queen
from QueenCollection import QueenCollection,MoveQueen

class Game:
    def __init__(self):
        self.players = []
        self.numofplayers = GameState.numberOfPlayers
        self.drawing_and_trash_pile = DrawingAndTrashPile()
        self.sleeping_queens = QueenCollection(shuffle([Queen(5), Queen(5), Queen(5), Queen(5), Queen(10), Queen(10), Queen(10), Queen(10),
                  Queen(15), Queen(15), Queen(15), Queen(20)]))
        self._players_states: List[PlayerState] = list()

        for i in range(GameState.numberOfPlayers):
            self.players.append(Player(Hand(i, self.drawing_and_trash_pile), MoveQueen(self.sleeping_queens)))
            for x in range(5):
                card = self.drawing_and_trash_pile.drawing_pile.pop()
                card.setHandPosition(x, i)
                self.players[i].hand.cards.append(card)

    def play(self,playerIdx: int, cards: List[Position]) -> Optional[GameState]:
        if self.players[playerIdx].play(cards):
            onturn = (playerIdx + 1) % self.numofplayers
            awokenqueens = list()
            for i in self._players_states:
                awokenqueens.append(i.awokenQueens)
            state = GameState()
            state.onTurn = onturn
            state.numberOfPlayers = self.numofplayers
            state.sleepingQueens = self.sleeping_queens
            state.AwokenQueens = awokenqueens
            state.cardsDiscardedLastTurn = self.drawing_and_trash_pile.getCardsDiscardedThisTurn()
            return state
        else:
            return None




GameState()
GameState.numberOfPlayers = 4
a = Game()
print(a.players[0].hand.cards)


