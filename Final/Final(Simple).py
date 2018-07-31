alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

class ListNode:
    
    def __init__(self, item=None, left=None, mid=None, right=None):
        
        self.item = item
        self.left = left
        self.mid = mid
        self.right = right

class triTree:

    def __init__(self, size = None):
        self.size = size
        self.node = ListNode()

    def shuff(self, a):
        for i in range(len(a)):
            yield i
        
    def tree(self):
        
        size = self.size
     
        
        for a in range(size):        
            node = self.node
            left = node.left
            mid = node.mid
            right = node.right

            for char in alpha[:size]:
                
                                    
                node.left = ListNode(char + alpha[a])
                left = node.left
                   
                    
                node.mid = ListNode(char + alpha[a])
                mid = node.mid
                
                
                node.right = ListNode(char + alpha[a])
                right = node.right
                       
                print(left.item, mid.item, right.item)
                            
            
    
g = triTree(3)
g.tree()

