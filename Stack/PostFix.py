from Stack import *

test = '345+*2-36*+'
test2 = '543+2/+'

def postfix(target):
    total = 0
    stack = Stack()
    for i in target:
        if i == "+":
            f = stack.pop()
            s = stack.pop()
            stack.push(int(s) + int(f))
            
        elif i == "*":
            f = stack.pop()
            s = stack.pop()
            stack.push(int(s) * int(f))
            
        elif i == "-":
            f = stack.pop()
            s = stack.pop()
            stack.push(int(s) - int(f))
        elif i == "/":
            f = stack.pop()
            s = stack.pop()
            stack.push(int(s) / int(f))
           
        else:
            stack.push(i)
            
    return print(stack.top())
            
            

postfix(test)
postfix(test2)

