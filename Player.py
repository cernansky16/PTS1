# from Hand import Hand
from QueenCollection import AwokenQueens
from GameState_PlayerState import PlayerState
class Player:
    def __init__(self,hand):
        self.hand = hand
        self.state = PlayerState(self.hand.cards,AwokenQueens())
    def __repr__(self):
        return self.hand.getIndex()
    def play(self,cards):
        pass
    def getPlayerState(self):
        return self.state

class EvaluateNumberedCards:
    def play(self,cards):
        only_numbered_cards = []
        for card in cards:
            if card.type == 1:
                only_numbered_cards.append(card)
        only_numbered_cards.sort()
        #vymysliet algoritmus, ktory vyhodnoti, kolko kariet moze clovek vyhodit


