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

def replace_values(card, board, board2):
    print ("The origin coordenate of the board is on the top left corner")
    x = int(input("Please insert coordenate in x: "))
    if x>=0 and x<card:
        y = int(input("Please insert coordenate in y between -1 and 0: "))
        if y == 0 or y ==-1:
            board2[y][x] = board[y][x]
            print (board)
            return (board2)
        else:
            print ("You inserted a coordenate out of range")
    else: 
        print ("You inserted a coordenate out of range")


















Cards = int(input("Please insert the amount of cards you wish to play with: "))

Player1 = 0
Player2 = 0

Board = createMatrix(Cards)
Board2 = createMatrix2(Cards)
print (Board)
print (Board2)
print ("The origin coordenate of the board is on the top left corner")

contador=0
value1 = 0
value2 = 0
#while contador<(Cards*2):
i = 0
while i<2:
    x = int(input("Please insert coordenate in x: "))
    if x>=0 and x<Cards:
        y = int(input("Please insert coordenate in y between -1 and 0: "))
        if y == 0 or y ==-1:
            value1=Board[y][x]
            Board2[y][x] = Board[y][x]
            print(Board2)
            if value1 == 0:
                value1=Board[y][x]
                i+=1
            else:
                value2=Board[y][x]
                i+=1
        else:
            print ("You inserted a coordenate out of range")
    else: 
        print ("You inserted a coordenate out of range")
        
print(value1)
print(value2)      
        
        
        
        
#Replace = replace_values(Cards, Board, Board2)
#print (Replace)
#i+=1
        




    
    



#print (Board)
#print (Board2)
