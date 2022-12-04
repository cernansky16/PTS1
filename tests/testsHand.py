import unittest
from Game import Game
from Hand import Hand
from Card_CardType import Card,Queen
from Position import HandPosition,AwokenQueenPosition

class TestHand(unittest.TestCase):

    def test_Hand_sociable(self):
        hra = Game(4)
        kopka = hra.drawing_and_trash_pile
        hrac0 = hra.players[0]
        ruka: Hand = hrac0.hand
        ruka.cards = [Card(1, 1), Card(1, 2), Card(1, 3), Card(2, 0), Card(5, 0)]
        self.assertTrue(ruka.hasCardOfType(1))
        self.assertTrue(ruka.hasCardOfType(2))
        self.assertFalse(ruka.hasCardOfType(6))
        cards0 = ruka.getCards()
        self.assertEqual(ruka.cards, cards0)
        self.assertEqual(0,ruka.getIndex())
        picked = ruka.pickCards([HandPosition(0,hra.players[0]),HandPosition(1,hra.players[0]),HandPosition(2,hra.players[0])])
        self.assertEqual(picked, [Card(1, 1), Card(1, 2), Card(1, 3)])
        ruka.removePickedCardsAndDraw()
        self.assertEqual(5,len(ruka.getCards()))
        self.assertEqual(kopka.getCardsDiscardedThisTurn(),[Card(1, 1), Card(1, 2), Card(1, 3)])
        self.assertEqual(len(kopka.trash_pile),3)
    def test_evaluate_attack(self):
        hra = Game(4)
        kopka = hra.drawing_and_trash_pile
        utocnik = hra.players[0]
        utocnik.hand.cards= [Card(1, 1), Card(1, 2), Card(1, 3), Card(4, 0), Card(4, 0)]
        utocnik.hand.cards[0].setHandPosition(0,utocnik)
        utocnik.hand.cards[1].setHandPosition(1, utocnik)
        utocnik.hand.cards[2].setHandPosition(2, utocnik)
        utocnik.hand.cards[3].setHandPosition(3, utocnik)
        utocnik.hand.cards[4].setHandPosition(4, utocnik)
        obranca = hra.players[1]
        obranca.awoken.add(Queen(10))
        obranca.hand.cards = [Card(1, 1), Card(1, 2), Card(1, 3), Card(2, 0), Card(6, 0)]
        obranca.hand.cards[0].setHandPosition(0, obranca)
        obranca.hand.cards[1].setHandPosition(1, obranca)
        obranca.hand.cards[2].setHandPosition(2, obranca)
        obranca.hand.cards[3].setHandPosition(3, obranca)
        obranca.hand.cards[4].setHandPosition(4, obranca)
        self.assertTrue(utocnik.play([HandPosition(3,utocnik),AwokenQueenPosition(0,obranca)]))
        self.assertTrue(len(obranca.awoken.getQueens()) == 1)
        self.assertTrue(len(utocnik.awoken.getQueens()) == 0)
        self.assertTrue(utocnik.play([HandPosition(3, utocnik), AwokenQueenPosition(0, obranca)]))
        self.assertTrue(len(obranca.awoken.getQueens()) == 0)
        self.assertTrue(len(utocnik.awoken.getQueens()) == 1)


if __name__ == '__main__':
    unittest.main()

