import unittest
from GameObservable import GameAdaptor,GameObservable
from Game import Game
from Card_CardType import Card,Queen
from Position import SleepingQueenPosition

class TestGameAdaptor(unittest.TestCase):
    def test_Adaptor(self):
        adaptor = GameAdaptor()
        #adaptor has observable atribute which is a instance of class GameObservable
        adaptor.observable.addPlayer("Igor")
        adaptor.observable.addPlayer("Andrej")
        adaptor.observable.addObserver("Terezka")
        self.assertTrue(3 == len(adaptor.observable.getObservers()))
        self.assertTrue(2 == len(adaptor.observable.getPlayers()))
        self.assertTrue(adaptor.game == None)
        adaptor.create_game()
        self.assertTrue(isinstance(adaptor.game,Game))
        #inserting cards to hands of players just for testing
        adaptor.game.players[0].hand.cards = [Card(1,1),Card(2,0),Card(5,0),Card(1,1),Card(2,0)]
        adaptor.game.players[1].hand.cards = [Card(1,1),Card(2,0),Card(3,0),Card(3,1),Card(2,0)]
        #game has begun
        adaptor.play("1", "h2 s1")
        adaptor.play("2", "h2 s4")
        self.assertTrue(len(adaptor.game.players[0].awoken.getQueens())==1)
        self.assertTrue(len(adaptor.game.players[1].awoken.getQueens()) == 1)
        adaptor.play("2", "h2 s2") # Game notifies player2 it is not his turn
        adaptor.play("1", "h1 h3")
        adaptor.play("2", "h2 a11")
        self.assertTrue(len(adaptor.game.players[1].awoken.getQueens()) == 1)
        self.assertTrue(len(adaptor.game.players[1].awoken.getQueens()) == 1) # player1 had a dragon
        ## imitating the end of game -  putting a lot of queens into player1 hand so he had many points
        adaptor.game.players[0].awoken.add(adaptor.game.sleeping_queens.removeQueen(SleepingQueenPosition(5)))
        adaptor.game.players[0].awoken.add(adaptor.game.sleeping_queens.removeQueen(SleepingQueenPosition(9)))
        adaptor.game.players[0].awoken.add(adaptor.game.sleeping_queens.removeQueen(SleepingQueenPosition(11)))
        adaptor.game.players[0].awoken.add(adaptor.game.sleeping_queens.removeQueen(SleepingQueenPosition(8)))
        adaptor.game.players[0].awoken.add(adaptor.game.sleeping_queens.removeQueen(SleepingQueenPosition(7)))
        # he has a lot of point but i am testing the last move where game writes that it is finished
        adaptor.play("1","h1 s6")




