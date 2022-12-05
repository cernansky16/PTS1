from __future__ import annotations
from typing import TYPE_CHECKING,List

if TYPE_CHECKING:
    from Position import HandPosition, SleepingQueenPosition,AwokenQueenPosition
from Game import Game

class GameObserverInterface:
    def notify(self, message: str):
        pass

class GameObservable(GameObserverInterface):
    def __init__(self):
        self.players = list()
        self.observers = list()

    def add(self,observer: GameObserverInterface) -> None:
        self.observers.append(observer)

    def addPlayer(self,player,observer) -> None:
        if len(self.players) > 5:
            self.observers.append(observer)
            self.players.append(player)

    def remove(self,observer) -> None:
        self.observers.remove(observer)

    def notifyPlayer(self,idx,message) -> None:
        pass
    def notifyPlayers(self,message) -> None:
        pass
    def notifyAll(self,message) -> None:
        pass


class GamePlayerInterface:
    def play(self,player : str, cards: str):
        pass

class GameAdaptor(GamePlayerInterface):

    def __init__(self):
        self.observable = GameObservable()

    def create_game(self):
        self.game = Game(len(self.observable.players))

    def play(self,player : str, cards: str) ->None:
        index = int(player)
        player = self.game.players[index-1]
        commands = cards.split()
        def getPositions():
            handpos : List[HandPosition] = []
            sleepingpos = None
            awokenqueenpos = None
            """
            Commands
            h<n> stands n-th card from hand
            a<n><m> stands for attacking n-th player´s m-th queen
            s<n> stands for awakening n-th sleepingqueen from deck 
            """
            for command in commands:
                if command[0] == "h":
                    index = int(command[1])
                    if index > self.game.numofplayers:
                        self.observable.notifyPlayer(index,"Wrong index")
                    pos = HandPosition(index-1,player)
                    handpos.append(pos)
                elif command[0] == "a":
                    index = int(command[2])
                    playerIdx = int(command[1])
                    if index > self.game.numofplayers:
                        self.observable.notifyPlayer(playerIdx,"Wrong index")
                    awokenqueenpos = AwokenQueenPosition(index-1,self.game.players[playerIdx-1])
                elif command[0] == "s":
                    index = int(command[1])
                    if index > 12:
                        self.observable.notifyAll("There are only 12 queens in the game")
                    sleepingpos = SleepingQueenPosition(index-1)
                return [handpos, sleepingpos, awokenqueenpos]

        self.game.play(index, getPositions())
        if self.game.sleeping_queens.getQueens() == [None for i in range (12)]:
            self.observable.notifyAll("The game has ended")
        sums_of_points = list()
        for i in self.game.players:
            sum = 0
            queens = i.awoken.getQueens()
            for x in queens:
                sum += x.getPoints()
            sums_of_points.append(sum)
        if max(sums_of_points) >= self.game.required_points:
            self.observable.notifyAll("The game has ended")



# class GameFinishedInterface:
#     def isFinished(self) -> bool:
#        pass
#
# class GameFinished(GameFinishedInterface):
#     pass




