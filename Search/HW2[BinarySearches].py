from time import time

def main():

    numbers = list(range(1000000)) # generate a list of numbers from 0 to 999999

#   Linear Testing....
    start = time()
    a = linear_search(numbers,10)
    end = time()
    print('[Linear Search] Running time...: {} seconds at index: {}'.format(end - start, a))
    
    start = time()
    a = linear_search(numbers,499999)
    end = time()
    
    print('[Linear Search] Running time...: {} seconds at index: {}'.format(end - start, a))
    
    start = time()
    a = linear_search(numbers,999999)
    end = time()
    print('[Linear Search] Running time...: {} seconds at index: {}'.format(end - start, a))
    
    start = time()
    a = linear_search(numbers,10000000)
    end = time()
    print('[Linear Search] Running time...: {} seconds at index: {}'.format(end - start, a))

    start = time()
    a = linear_search(numbers, 7)
    end = time()
    print('[Linear Search] Running time...: {} seconds at index: {}'.format(end - start, a))


    print()

#   Binary Testing....
    start = time()
    a = binary_search(numbers, 10)
    end = time()
    print('[Binary Search] Running time...: {} seconds at index: {}'.format(end - start, a))
    
    start = time()
    a = binary_search(numbers, 499999)
    end = time()
    print('[Binary Search] Running time...: {} seconds at index: {}'.format(end - start, a))

    start = time()
    a = binary_search(numbers, 999329)
    end = time()
    print('[Binary Search] Running time...: {} seconds at index: {}'.format(end - start, a))

    start = time()
    a = binary_search(numbers, 10000000)
    end = time()
    print('[Binary Search] Running time...: {} seconds at index: {}'.format(end - start, a))
    
    start = time()
    a = binary_search(numbers, 17)
    end = time()
    print('[Binary Search] Running time...: {} seconds at index: {}'.format(end - start, a))
    
def linear_search(items,target):
    ''' The inear search loops throught the inputed list arguments and compares one by one to the
        target argument. If the target isn't in the list then the function will return -1'''
 
    for i in items:
        if target == i:     #compares the target and item 
            return items.index(i)       #returns the inputed item
    return -1                   #returns -1 if not found

    
def binary_search(items,target):
    '''The Binary search function takes an inputed list argument and searches the left side of the 
       list and continues to cut the list in half until the target is found. If target is
       not found, then the function also returns -1'''

    sorted(items)   #sorts the list
    
    low = 0
    high = len(items) - 1   #sets the high variable to the length of the list - 1
    while low < high:
        mid = (low + high) // 2     #sum of the low and high divided by 2
        item = items[mid]   #stores the item located in the list at the mid point in the variable item
                            

        if target == item :     #compares variable item with target (Bool)
            return mid
        elif target < item:     #cuts items larger than target in the list
            high = mid - 1
        else:                   #cuts items less than target in the list
            low = mid + 1
    return -1


main()

