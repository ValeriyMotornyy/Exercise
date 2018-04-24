import random

""" Common """
def swap(array,x,y):
    temp = array[x]
    array[x] = array[y]
    array[y] = temp

def fisherYatesShuffle(array):
    for i in range(len(array)-1,0,-1):
        swap(array,i,random.randint(0,i))

def numberArray():
    array = []
    for x in range(20):
        array.append(random.randint(1,100))
    return array
