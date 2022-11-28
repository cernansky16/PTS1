from typing import Union

class SleepingQueenPosition:
    def getCardIndex(self): int

class AwokenQueenPosition:
    def getCardIndex(self): int

    def getPlayerIndex(self):int

class HandPosition:
    def getCardIndex(self): int

    def getPlayerIndex(self): int

class Position:
    position: Union[SleepingQueenPosition,AwokenQueenPosition,HandPosition]


