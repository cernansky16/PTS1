from Player import Player
from Hand import Hand
from Card_CardType import Card
from QueenCollection import SleepingQueens
from random import shuffle
from GameState_PlayerState import GameState

class Game:
    def __init__(self):
        self.players = []
        self.drawing_and_trash_pile = DrawingAndTrashPile()
        self.sleepingQueens = SleepingQueens()
        for i in range(GameState.numberOfPlayers):
            cards = []
            for x in range(5):
                cards.append(self.drawing_and_trash_pile.all_cards.pop())
            self.players.append(Player(Hand(i,cards)))

class DrawingAndTrashPile:
    def __init__(self):
        self.all_cards = []
        for i in range(10):
            self.all_cards.append(Card(1, i))
        for i in range(4):
            self.all_cards.append(Card(1, 0))
            self.all_cards.append(Card(2, 0))
            self.all_cards.append(Card(3, 0))
            self.all_cards.append(Card(4, 0))
        for j in range(3):
            self.all_cards.append(Card(5, 0))
            self.all_cards.append(Card(6, 0))

        shuffle(self.all_cards)

    def discardAndDraw(self,discard:list[Card]): #-> list[Card]
        pass
    def newTurn(self):
        pass
    def getCardsDiscardedThisTurn(self):
        pass

# GameState()
# GameState.numberOfPlayers = 4
# a = Game()



