##Task 6.1
##import math


## Task 6.2
##from random import radint

## 6.3


## 6.4

def makeInverseIndex(strlist):
    """
    >>> makeInverseIndex()
    Cosa
    """
    
    f = open('stories_big.txt')
    for line in f:
        print(line)
    
    for x in [1,2,3]:
        y = x*x
        print(y)
        




def readFile():
    """
    >>> readFile()
    True
    """
    
    f = open('stories_big.txt')
    ##for line in f:
        ##print(line)
    return f is not None

if __name__ == "__main__":
    import doctest
    doctest.testmod()