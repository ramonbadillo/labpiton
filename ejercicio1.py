def minutesInWeek():
	"""
	>>> minutesInWeek()
	10080
	"""
	return 24*60*7

def div(x,y):
	"""
	>>> div(2304811,47)
	25
	"""

	return x-((x//y)*y)

def num(x,y):
	"""
	>>> num(673,909)
	False
	"""
	return (x+y)%3==0

def valor(x,y):
	"""
	>>> valor(-9,1/2)
	1.0
	"""
	return 2**(y+1/2) if x+10<0 else 2**(y-1/2)

def cuadrados(set):
	"""
	>>> cuadrados({1,2,3,4,5})
	{16, 1, 9, 25, 4}
	"""
	return {x*x for x in set}

def potencia(set):
	"""
	>>> potencia({0,1,2,3,4})
	{8, 1, 2, 16, 4}
	"""
	return {2**x for x in set}

def setnueve(set1, set2):
	"""
	>>> setnueve({1,7,11}, {2,3,4} )
	{33, 2, 3, 4, 44, 14, 21, 22, 28}
	"""
	return {x*y for x in set1 for y in set2}

def setcinco(set1, set2):
	"""
	>>> setcinco({2,4,8}, {16,32,64} )
	{512, 256, 128, 64, 32}
	"""
	return {x*y for x in set1 for y in set2}

def inter(set1, set2):
	"""
	>>> inter({1,2,3,4}, {3,4,5,6} )
	{3, 4}
	"""
	return {x for x in set1 for y in set2 if x==y}
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

def prom(list):
	"""
	>>> prom([20,10,15,75])
	30.0
	"""
	return sum(list)/len(list)

def posible(list1, list2):
	"""
	>>> posible(['A','B','C'], [1,2,3] )
	[['A', 1], ['A', 2], ['A', 3], ['B', 1], ['B', 2], ['B', 3], ['C', 1], ['C', 2], ['C', 3]]
	"""
	return [[x,y] for x in list1 for y in list2]

def sumal(list):
	"""
	>>> sumal([[.25, .75, .1],[-1, 0], [4, 4, 4, 4]])
	16.1
	"""
	return sum(sum(x) for x in list)

'''def fallo(x,y):
	"""
	>>> fallo([x,y],[4,2,3])
	true
	"""
	return [x,y]=[4,2,3]
	'''
def ent(set):
	"""
	>>> ent({-4,-2,-1,2,5,0})
	[(0, 0, 0), (0, 2, -2), (0, -2, 2), (2, 0, -2), (2, 2, -4), (2, -4, 2), (2, -1, -1), (2, -2, 0), (5, -4, -1), (5, -1, -4), (-4, 2, 2), (-4, 5, -1), (-4, -1, 5), (-1, 2, -1), (-1, 5, -4), (-1, -4, 5), (-1, -1, 2), (-2, 0, 2), (-2, 2, 0)]
	"""
	return [(x,y,z) for x in set for y in set for z in set if x+y+z==0]

def ent2(set):
	"""
	>>> ent2({-4,-2,-1,2,5,0})
	[(0, 2, -2), (0, -2, 2), (2, 0, -2), (2, 2, -4), (2, -4, 2), (2, -1, -1), (2, -2, 0), (5, -4, -1), (5, -1, -4), (-4, 2, 2), (-4, 5, -1), (-4, -1, 5), (-1, 2, -1), (-1, 5, -4), (-1, -4, 5), (-1, -1, 2), (-2, 0, 2), (-2, 2, 0)]
	"""
	return [(x,y,z) for x in set for y in set for z in set if x+y+z==0 and (x,y,z) != (0,0,0)]

def tupla(set):
	"""
	>>> tupla({-4,-2,-1,2,5,0})
	[(0, 0, 0)]
	"""
	return [(x,y,z) for x in set for y in set for z in set if x+y+z==0 and (x,y,z) == (0,0,0)]

def listSet(lista):
	"""
	>>> listSet([1,2,2,3])
	False
	"""
	return len(lista) == len(list(set(lista)))

def rango(x):
	"""
	>>> rango(100)
	[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99]
	"""
	li = list(range(100))
	return li[1::2]

def combo(lista):
	"""
	>>> combo(['A','B','C','D','E'])
	[(0, 'A'), (1, 'B'), (2, 'C'), (3, 'D'), (4, 'E')]
	"""
	return [(lista.index(x),x) for x in lista]




def combo2(lista,lista1):
	"""
	>>> combo2([10,25,40],[1,15,20])
	[(10, 1), (25, 15), (40, 20)]
	"""
	return list(zip(lista, lista1))

def el21(lista):
	"""
	>>> el21([{'James':'Sean','director':'Terence'}, {'James':'Roger', 'director':'Lewis'}, {'James':'Pierce','director':'Roger'}])
	['Sean', 'Roger', 'Pierce']
	"""
	k='James'
	return [lista[x][k] for x in range(len(lista))]

def el23(n):
	"""
	>>> el23(99)
	{0:0.00, }
	"""
	import math
	return {x:round(math.sqrt(x),2) for x in range(n)}

def el28(Lista):
	"""
	>>> el28([1,5,7])
	[2, 6, 8]
	"""
	return [x+1 for x in Lista]



def el29(Lista):
	"""
	>>> el29([1,2,3])
	[1, 8, 27]
	"""
	return [x**Lista[len(Lista)-1] for x in Lista]

def el30():
	"""
	>>> el30()
	
	"""
	import math



if __name__ == "__main__":
    import doctest
    doctest.testmod()