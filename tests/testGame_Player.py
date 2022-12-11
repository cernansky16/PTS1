import unittest
from unittest.mock import Mock,MagicMock
from Game import Game
from Card_CardType import Card,Queen,CardType
from QueenCollection import QueenCollection,MoveQueen
from Position import HandPosition,SleepingQueenPosition
from Player import Player
from Piles import DrawingAndTrashPile

class TestPlayer(unittest.TestCase):

    def test_Player_solitary(self):
        self.hra = Mock()
        self.hrac0 = Player(Mock(),Mock())
        self.hra.drawing_and_trash_pile = Mock()
        self.hrac0.hand.removePickedCardsAndDraw = MagicMock(return_value =[Card(CardType.Number,7)])
        self.hrac0.hand.cards = [Card(CardType.Number, 1), Card(CardType.Number, 4),Card(CardType.Knight ,0),
                                 Card(CardType.Number,5), Card(CardType.Wand,0)]
        self.hrac0.hand.cards[0].setHandPosition(0, self.hrac0)
        self.hrac0.hand.cards[1].setHandPosition(1, self.hrac0)
        self.hrac0.hand.cards[2].setHandPosition(2, self.hrac0)
        self.hrac0.hand.cards[3].setHandPosition(3, self.hrac0)
        self.hrac0.hand.cards[4].setHandPosition(4, self.hrac0)
        #testing method evaluated numbered cards
        self.assertTrue(self.hrac0.evaluateNumberedCards([Card(CardType.Number,1)]))
        self.assertTrue(self.hrac0.evaluateNumberedCards([Card(CardType.Number,1),Card(CardType.Number, 4), Card(CardType.Number ,5)])) # valid equation
        self.assertTrue(self.hrac0.evaluateNumberedCards([Card(CardType.Number, 4), Card(CardType.Number, 4)]))
        self.assertFalse(self.hrac0.evaluateNumberedCards([Card(CardType.Number, 4), Card(CardType.Number, 2)]))
        self.hrac0.hand.pickCards = MagicMock(return_value =[Card(CardType.Number,7)])
        self.assertTrue(self.hrac0.play([HandPosition(0, self.hrac0)]))

    def testGame(self):

        hra = Game(4)
        self.assertEqual(4,hra.numofplayers)
        self.assertTrue(len(hra.sleeping_queens.getQueens()),12)
        self.assertTrue(hra.required_points,40)
        self.assertTrue(hra.drawing_and_trash_pile._trash_pile == list()) # no cards in trash pile
        self.assertEqual(len(hra.drawing_and_trash_pile.drawing_pile),42) # 20 cards has been distributed
        hra.players[0].hand.cards[0] = Card(CardType.King, 0)
        state = hra.play(0,[HandPosition(0,hra.players[0]),SleepingQueenPosition(9)]) #player0 has played a king to awaken a queen
        self.assertEqual(state.onTurn,1) # now is on turn player 1
        self.assertEqual(len(hra.players[0].awoken.getQueens()),1)
        self.assertIsNone(hra.sleeping_queens.collection[9])

    def test_drawing_and_trash_pile(self):
        pile = DrawingAndTrashPile()
        self.assertEqual(len(pile.discardAndDraw([Card(CardType.Number,1),Card(CardType.Number,2)])),2) #it has returned two cards
        self.assertEqual([Card(CardType.Number, 1), Card(CardType.Number, 2)], pile.getCardsDiscardedThisTurn())
        pile = DrawingAndTrashPile()
        self.assertEqual(62, len(pile.drawing_pile))
        self.assertEqual(0, len(pile._trash_pile))
        #just testing reset drawing pile method
        pile._trash_pile = pile.drawing_pile[:]
        pile.drawing_pile = list()
        self.assertEqual(0, len(pile.drawing_pile))
        pile.reset()
        self.assertEqual(62, len(pile.drawing_pile))

    def test_QueenCollection(self):
        colection = QueenCollection()
        colection.addAwoken(Queen(10))
        self.assertEqual(1,len(colection.getQueens()))
        colection.addAwoken(Queen(5))
        self.assertIsNone(colection.removeAwokenQueen(SleepingQueenPosition(98))) #wrong position
        self.assertEqual(colection.removeAwokenQueen(SleepingQueenPosition(1)),Queen(5))
        self.assertEqual(colection.removeAwokenQueen(SleepingQueenPosition(0)), Queen(10))
        self.assertEqual(colection.getQueens(), [])
        self.assertIsNone(colection.removeAwokenQueen(SleepingQueenPosition(98)))

    def testQueen(self):
        queen = Queen(20)
        self.assertEqual(20,queen.getPoints())
    def testCard_CardType(self):
        card = Card(CardType.Wand, 0)
        self.assertEqual(CardType.Wand, card.getType())
        self.assertEqual(0, card.getValue())
        card.setHandPosition(0,Mock())
        self.assertIsInstance(card.getHandPosition(),HandPosition)
        card2 = Card(CardType.Number, 10)
        self.assertEqual(card2.getValue(), 10)
        card2.setHandPosition(2, Mock())
        self.assertTrue(card2.getHandPosition().cardIndex == 2)
    def test_MoveQueen(self):
        kralovne = QueenCollection([Queen(5), Queen(5), Queen(5), Queen(5), Queen(10), Queen(10), Queen(10), Queen(10),
                    Queen(15), Queen(15), Queen(15), Queen(20)])
        move = MoveQueen(kralovne)
        move.play(SleepingQueenPosition(1))
        self.assertEqual(None, move.sleeping_queens.collection[1])
        self.assertEqual(move.getLastMoved(),Queen(5))
        self.assertFalse(move.play(SleepingQueenPosition(1)))
        move.add(Queen(5))
        self.assertEqual(Queen(5), move.sleeping_queens.collection[1])

if __name__ == '__main__':
    unittest.main()
