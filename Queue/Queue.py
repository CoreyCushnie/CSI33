#!/usr/bin/env python
# Queue.py
# Dave Reed
# CS161
# 02/24/2006

#----------------------------------------------------------------------

class Queue:

    #----------------------------------------------------------------------
    
    def __init__(self):

        '''create an empty FIFO queue'''
        
        self.q = []

    #----------------------------------------------------------------------

    def size(self):

        '''return number of items in the queue

        pre: none
        
        post: returns number of items in the queue'''
        
        return len(self.q)

    #----------------------------------------------------------------------

    def enqueue(self, x):

        '''insert x at end of queue

        pre: none

        post: x is added to the queue'''
        
        self.q.append(x)

    #----------------------------------------------------------------------

    def front(self):

        '''return first item in queue

        pre: queue is not empty; IndexError is raised if empty

        post: returns first item in the queue'''

        return self.q[0]

    #----------------------------------------------------------------------

    def dequeue(self):

        '''remove and return first item in queue

        pre: queue is not empty; IndexError is raised if empty

        post: removes and returns first item in the queue'''
        
        return self.q.pop(0)

    def queueInOrder(self):
        for i in range(self.size() - 1):
            if self.q[i] > self.q[i+1]:
                return False
        
                
        return True

#----------------------------------------------------------------------


f = Queue()
c = Queue()
f.enqueue(3)
f.enqueue(45)
f.enqueue(1)
f.enqueue(23)
f.enqueue(11)

c.enqueue(1)
c.enqueue(2)
c.enqueue(3)
c.enqueue(4)
c.enqueue(5)

print(f.size())
print(f.queueInOrder())
print(c.queueInOrder())

