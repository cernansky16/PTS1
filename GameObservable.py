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
    def add(self,observer) -> None:
        self.observers.append(observer)
    def addPlayer(self,player,observer) -> None:
        self.observers.append(observer)
        self.players.append(player)
    def remove(self,observer) -> None:
        self.observers.remove(observer)
    def notifyAll(self,message) -> None:
        pass
class GamePlayerInterface:
    def play(self,player : str, cards: str):
        pass

class GameAdaptor(GamePlayerInterface):
    def __init__(self):
        self.observable = GameObservable()
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
            h<n> stands for hand of n-th player
            a<n><m> stands for attacking n-th player´s m-th queen
            s<n> stands for awakening n-th sleepingqueen from deck 
            """
            for command in commands:
                if command[0] == "h":
                    index = int(command[1])
                    pos = HandPosition(index,player)
                    handpos.append(pos)
                elif command[0] == "a":
                    index = int(command[1])
                    playerIdx = int(command[2])
                    awokenqueenpos = AwokenQueenPosition(index,self.game.players[playerIdx-1])
                elif command[0] == "s":
                    index = int(command[1])
                    sleepingpos = SleepingQueenPosition(index)
                return [handpos, sleepingpos, awokenqueenpos]

        self.game.play(index,getPositions())

class GameFinishedInterface:
    def isFinished(self) -> bool:
       pass
class GameFinished(GameFinishedInterface):
    pass




