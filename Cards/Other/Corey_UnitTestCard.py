import sys
import unittest

from Card import *

class RankTest(unittest.TestCase):
  """ Tests Rank methods: rank() and rankName() """
  
  def testRanks(self): # unit test for ranks 1-13
    """ creates cards of rank 1 through 13 of clubs and
    verifies that the created card's rank is equal to the
    rank it was created with """
    
    for i in range(2,15):
      myCard = Card(i,'c') # create i of clubs
      self.assertEqual(myCard.rank(),i) # verifies that the card's rank is i

  def testRankName(self): # unit test for rank names, 'ace', 'two', 'three',...
    """ creates cards with rank names "ace", ...
    and then checks for equivalency: card's rank name, by calling method rankName,
    and the rank name that was given to the card"""
    
    for i in range(2,15):    
        myCard = Card(i, 's')  # creates the cards 
        self.assertEqual(myCard.rankName(), Card.RANK_NAMES[i-2])       # by adding 2 to the index of RANK_NAMES
                                                                        # and assigns it to myCard.
class SuitTest(unittest.TestCase):
  """ Tests Suit methods: suit() and suitName() """
    
  def testSuits(self): # unit test for suits, 'c', 'd', 'h', 's'
    """ creates cards of rank ...  of c (clubs), d (diamonds),
    h(hearts) and s (spades), and verifies that the created card's suit
    is equal to the suit it was created with (c,d,h,s) """
    
    for suit in Card.SUITS:
        myCard = Card(range(2,15), suit)
        self.assertEqual(myCard.suit(), suit)
    
  def testSuitName(self): # unit test for suit names, 'clubs', 'diamonds',...
    """ creates cards with all the suit names ...
    and then checks for equivalency: card's suit name, by calling method suitName,
    and the suit name that was given to the card"""
    
     # creates all the cards with all the suits
    for suit in Card.SUITS:
        myCard = Card(range(2,15), suit)
        self.assertEqual(myCard.suitName(),Card.SUIT_NAMES[Card.SUITS.index(suit)])
              
def main(argv):
  unittest.main()

if __name__ == '__main__':
  main(sys.argv)
