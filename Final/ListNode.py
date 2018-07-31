# ListNode2.py

class ListNode2:
    
    def __init__(self, item = None, leftL = None, rightL = None):

        '''creates a ListNode with the specified data value and
           two links: to the previous node and to the next node
        post: creates a ListNode with the specified data value and links'''
        
        self.item = item
        self.leftL = leftL
        self.rightL = rightL

    def __str__(self):
      ''' for printing the node '''
      
      return str(self.item)

def printLR(headNode):
    """ prints all elements following right links, starting with the headNode """
    node = headNode
    
    while node is not None:
        print(node.item, end = "\t")
        node = node.rightL

    print("end of linked list")

def printRL(tailNode):
    """ generates a list all elements following left links,
    starting with the tailNode """
    
    node = tailNode
    listV = []
    
    while node is not None:
        listV.append(node.item)
        node = node.leftL
    
    listV = listV[::-1]
    print("here is the list of elements, following left links:",listV)

    return listV           
