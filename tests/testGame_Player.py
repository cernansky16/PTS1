import unittest
from unittest.mock import Mock,MagicMock
from Game import Game
from Card_CardType import Card,Queen,CardType
from QueenCollection import QueenCollection,MoveQueen
from Position import HandPosition,SleepingQueenPosition,AwokenQueenPosition,Position
from Player import Player
from Piles import DrawingAndTrashPile,Strategy1
from GameState_PlayerState import GameState
from typing import List


class TestPlayerSolitary(unittest.TestCase):
    def setUp(self) -> None:
        self.hra = Mock()
        self.hrac0: Player = Player(Mock(), Mock(), Mock(), Mock(), Mock())
        self.hra.drawing_and_trash_pile = Mock()
        self.hrac0.hand.removePickedCardsAndDraw = MagicMock(return_value=[Card(CardType.Number, 7)])
        hrac0_cards = [Card(CardType.Number, 1), Card(CardType.Number, 4), Card(CardType.King, 0),
                                 Card(CardType.Number, 5), Card(CardType.Potion, 0)]
        self.hrac0.hand.setCards(hrac0_cards,5)
        self.hrac0.hand.setPositions()
        self.good_cards0: List[Position] = [HandPosition(0, 0)]
        self.bad_cards0: List[Position]= [HandPosition(0, 0), HandPosition(4, 0)]
        self.bad_cards1: List[Position]= [HandPosition(2, 0), HandPosition(4, 0)]
        self.good_cards1: List[Position]= [HandPosition(2, 0), SleepingQueenPosition(0)]

    def test_Player_evaluate_numbered_cards(self):

        """testing method evaluated numbered cards"""
        self.assertTrue(self.hrac0.evaluateNumberedCards([Card(CardType.Number,1)])) #valid
        self.assertTrue(self.hrac0.evaluateNumberedCards([Card(CardType.Number, 1),Card(CardType.Number, 4),
                                                          Card(CardType.Number, 5)])) # valid equation
        self.assertTrue(self.hrac0.evaluateNumberedCards([Card(CardType.Number, 4), Card(CardType.Number, 4)]))#valid
        self.assertFalse(self.hrac0.evaluateNumberedCards([Card(CardType.Number, 4), Card(CardType.Number, 2)]))#not valid
        self.assertFalse(self.hrac0.evaluateNumberedCards([Card(CardType.King, 0)]))
        self.assertFalse(self.hrac0.evaluateNumberedCards([Card(CardType.King, 0),Card(CardType.Number, 4)]))
        self.assertTrue(self.hrac0.evaluateNumberedCards([Card(CardType.Number, 1), Card(CardType.Number, 1), Card(CardType.Number, 1),
                                                          Card(CardType.Number, 1), Card(CardType.Number, 4)]))

    def test_method_play(self):
        self.hrac0.move_queen.play = MagicMock(return_value=True)
        self.hrac0.hand.pickCards = MagicMock(return_value =[Card(CardType.Number, 7)])
        self.assertTrue(self.hrac0.play(self.good_cards0))
        self.hrac0.hand.pickCards = MagicMock(return_value=[Card(CardType.Number, 7), Card(CardType.Wand,0)])
        self.assertFalse(self.hrac0.play(self.bad_cards0)) #wrongly picked cards
        self.hrac0.hand.pickCards = MagicMock(return_value=[Card(CardType.Knight, 0), Card(CardType.Wand, 0)])
        self.assertFalse(self.hrac0.play(self.bad_cards1))  # wrongly picked cards
        self.hrac0.hand.pickCards = MagicMock(return_value=[Card(CardType.King, 0)])
        self.assertTrue(self.hrac0.play(self.good_cards1))  # goodly picked cards

    def test_attack(self):
        self.hrac0.evaluate_attack = MagicMock(return_value=True)
        self.good_cards2: List[Position] = [HandPosition(4, 0), AwokenQueenPosition(0,1)]
        self.hrac0.hand.pickCards = MagicMock(return_value=[Card(CardType.Potion, 0)])
        self.hrac0.hand.getCards = MagicMock(return_value=[Card(CardType.Number, 1), Card(CardType.Number, 4), Card(CardType.King, 0),
                                 Card(CardType.Number, 5), Card(CardType.Potion, 0)])
        self.assertTrue(self.hrac0.play(self.good_cards2))

class OtherClassesTests(unittest.TestCase):
    def testGame_Gamestate(self):

        hra: Game = Game(4)
        self.assertEqual(4, hra.numofplayers)
        self.assertTrue(len(hra.sleeping_queens.getQueens()), 12)
        self.assertTrue(hra.required_points, 40)
        self.assertEqual(hra.required_queens, 4)
        self.assertTrue(hra.drawing_and_trash_pile.trash_pile == list()) # no cards in trash pile
        self.assertEqual(len(hra.drawing_and_trash_pile.drawing_pile),42) # 20 cards has been distributed
        hra.players[0].hand.setCards([Card(CardType.King, 0)],0)
        state: GameState = hra.play(0, [HandPosition(0, 0), SleepingQueenPosition(9)]) #player0 has played a king to awaken a queen
        self.assertEqual(state.onTurn, 1) # now is on turn player 1
        self.assertEqual(len(hra.players[0].awoken.getQueens()),1)
        self.assertIsNone(hra.sleeping_queens.collection[9])


    def test_drawing_and_trash_pile(self):
        pile: DrawingAndTrashPile = DrawingAndTrashPile(Strategy1())
        self.assertEqual(len(pile.discardAndDraw([Card(CardType.Number, 1),Card(CardType.Number, 2)])), 2) #it has returned two cards
        self.assertEqual([Card(CardType.Number, 1), Card(CardType.Number, 2)], pile.getCardsDiscardedThisTurn())
        pile2: DrawingAndTrashPile = DrawingAndTrashPile(Strategy1())
        self.assertEqual(62, len(pile2.drawing_pile))
        self.assertEqual(0, len(pile2.trash_pile))
        #just testing reset drawing pile method
        pile2.trash_pile = pile2.drawing_pile[:]
        pile2.drawing_pile = list()
        self.assertEqual(0, len(pile2.drawing_pile))

    def test_QueenCollection(self):
        colection = QueenCollection()
        colection.addAwoken(Queen(10))
        self.assertEqual(1,len(colection.getQueens()))
        colection.addAwoken(Queen(5))
        self.assertIsNone(colection.removeAwokenQueen(AwokenQueenPosition(98,0))) #wrong position
        self.assertEqual(colection.removeAwokenQueen(AwokenQueenPosition(1,0)),Queen(5))
        self.assertEqual(colection.removeAwokenQueen(AwokenQueenPosition(0,0)), Queen(10))
        self.assertEqual(colection.getQueens(), [])
        self.assertIsNone(colection.removeAwokenQueen(AwokenQueenPosition(98,0)))

    def testQueen(self):
        queen = Queen(20)
        self.assertEqual(20,queen.getPoints())

    def testCard_CardType(self):
        card = Card(CardType.Wand, 0)
        self.assertEqual(CardType.Wand, card.getType())
        self.assertEqual(0, card.getValue())
        card.setHandPosition(0,0)
        self.assertIsInstance(card.getHandPosition(),HandPosition)
        card2 = Card(CardType.Number, 10)
        self.assertEqual(card2.getValue(), 10)
        card2.setHandPosition(2, 0)
        self.assertTrue(card2.getHandPosition().getCardidx() == 2)

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
