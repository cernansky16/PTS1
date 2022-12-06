import unittest
from unittest.mock import Mock
from Game import  Game
from Card_CardType import Card,Queen
from QueenCollection import QueenCollection
from Position import HandPosition,SleepingQueenPosition
from Player import Player
from Piles import DrawingAndTrashPile

class TestPlayer(unittest.TestCase):

    def test_Player(self):
        hra = Mock()
        hrac0 = Player(Mock(),Mock())
        hrac0.hand.cards = [Card(1,1),Card(1,4),Card(3,0),Card(1,5),Card(6,0)]
        hrac0.hand.cards[0].setHandPosition(0, hrac0)
        hrac0.hand.cards[1].setHandPosition(1, hrac0)
        hrac0.hand.cards[2].setHandPosition(2, hrac0)
        hrac0.hand.cards[3].setHandPosition(3, hrac0)
        hrac0.hand.cards[4].setHandPosition(4, hrac0)
        #testing method evaluated numbered cards
        self.assertTrue(hrac0.evaluateNumberedCards([Card(1,1)]))
        self.assertTrue(hrac0.evaluateNumberedCards([Card(1,1),Card(1,4),Card(1,5)])) # valid equation
        self.assertTrue(hrac0.evaluateNumberedCards([Card(1,4),Card(1,4)]))
        self.assertFalse(hrac0.evaluateNumberedCards([Card(1, 4), Card(1, 2)]))

    def testGame(self):

        hra = Game(4)
        self.assertEqual(4,hra.numofplayers)
        self.assertTrue(len(hra.sleeping_queens.getQueens()),12)
        self.assertTrue(hra.required_points,40)
        self.assertTrue(hra.drawing_and_trash_pile._trash_pile == list()) # no cards in trash pile
        self.assertEqual(len(hra.drawing_and_trash_pile.drawing_pile),42) # 20 cards has been distributed
        hra.players[0].hand.cards[0] = Card(2,0)
        state = hra.play(0,[HandPosition(0,hra.players[0]),SleepingQueenPosition(9)]) #player0 has played a king to awaken a queen
        self.assertEqual(state.onTurn,1) # now is on turn player 1
        self.assertEqual(len(hra.players[0].awoken.getQueens()),1)
        hra.players[0].hand.cards[0] = Card(2, 0)

    def test_drawing_and_trash_pile(self):
        pile = DrawingAndTrashPile()
        self.assertEqual(len(pile.discardAndDraw([Card(1,1),Card(1,2)])),2) #it has returned two cards
        self.assertEqual([Card(1,1),Card(1,2)],pile.getCardsDiscardedThisTurn())
        pile = DrawingAndTrashPile()
        self.assertEqual(62, len(pile.drawing_pile))
        #just testing reset drawing pile method
        pile._trash_pile = pile.drawing_pile[:]
        pile.drawing_pile = list()
        self.assertEqual(0, len(pile.drawing_pile))
        pile.reset()
        self.assertEqual(62, len(pile.drawing_pile))

    def test_QueenCollection(self):
        colection = QueenCollection()
        colection.add(Queen(10))
        self.assertEqual(1,len(colection.getQueens()))
        colection.add(Queen(5))
        self.assertEqual(colection.removeQueen(SleepingQueenPosition(98)),None) #wrong position
        self.assertEqual(colection.removeQueen(SleepingQueenPosition(1)),Queen(5))

if __name__ == '__main__':
    unittest.main()
