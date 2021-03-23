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

Board = createMatrix(Cards)

print (Board)