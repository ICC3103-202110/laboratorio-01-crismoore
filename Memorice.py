#import numpy as np
import random
import numpy as np
from random import randint, sample

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

def replace_values(card):
    print ("The origin coordenate of the board is on the top left corner")
    x = int(input("Please insert coordenate in x: "))
    if x>=0 and x<card:
        y = int(input("Please insert coordenate in y between -1 and 0: "))
        if y == 0 or y ==-1:
            Board = createMatrix(Cards)
            Board2 = createMatrix2(Cards)
            Board2[y][x] = Board[y][x]
            print (Board)
            return (Board2)
        else:
            print ("You inserted the wrong coordenate")
            

Cards = int(input("Please insert the amount of cards you wish to play with: "))

Player1 = 0
Player2 = 0

Replace = replace_values(Cards)

print (Replace)


#print (Board)
#print (Board2)
