import unittest
from GameObservable_GameAdaptor import GameAdaptor
from Game import Game
from Card_CardType import Card,CardType
from Position import SleepingQueenPosition

class TestGameAdaptor(unittest.TestCase):
    def test_Adaptor(self):
        adaptor: GameAdaptor = GameAdaptor()
        #adaptor has observable atribute which is a instance of class GameObservable
        adaptor.observable.addPlayer("Igor")
        adaptor.observable.addPlayer("Andrej")
        adaptor.observable.addObserver("Terezka")
        self.assertTrue(3 == len(adaptor.observable.getObservers()))
        self.assertTrue(2 == len(adaptor.observable.getPlayers()))
        self.assertTrue(adaptor.game.numofplayers == 0) #game has not been created yet
        adaptor.create_game()
        self.assertTrue(isinstance(adaptor.game,Game))
        #inserting cards to hands of players just for testing
        adaptor.game.players[0].hand.setCards([Card(CardType.Number, 1), Card(CardType.King,0),Card(CardType.Dragon,0),
                                              Card(CardType.Number, 1), Card(CardType.King,0)],5)
        adaptor.game.players[1].hand.setCards([Card(CardType.Number,1), Card(CardType.King,0), Card(CardType.Knight, 0),
                                              Card(CardType.Knight, 0),Card(CardType.King, 0)],5)
        adaptor.game.drawing_and_trash_pile.drawing_pile[:7] = [Card(CardType.Wand, 1), Card(CardType.Potion,0),Card(CardType.Number,2),
                                              Card(CardType.Number, 2), Card(CardType.King, 0), Card(CardType.Dragon, 0),
                                              Card(CardType.Number, 2)]
        #game has begun
        adaptor.play("1", "h2 s1")
        adaptor.play("2", "h2 s4")
        self.assertTrue(len(adaptor.game.players[0].awoken.getQueens()) == 1)
        self.assertTrue(len(adaptor.game.players[1].awoken.getQueens()) == 1)
        adaptor.play("2", "h2 s2") # it is not player2 turn
        adaptor.play("1", "h1 h3") # he plays numbered cards
        adaptor.play("2", "h2 a11") #player2 plays knight, but player1 has a dragon
        self.assertTrue(len(adaptor.game.players[1].awoken.getQueens()) == 1) # player1 had a dragon
        #player1 has now this cards [CardType.King 0, CardType.Wand 1, CardType.Number 2, CardType.Number 2, CardType.Dragon 0]
        #player2 has now this cards [CardType.Number 1, CardType.Knight 0, CardType.King 0, CardType.Potion 0, CardType.King 0]
        adaptor.play("1", "h1 s12")
        self.assertTrue(len(adaptor.game.players[0].awoken.getQueens()) == 2)
        adaptor.play("2", "h4 a11")
        self.assertTrue(len(adaptor.game.players[0].awoken.getQueens()) == 2) #he had magic wand

    def endGame(self):
        adaptor: GameAdaptor = GameAdaptor()
        # adaptor has observable atribute which is a instance of class GameObservable
        adaptor.observable.addPlayer("Igor")
        adaptor.observable.addPlayer("Andrej")
        adaptor.observable.addObserver("Terezka")
        adaptor.create_game()
        ## imitating the end of game -  putting a lot of queens into player1 hand so he had many points
        adaptor.game.players[0].awoken.addAwoken(adaptor.game.sleeping_queens.removeSleepingQueen(SleepingQueenPosition(5)))
        adaptor.game.players[0].awoken.addAwoken(adaptor.game.sleeping_queens.removeSleepingQueen(SleepingQueenPosition(9)))
        adaptor.game.players[0].awoken.addAwoken(adaptor.game.sleeping_queens.removeSleepingQueen(SleepingQueenPosition(11)))
        adaptor.game.players[0].awoken.addAwoken(adaptor.game.sleeping_queens.removeSleepingQueen(SleepingQueenPosition(8)))
        adaptor.game.players[0].awoken.addAwoken(adaptor.game.sleeping_queens.removeSleepingQueen(SleepingQueenPosition(7)))
        # he has a lot of point but i am testing the last move where game writes that it is finished
        adaptor.play("1", "h1 s6")
        self.assertTrue(adaptor.game_finished.isFinished(adaptor.game)[0]) #the game has finished
        #the game has ended
        ## just testing ilegal move
        adaptor.play("2", "h1 h2")
        #print(adaptor.game.players[1].hand.cards)
        #the picked cards were a king and a numbered card, they werent used, because it would
        # be illegal, they were inserted into back of players2 hand

    def too_many_players(self):
        adaptor: GameAdaptor = GameAdaptor()
        for i in range(6):
            adaptor.observable.addPlayer(f"{i}")
        adaptor.create_game()
        self.assertEqual(5, adaptor.game.numofplayers)# maximum number of players is five
        adaptor.game.sleeping_queens.collection = [None for i in range(12)]
        self.assertTrue(adaptor.game_finished.isFinished(adaptor.game)[0])  # testing the end of the game, no queens, left



if __name__ == '__main__':
     unittest.main()
