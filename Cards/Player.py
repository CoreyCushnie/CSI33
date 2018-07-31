from Card import *
from Deck import *
from Hand import *

class Main:

    def __init__(self):
        
        p1 = Hand('Player1')
        p2 = Hand('Player2')
        house = Hand('Trump')

        d = Deck()
        d.shuffle()
        
        house.add(d.deal())
        house.dump()
        d.addTop(house)
        for i in range(d.size()):        
            house.add(d.deal())
        
        house.dump()
        
        print(d.size())

        print(d.size())
    

  
n = Main()
        

