from __future__ import annotations
from typing import List
from Position import HandPosition, SleepingQueenPosition,AwokenQueenPosition,Position
from Game import Game

class GameObserverInterface:
    def notify(self, message: str):
        pass

class GameObservable(GameObserverInterface):
    def __init__(self):
        self.players = list()
        self.observers = list()

    def addObserver(self,observer: GameObserverInterface) -> None:
        self.observers.append(observer)

    def addPlayer(self,player) -> None:
        if len(self.players) < 5:
            self.observers.append(player)
            self.players.append(player)

    def remove(self,observer) -> None:
        self.observers.remove(observer)

    def getObservers(self):
        return self.observers

    def getPlayers(self):
        return self.players

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
        self.game = None

    def create_game(self):
        self.game = Game(len(self.observable.players))

    def play(self,player : str, cards: str) ->None:
        index = int(player)
        if index-1 != self.game.state.onTurn:
            self.observable.notifyPlayer(index,"It is not your turn")
            print("It is not your turn")
            return
        player = self.game.players[index-1]
        commands = cards.split()
        def getPositions() -> List[Position]:

            positions = list()
            """
            Commands
            h<n> stands n-th card from hand
            a<n><m> stands for attacking n-th player´s m-th queen
            s<n> stands for awakening n-th sleepingqueen from deck 
            """
            for command in commands:
                if command[0] == "h":
                    index = int(command[1])
                    if index > 5:
                        self.observable.notifyPlayer(index,"Wrong index of card")
                        return list()
                    pos = HandPosition(index-1, player)
                    positions.append(pos)
                elif command[0] == "a":
                    index = int(command[2])
                    playerIdx = int(command[1])
                    if playerIdx> self.game.numofplayers:
                        self.observable.notifyPlayer(playerIdx,"Wrong index")
                        return list()
                    positions.append(AwokenQueenPosition(index-1,self.game.players[playerIdx-1]))
                elif command[0] == "s":
                    index = int(command[1:])
                    if index > 12:
                        self.observable.notifyAll("There are only 12 queens in the game")
                        return list()

                    else:
                        positions.append(SleepingQueenPosition(index-1))
            return positions

        self.game.play(index-1, getPositions())
        if self.isFinished()[0]:
            print(f"The game has ended, winner is player {self.isFinished()[1]}")


    def isFinished(self) -> (bool,str):
        ended = False
        if self.game.sleeping_queens.getQueens() == [None for i in range (12)]:
            self.observable.notifyAll("The game has ended")
            ended = True
        sums_of_points = list()
        for i in self.game.players:
            sum = 0
            queens = i.awoken.getQueens()
            for x in queens:
                sum += x.getPoints()
            sums_of_points.append(sum)
        if max(sums_of_points) >= self.game.required_points or ended == True:
            self.observable.notifyAll("The game has ended")
            return True,str(sums_of_points.index(max(sums_of_points))+1)
        return False,""


