from __future__ import annotations
from typing import List
from Position import HandPosition, SleepingQueenPosition,AwokenQueenPosition,Position
from Game import Game

class GameFinishedInterface:
    def is_finished(self) -> tuple[bool, int] :
        return False,-1


class GameFinished(GameFinishedInterface):
    @staticmethod
    def isFinished(game: Game) -> tuple[bool, int]: #returns wheter the game has finished and returns index of winner
        ended = False
        if game.sleeping_queens.getQueens() == [None for i in range(12)]:
            ended = True
        sums_of_points: List[int] = list()
        for i in game.players:
            sum = 0
            queens = i.awoken.getQueens()
            if len(queens) >= game.required_queens:
                return True, len(sums_of_points)+1  #the index of player is thesame as the length of the list
            for x in queens:
                if x is not None:
                    sum += x.getPoints()
            sums_of_points.append(sum)
        if max(sums_of_points) >= game.required_points or ended:
            return True, sums_of_points.index(max(sums_of_points))+1
        return False, -1


class GameObserverInterface:
    def addObserver(self, observer: str) -> None:
        pass

    def addPlayer(self, player) -> None:
        pass

    def remove(self, observer) -> None:
        pass

    def getObservers(self)->List[str]:
        return []

    def getPlayers(self)->List[str]:
        return []

    def notifyPlayer(self, idx, message) -> None:
        pass

    def notifyPlayers(self, message) -> None:
        pass

    def notifyAll(self, message) -> None:
        pass


class GameObservable(GameObserverInterface):
    def __init__(self):
        self.players = list()
        self.observers = list()

    def addObserver(self,observer: str) -> None:
        self.observers.append(observer)

    def addPlayer(self, player) -> None:
        if len(self.players) < 5:
            self.observers.append(player)
            self.players.append(player)
            self.notifyAll("Too many players")

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
        self.observable: GameObservable = GameObservable()
        self.game: Game = Game(0)
        self.game_finished: GameFinished = GameFinished()

    def create_game(self):
        self.game = Game(len(self.observable.players))

    def play(self, player: str, cards: str) -> None:
        index_of_player = int(player)-1
        if index_of_player != self.game.state.onTurn:
            self.observable.notifyPlayer(index_of_player, "It is not your turn")
            self.observable.notifyPlayer(index_of_player,"It is not your turn")
            return
        #player = self.game.players[index_of_player-1]
        commands = cards.split()

        def getPositions() -> List[Position]:

            positions: List[Position] = list()
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
                        self.observable.notifyPlayer(index_of_player, "Wrong index of card")
                        return list()
                    pos = HandPosition(index-1, index_of_player)
                    positions.append(pos)
                elif command[0] == "a":
                    index = int(command[2])
                    player_to_attack = int(command[1])-1
                    if player_to_attack > self.game.numofplayers:
                        self.observable.notifyPlayer(index_of_player,"Wrong index")
                        return list()
                    positions.append(AwokenQueenPosition(index-1, player_to_attack))
                elif command[0] == "s":
                    index = int(command[1:])
                    if index > 12:
                        self.observable.notifyPlayer(index_of_player, "There are only 12 queens in the game")
                        return list()

                    else:
                        positions.append(SleepingQueenPosition(index-1))
            return positions

        self.game.play(index_of_player, getPositions())
        if self.game_finished.isFinished(self.game)[0]:
            self.observable.notifyAll(f"The game has ended, winner is player {self.game_finished.isFinished(self.game)[1]}")



