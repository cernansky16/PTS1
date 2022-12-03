from Player import Player
from typing import List
from Piles import DrawingAndTrashPile
from QueenCollection import SleepingQueens
from GameState_PlayerState import GameState, PlayerState
from Hand import Hand

class Game:
    def __init__(self):
        self._players = []
        self.drawing_and_trash_pile = DrawingAndTrashPile()
        self._sleepingQueens = SleepingQueens()
        self._players_states: List[PlayerState] = list()

        for i in range(GameState.numberOfPlayers):
            self._players.append(Player(Hand(i,self.drawing_and_trash_pile)))
            for x in range(5):
                card = self.drawing_and_trash_pile.drawing_pile.pop()
                card.setHandPosition(x, i)
                self._players[i].hand.cards.append(card)
    def play(self):
        pass





# GameState()
# GameState.numberOfPlayers = 4
# a = Game()
# carty = list()
# for i in a._players[0].hand.cards:
#     if i.getType() == 1:
#         carty.append(i)
# print(a._players[0].evaluateNumberedCards(carty))



