import unittest
from unittest.mock import  Mock,MagicMock
from Game import Game
from Hand import Hand
from Card_CardType import Card
from Position import HandPosition,AwokenQueenPosition,SleepingQueenPosition

class TestHand(unittest.TestCase):
    def test_hand_mock(self):
        cards_to_draw = [Card(2, 0), Card(1, 7), Card(6, 0)]
        self.fake_pile = Mock()
        self.fake_pile.discardAndDraw = MagicMock(return_value = cards_to_draw)
        ruka = Hand(0,self.fake_pile)
        ruka.cards = [Card(2, 0), Card(1, 2), Card(2, 0), Card(1, 1), Card(5, 0)]
        self.assertTrue(ruka.hasCardOfType(1))  # has numbered card
        self.assertFalse(ruka.hasCardOfType(6))  # does not have magicwand
        cards0 = ruka.getCards()
        self.assertEqual(ruka.cards, cards0)
        self.assertEqual(0, ruka.getIndex())  # the index of hand is right
        picked = ruka.pickCards(
            [HandPosition(0, Mock()), HandPosition(1, Mock()),
             HandPosition(2, Mock())]) # Mock to imitate player
        self.assertEqual(picked, [Card(1, 1), Card(1, 2), Card(1, 3)])  # pick method picks right cards
        self.assertEqual(2, len(ruka.getCards()))
        ruka.removePickedCardsAndDraw(picked)
        self.assertEqual(5, len(ruka.getCards()))

    def test_Hand_sociable(self):
        hra = Game(4)
        kopka = hra.drawing_and_trash_pile
        hrac0 = hra.players[0]
        ruka: Hand = hrac0.hand
        ruka.cards = [Card(1, 1), Card(1, 2), Card(1, 3), Card(2, 0), Card(5, 0)]
        self.assertTrue(ruka.hasCardOfType(1)) #has numbered card
        self.assertTrue(ruka.hasCardOfType(2)) #has a king
        self.assertFalse(ruka.hasCardOfType(6)) # does not have magicwand
        picked = ruka.pickCards([HandPosition(0,hra.players[0]),HandPosition(1,hra.players[0]),HandPosition(2,hra.players[0])])
        self.assertEqual(picked, [Card(1, 1), Card(1, 2), Card(1, 3)]) # pick method picks right cards
        self.assertEqual(2, len(ruka.getCards())) # has now only 2 cards
        ruka.removePickedCardsAndDraw(picked)
        self.assertEqual(5,len(ruka.getCards())) # cards have been redrawn
        self.assertEqual(kopka.getCardsDiscardedThisTurn(),[Card(1, 1), Card(1, 2), Card(1, 3)])
        self.assertEqual(len(kopka._trash_pile), 3) # cards are in trash pile now

    def test_evaluate_attack_and_move_queen(self):
         hra = Game(4)
         kopka = hra.drawing_and_trash_pile
         utocnik = hra.players[0]
         utocnik.hand.cards= [Card(1, 1), Card(1, 2), Card(4, 0), Card(3, 0), Card(3, 0)]
         utocnik.hand.cards[0].setHandPosition(0,utocnik)
         utocnik.hand.cards[1].setHandPosition(1, utocnik)
         utocnik.hand.cards[2].setHandPosition(2, utocnik)
         utocnik.hand.cards[3].setHandPosition(3, utocnik)
         utocnik.hand.cards[4].setHandPosition(4, utocnik)
         obranca = hra.players[1]
         obranca.awoken.add(hra.sleeping_queens.removeQueen(SleepingQueenPosition(0)))
         self.assertFalse(hra.sleeping_queens.removeQueen(SleepingQueenPosition(0))) # cant remove queen which is not there
         obranca.hand.cards = [Card(4, 0), Card(1, 2), Card(1, 3), Card(2, 0), Card(5, 0)]
         obranca.hand.cards[0].setHandPosition(0, obranca)
         obranca.hand.cards[1].setHandPosition(1, obranca)
         obranca.hand.cards[2].setHandPosition(2, obranca)
         obranca.hand.cards[3].setHandPosition(3, obranca)
         obranca.hand.cards[4].setHandPosition(4, obranca)
         hra.drawing_and_trash_pile.drawing_pile[:5] = [Card(1, 2),Card(1, 10),Card(1, 2),Card(1, 9),Card(6, 0)]
         # Just assuring that the second card is not (5,0) beacuse the test would fail, also for further testing, it is better that the cards at
         # top are numbered cards, also i need that obranca has a magic wand
         self.assertTrue(utocnik.play([HandPosition(3,utocnik),AwokenQueenPosition(0,obranca)]))
         self.assertTrue(len(obranca.awoken.getQueens()) == 1) # obranca had fought off the attack
         self.assertTrue(len(utocnik.awoken.getQueens()) == 0)
         utocnik.play([HandPosition(3, utocnik), AwokenQueenPosition(0, obranca)])
         self.assertFalse(len(obranca.awoken.getQueens()) == 1)
         self.assertTrue(len(utocnik.awoken.getQueens()) == 1) # the attack has been sucessful
         obranca.play([HandPosition(0,obranca),AwokenQueenPosition(0,utocnik)])# obranca has put the queen to sleep
         obranca.play([HandPosition(2, obranca), SleepingQueenPosition(9)]) # obranca has used a king to wake up a queen
         # now cards of utocnik are = [1 1, 1 2, 4 0, 1 2, 1 2]
         # cards of obranca are =  [1 2, 1 3, 1 10, 1 9, 6 0]
         self.assertEqual(obranca.state.cards,[Card(1,2),Card(1,3),Card(1,10),Card(1,9),Card(6,0)])
         self.assertFalse(obranca.play([HandPosition(4,obranca),AwokenQueenPosition(0,1)])) #utocnik has no queen that could be woken up
         self.assertTrue(utocnik.evaluateNumberedCards([Card(1,2),Card(1,2)]))
         self.assertTrue(utocnik.play([HandPosition(1,utocnik),HandPosition(4,utocnik)]))








