from typing import Union

class SleepingQueenPosition:
    def __init__(self,cardIndex):
        self.cardIndex = cardIndex
    def getCardIndex(self) -> int :
        return self.cardIndex
class AwokenQueenPosition:
    def __init__(self,cardIndex,playerIndex):
        self.cardIndex = cardIndex
        self.playerIndex = playerIndex
    def getCardIndex(self) -> int:
        return self.cardIndex
    def getPlayerIndex(self) -> int:
        return self.playerIndex

class HandPosition:
    def __init__(self,card, player):
        self.cardIndex = card
        self.playerIndex = player
    def getCardIndex(self):
        return self.cardIndex
    def getPlayerIndex(self):
        return self.playerIndex

class Position:
    def __init__(self,position:Union[SleepingQueenPosition,AwokenQueenPosition,HandPosition]):
        self.position = position

    def getCardIndex(self) -> int:
        return self.position.getCardIndex()
    def getPlayerIndex(self) -> int:
        return self.position.getPlayerIndex()


