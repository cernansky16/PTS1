import unittest
from Game import Game
from Hand import Hand
from Card_CardType import Card
from Position import HandPosition
class TestHand(unittest.TestCase):

    def test_Hand(self):
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
        self.assertTrue(len(kopka.trash_pile)==3)

if __name__ == '__main__':
    unittest.main()

