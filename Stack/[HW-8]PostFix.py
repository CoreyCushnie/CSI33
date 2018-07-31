from Stack import *

test = '345+*2-36*+'
test2 = '543+2/+'

def postfix(target):
    
    # Initializes stack
    stack = Stack()

    # Loops through the target 
    for i in target:
        
        # Checks if anything in the target matches a math operator
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
            
            # Pushes the numbers into the stack list
            stack.push(i)
            
    # Prints the results to the console.
    return print(stack.top())

# Tests           
postfix(test)
postfix(test2)


"TRUE FALSE {181 1-4}"
'''
        1-False
        2-True
        3-True
        4-True
'''
"TRUE FALSE {182 1-5}"
'''
        1-B
        2-B
        3-B..?
        4-D
        5-A..?
'''
