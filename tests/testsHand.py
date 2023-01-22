import unittest
from unittest.mock import Mock, MagicMock
from Game import Game
from Hand import Hand
from Card_CardType import Card, CardType
from Position import HandPosition, AwokenQueenPosition, SleepingQueenPosition

class TestHand(unittest.TestCase):
    def test_hand_mock(self):
        cards_to_draw = [Card(CardType.King, 0), Card(CardType.Number, 7), Card(CardType.Wand, 0)]
        self.fake_pile = Mock()
        self.fake_pile.discardAndDraw = MagicMock(return_value=cards_to_draw)
        ruka = Hand(0,self.fake_pile)
        ruka.cards = [Card(CardType.King, 0), Card(CardType.Number, 2), Card(CardType.King, 0),
                      Card(CardType.Number, 1), Card(CardType.Dragon, 0)]
        self.assertTrue(ruka.hasCardOfType(CardType.Number))  # has numbered card
        self.assertFalse(ruka.hasCardOfType(CardType.Wand))  # does not have magicwand
        cards0 = ruka.getCards()
        self.assertEqual(ruka.cards, cards0)
        self.assertEqual(0, ruka.getIndex())  # the index of hand is right
        picked = ruka.pickCards(
            [HandPosition(0, 0), HandPosition(1, 0),
             HandPosition(2, 0)])
        self.assertEqual(picked, [Card(CardType.Number, 1), Card(CardType.Number, 2), Card(CardType.Number, 3)])  # pick method picks right cards
        self.assertEqual(2, len(ruka.getCards()))
        ruka.removePickedCardsAndDraw(picked)
        self.assertEqual(5, len(ruka.getCards()))

    def test_Hand_sociable(self):
        hra = Game(4)
        kopka = hra.drawing_and_trash_pile
        hrac0 = hra.players[0]
        ruka: Hand = hrac0.hand
        ruka.cards = [Card(CardType.Number, 1), Card(CardType.Number, 2), Card(CardType.Number, 3), Card(CardType.King, 0), Card(CardType.Dragon, 0)]
        self.assertTrue(ruka.hasCardOfType(CardType.Number)) #has numbered card
        self.assertTrue(ruka.hasCardOfType(CardType.King)) #has a king
        self.assertFalse(ruka.hasCardOfType(CardType.Wand)) # does not have magicwand
        picked = ruka.pickCards([HandPosition(0,hra.players[0]),HandPosition(1,hra.players[0]),HandPosition(2,hra.players[0])])
        self.assertEqual(picked, [Card(CardType.Number, 1), Card(CardType.Number, 2), Card(CardType.Number, 3)]) # pick method picks right cards
        self.assertEqual(2, len(ruka.getCards())) # has now only 2 cards
        ruka.removePickedCardsAndDraw(picked)
        self.assertEqual(5,len(ruka.getCards())) # cards have been redrawn
        self.assertEqual(kopka.getCardsDiscardedThisTurn(),[Card(CardType.Number, 1),
                                                            Card(CardType.Number, 2), Card(CardType.Number, 3)])
        self.assertEqual(len(kopka._trash_pile), 3) # cards are in trash pile now

    def test_evaluate_attack_and_move_queen(self):
         hra = Game(4)
         kopka = hra.drawing_and_trash_pile
         utocnik = hra.players[0]
         utocnik.hand.cards= [Card(CardType.Number, 1), Card(CardType.Number, 2), Card(CardType.Potion, 0),
                              Card(CardType.Knight, 0), Card(CardType.Knight, 0)]
         utocnik.hand.cards[0].setHandPosition(0, 0)
         utocnik.hand.cards[1].setHandPosition(1, 0)
         utocnik.hand.cards[2].setHandPosition(2, 0)
         utocnik.hand.cards[3].setHandPosition(3, 0)
         utocnik.hand.cards[4].setHandPosition(4, 0)
         obranca = hra.players[1]
         obranca.awoken.addAwoken(hra.sleeping_queens.removeSleepingQueen(SleepingQueenPosition(0)))
         self.assertFalse(hra.sleeping_queens.removeSleepingQueen(SleepingQueenPosition(0))) # cant remove queen which is not there
         obranca.hand.cards = [Card(CardType.Potion, 0), Card(CardType.Number, 2), Card(CardType.Number, 3),
                               Card(CardType.King, 0), Card(CardType.Dragon, 0)]
         obranca.hand.cards[0].setHandPosition(0, 1)
         obranca.hand.cards[1].setHandPosition(1, 1)
         obranca.hand.cards[2].setHandPosition(2, 1)
         obranca.hand.cards[3].setHandPosition(3, 1)
         obranca.hand.cards[4].setHandPosition(4, 1)
         hra.drawing_and_trash_pile.drawing_pile[:5] = [Card(CardType.Number, 2), Card(CardType.Number, 10),
                                                        Card(CardType.Number, 2), Card(CardType.Number, 9), Card(CardType.Wand, 0)]
         # Just assuring that the second card is not (5,0) beacuse the test would fail, also for further testing, it is better that the cards at
         # top are numbered cards, also i need that obranca has a magic wand
         self.assertTrue(utocnik.play([HandPosition(3, 0), AwokenQueenPosition(0, 1)]))
         self.assertTrue(len(obranca.awoken.getQueens()) == 1) # obranca had fought off the attack
         self.assertTrue(len(utocnik.awoken.getQueens()) == 0)
         utocnik.play([HandPosition(3, 0), AwokenQueenPosition(0, 1)])
         self.assertFalse(len(obranca.awoken.getQueens()) == 1)
         self.assertTrue(len(utocnik.awoken.getQueens()) == 1) # the attack has been sucessful
         obranca.play([HandPosition(0,1),AwokenQueenPosition(0,0)])# obranca has put the queen to sleep
         obranca.play([HandPosition(2, 1), SleepingQueenPosition(9)]) # obranca has used a king to wake up a queen
         # now cards of utocnik are = [1 1, 1 2, 4 0, 1 2, 1 2]
         # cards of obranca are =  [1 2, 1 3, 1 10, 1 9, 6 0]
         self.assertEqual(obranca.state.cards, [Card(CardType.Number, 2), Card(CardType.Number, 3), Card(CardType.Number, 10),
                                               Card(CardType.Number, 9), Card(CardType.Wand, 0)])
         self.assertFalse(obranca.play([HandPosition(4, 1),AwokenQueenPosition(0, 1)])) #utocnik has no queen that could be woken up
         self.assertTrue(utocnik.evaluateNumberedCards([Card(CardType.Number, 2),Card(CardType.Number, 2)]))
         self.assertTrue(utocnik.play([HandPosition(1,0),HandPosition(4,0)]))
         obranca.play([HandPosition(1, 1)])
         utocnik.play([HandPosition(2,0),AwokenQueenPosition(0,1)])#obranca has a magic wand against the potion
         self.assertEqual(1, len(obranca.awoken.getQueens()))
         # print(obranca.state)
         cards = utocnik.hand.getCards()
         # cards of utocnik are now [CardType.Number 1, CardType.Potion 0, CardType.Number 2, CardType.Number 1, CardType.Number 10]
         self.assertFalse(utocnik.play([HandPosition(0, 0), HandPosition(1, 0)]))  # invalid move
         self.assertEqual(utocnik.hand.getCards(), cards)




if __name__ == '__main__':
    unittest.main()


