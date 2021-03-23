#import numpy as np
import random
import numpy as np
from random import randint, sample


Cards = int(input("Please insert the amount of cards you wish to play with: "))

Player1 = 0
Player2 = 0


def createMatrix(card):
    numbers = range(1,card+1)
    list1 = sample(numbers, k=card)
    list2 = sample(numbers, k=card)
    row1 = np.array(list1)
    row2 = np.array(list2)
    matrix = np.array([row1, row2])
    return matrix


def createMatrix2(card):
    c = 0
    list3 = []
    list4 = []
    while c<card:
        list3.append('#')
        list4.append('#')
        c+=1
    row3 = np.array(list3)
    row4 = np.array(list4)
    matrix2 = np.array([row3, row4])
    return matrix2

Board = createMatrix(Cards)
Board2 = createMatrix2(Cards)

print (Board)
print (Board2)
