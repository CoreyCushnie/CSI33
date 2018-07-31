from time import time
from random import randrange

def main():
    test = []
    
    while len(test) <= 10000000:
        l = randrange(10000000)
        test.append(l) 

    start = time()
    sL(test)
    end = time()
    t = end - start
    
    print(t)


    
'''
    start = time()
    sL(test)
    end = time()
    t = end - start
    
    print(t)

    start = time()
    sL(test)
    end = time()
    t = end - start
    
    print(t)

    start = time()
    sL(test)
    end = time()
    t = end - start
    
    print(t)
'''

def sL(items):
    

    for i in range(len(items) -1):
        small = i
        for j in range(i+1, len(items)):
            if items[j]< items[small]:
                small = j
        if small != i:
            items[i], items[small] = items[small], items[i]

    
        
    
            
        
    
main()
