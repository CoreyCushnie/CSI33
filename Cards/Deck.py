# Deck.py

import random 
from Card import Card
from Hand import Hand
from time import time
  
class Deck(object):

    #------------------------------------------------------------

    def __init__(self):

        """post: Creates a 52 card deck in standard order"""

        cards = []
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                cards.append(Card(rank,suit))
        self.cards = cards
        

    #------------------------------------------------------------

    def size(self):

        """Cards left
        post: Returns the number of cards in self"""
        
        return len(self.cards)

    #------------------------------------------------------------

    def deal(self):

        """Deal a single card
        pre:  self.size() > 0
        post: Returns the next card, and removes it from self.card if
        the deck is not empty, otherwise returns False"""

        if self.size() > 0:
            return self.cards.pop()
        else:
            return False

    #------------------------------------------------------------

    def shuffle(self):

        """Shuffles the deck
        post: randomizes the order of cards in self"""

        random.shuffle(self.cards)        

    def addTop(self, player):
        
        self.cards.append(self.deal())
        player.remove()
    
        
    def addBottom(self):
        
        self.cards.insert(self.deal())
        
    def addRandom(self):
        pass        
'''Times the process and creates an instance of the deck'''

t = time()
D = Deck()
D.size()
e = time()

print(D.size(), e -t)
