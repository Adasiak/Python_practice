# deque objects are like double-ended queues

import collections
import string
import os
from re import A

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)
clearConsole()

def main():
    
    # TODO: initialize a deque with lowercase letters
    d = collections.deque(string.ascii_letters)
    # TODO: deques support the len() function
    print("Item count: ", str(len(d)))
    # TODO: deques can be iterated over
    for elem in d :
        print(elem.upper(), end=',')
    print()
    # TODO: manipulate items from either end
    d. pop()
    d.popleft()
    d.append(2)
    d.appendleft(1)
    print(d)
    print()
    # TODO: rotate the deque
    d.rotate(10)
    print(d)

if __name__ == "__main__":
    main()
