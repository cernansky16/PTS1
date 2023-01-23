import unittest
from unittest.mock import Mock, MagicMock
from Game import Game
from Hand import Hand, HandInterface
from Piles import DrawingAndTrashPile
from typing import List
from Player import Player
from Card_CardType import Card, CardType
from Position import HandPosition, AwokenQueenPosition, SleepingQueenPosition


class TestHand(unittest.TestCase):
    def test_hand_solitary(self):
        cards_to_draw: List[Card] = [Card(CardType.King, 0), Card(CardType.Number, 7), Card(CardType.Wand, 0)]
        self.fake_pile = Mock()
        self.fake_pile.discardAndDraw = MagicMock(return_value=cards_to_draw)
        ruka: Hand = Hand(0, self.fake_pile)
        ruka.cards = [Card(CardType.King, 0), Card(CardType.Number, 2), Card(CardType.King, 0),
                      Card(CardType.Number, 1), Card(CardType.Dragon, 0)]
        self.assertTrue(ruka.hasCardOfType(CardType.Number))  # has numbered card
        self.assertFalse(ruka.hasCardOfType(CardType.Wand))  # does not have magicwand
        cards0: List[Card] = ruka.getCards()
        self.assertEqual(ruka.cards, cards0)
        self.assertEqual(0, ruka.getIndex())  # the index of hand is right
        picked: List[Card] = ruka.pickCards(
            [HandPosition(0, 0), HandPosition(1, 0),
             HandPosition(2, 0)])
        self.assertEqual(picked, [Card(CardType.Number, 1), Card(CardType.Number, 2), Card(CardType.Number, 3)])
        # pick method picks right cards
        self.assertEqual(2, len(ruka.getCards()))
        ruka.removePickedCardsAndDraw(picked)
        self.assertEqual(5, len(ruka.getCards()))

    def test_Hand_sociable(self):
        hra:Game = Game(4)
        kopka: DrawingAndTrashPile = hra.drawing_and_trash_pile
        hrac0: Player = hra.players[0]
        ruka: HandInterface = hrac0.hand
        ruka.setCards([Card(CardType.Number, 1), Card(CardType.Number, 2), Card(CardType.Number, 3), Card(CardType.King, 0),
                      Card(CardType.Dragon, 0)],5)
        self.assertTrue(ruka.hasCardOfType(CardType.Number)) #has numbered card
        self.assertTrue(ruka.hasCardOfType(CardType.King)) #has a king
        self.assertFalse(ruka.hasCardOfType(CardType.Wand)) # does not have magicwand
        picked = ruka.pickCards([HandPosition(0,0),HandPosition(1,0),HandPosition(2, 0)])
        self.assertEqual(picked, [Card(CardType.Number, 1), Card(CardType.Number, 2), Card(CardType.Number, 3)])
        # pick method picks right cards
        self.assertEqual(2, len(ruka.getCards())) # has now only 2 cards
        ruka.removePickedCardsAndDraw(picked)
        self.assertEqual(5,len(ruka.getCards())) # cards have been redrawn
        self.assertEqual(kopka.getCardsDiscardedThisTurn(),[Card(CardType.Number, 1),
                                                            Card(CardType.Number, 2), Card(CardType.Number, 3)])
        self.assertEqual(len(kopka.trash_pile), 3) # cards are in trash pile now


class TestPlayerSociable(unittest.TestCase):
    def setUp(self) -> None:
        self.hra = Game(4)
        self.kopka = self.hra.drawing_and_trash_pile
        self.utocnik = self.hra.players[0]
        utocnik_cards = [Card(CardType.Number, 1), Card(CardType.Number, 2), Card(CardType.Potion, 0),
                                Card(CardType.Knight, 0), Card(CardType.Knight, 0)]
        self.utocnik.hand.setCards(utocnik_cards,5)
        self.obranca = self.hra.players[1]
        queen = self.hra.sleeping_queens.removeSleepingQueen(SleepingQueenPosition(0))
        self.assertIsNotNone(queen)
        if queen is not None:
            self.obranca.awoken.addAwoken(queen)
        obranca_cards: List[Card]= [Card(CardType.Potion, 0), Card(CardType.Number, 2), Card(CardType.Number, 3),
                              Card(CardType.King, 0), Card(CardType.Dragon, 0)]
        self.obranca.hand.setCards(obranca_cards,5)
        self.hra.drawing_and_trash_pile.drawing_pile[:5] = [Card(CardType.Number, 2), Card(CardType.Number, 10),
                                                       Card(CardType.Number, 2), Card(CardType.Number, 9),
                                                       Card(CardType.Wand, 0)]
        # Just assuring that the second card is not (5,0) beacuse the test would fail, also for further testing,
        # it is better that the cards at
        # top are numbered cards, also i need that obranca has a magic wand

    def test_Player_Sociable(self):
         
         self.assertFalse(self.hra.sleeping_queens.removeSleepingQueen(SleepingQueenPosition(0))) # cant remove queen which is not there
         self.assertTrue(self.utocnik.play([HandPosition(3, 0), AwokenQueenPosition(0, 1)]))
         self.assertTrue(len(self.obranca.awoken.getQueens()) == 1) # obranca had fought off the attack
         self.assertTrue(len(self.utocnik.awoken.getQueens()) == 0)
         self.utocnik.play([HandPosition(3, 0), AwokenQueenPosition(0, 1)])
         self.assertFalse(len(self.obranca.awoken.getQueens()) == 1)
         self.assertTrue(len(self.utocnik.awoken.getQueens()) == 1) # the attack has been sucessful
         self.obranca.play([HandPosition(0,1),AwokenQueenPosition(0,0)]) # obranca has put the queen to sleep
         self.obranca.play([HandPosition(2, 1), SleepingQueenPosition(9)]) # obranca has used a king to wake up a queen
         # now cards of utocnik are = [1 1, 1 2, 4 0, 1 2, 1 2]
         # cards of obranca are =  [1 2, 1 3, 1 10, 1 9, 6 0]
         self.assertEqual(self.obranca.state.cards, [Card(CardType.Number, 2), Card(CardType.Number, 3), Card(CardType.Number, 10),
                                               Card(CardType.Number, 9), Card(CardType.Wand, 0)])
         self.assertFalse(self.obranca.play([HandPosition(4, 1),AwokenQueenPosition(0, 1)])) #utocnik has no queen that could be woken up
         self.assertTrue(self.utocnik.evaluateNumberedCards([Card(CardType.Number, 2),Card(CardType.Number, 2)]))
         self.assertTrue(self.utocnik.play([HandPosition(1,0),HandPosition(4,0)]))
         self.obranca.play([HandPosition(1, 1)])
         self.utocnik.play([HandPosition(2,0),AwokenQueenPosition(0,1)])#obranca has a magic wand against the potion
         self.assertEqual(1, len(self.obranca.awoken.getQueens()))
         cards = self.utocnik.hand.getCards()
         # cards of utocnik are now [CardType.Number 1, CardType.Potion 0, CardType.Number 2, CardType.Number 1, CardType.Number 10]
         self.assertFalse(self.utocnik.play([HandPosition(0, 0), HandPosition(1, 0)]))  # invalid move
         self.assertEqual(self.utocnik.hand.getCards(), cards)




if __name__ == '__main__':
    unittest.main()


