from Hand import *
from Deck import *

def main():

  h1 = Hand("south")
  h2 = Hand("north")
  h3 = Hand("east")
  h4 = Hand("west")

  d = Deck()
  d.shuffle()

  # dealing cards in order
  for i in range(13):
    h1.add(d.deal())
    

  # showing the cards
  h1.dump()
  h2.dump()
  h3.dump()
  h4.dump()

  # sorting hards in hand "south" and displaying them
  h1.sort() 
  h1.dump()

  # sorting hards in hand "north" and displaying them
  h2.sort()
  h2.dump()

  # sorting hards in hand "east" and displaying them
  h3.sort()
  h3.dump()

  # sorting hards in hand "west" and displaying them
  h4.sort()
  h4.dump()

main()
