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

def find(Value1, board, board2):
    found = np.argwhere(board==Value1)
    l = []
    for i in found:
        l.append(i)

   
#def replace_values(x, board22):
    

Cards = int(input("Please insert the amount of pairs of cards you wish to play with: "))
Board = createMatrix(Cards)
Board2 = createMatrix2(Cards)
print (" ")
print (Board)
print (" ")
print (Board2)
print (" ")
print ("The origin coordenate of the board is on the top left corner ")
print (" ")
Player1 = 0
Player2 = 0


flag = True
flag2 = True

while (Player1+Player2<=Cards):
    value1x = -10
    value1y = -10
    value2x = -10
    value2y = -10
    cont = 0
    print ("Player 1 make your move ")
    while flag == True:
        i = 0
        while i<2:
            y = int(input("Please insert coordenate in y between -1 and 0: "))
            if y == 0 or y ==-1:
                x = int(input("Please insert coordenate in x: "))
                print (" ")
                if x>=0 and x<Cards:
                    if flag2 == True:
                        value1x = x
                        value1y = y
                        Board2[y][x] = Board[y][x]
                        number1 = Board[y][x]
                        print (value1y, value1x)
                        print(Board2)
                        print(" ")
                        i+=1
                        flag2 = False
                                                
                    else: 
                        value2x = x
                        value2y = y
                        Board2[y][x] = Board[y][x]
                        number2 = Board[y][x]
                        print (value1y, value1x)
                        print(Board2)
                        print(" ")
                        i+=1
                        flag2 = True
          
        if number1 == number2: 
            print ("Nice! You got a point! It's your turn again ")
            print (" ")
            Player1+=1
            Board2[value1y][value1x] = ' '
            Board2[value2y][value2x] = ' '    
            print (Board2)
            print (value1y, value1x)
            print (value2y, value2x)
            print (" ")
            
        else:
            Board2[value1y][value1x] = '#'
            Board2[value2y][value2x] = '#'
            print (Board2)
            print (value1y, value1x)
            print (value2y, value2x)
            print (" ")
            flag = False
        
    print ("Player 2 make your move ")
    while flag == False:
        i = 0
        while i<2:
            y = int(input("Please insert coordenate in y between -1 and 0: "))
            if y == 0 or y ==-1:
                x = int(input("Please insert coordenate in x: "))
                print (" ")
                if x>=0 and x<Cards:
                    if flag2 == True:
                        value1x = x
                        value1y = y
                        Board2[y][x] = Board[y][x]
                        number1 = Board[y][x]
                        print (value1y, value1x)
                        print(Board2)
                        print (" ")
                        i+=1
                        flag2 = False
                        
                    else: 
                        value2x = x
                        value2y = y
                        Board2[y][x] = Board[y][x]
                        number2 = Board[y][x]
                        print (value1y, value1x)
                        print(Board2)
                        print (" ")
                        i+=1
                        flag2 = True
          
        if number1 == number2: 
            print ("Nice! You got a point! It's your turn again ")
            print (" ")
            Player1+=1
            Board2[value1y][value1x] = ' '
            Board2[value2y][value2x] = ' '    
            print (value1y, value1x)
            print (Board2)
            print (" ")
            
        else:
            Board2[value1y][value1x] = '#'
            Board2[value2y][value2x] = '#'
            print (value1y, value1x)
            print (value2y, value2x)
            print (Board2)
            print (" ")
            flag = True
            
if Player1>Player2:
    print ("Player 1 is the winner! Congratulations! ")
elif Player2>Player1:
    print ("Player 2 is the winner! Congratulations! ")
else:
    print ("It's a tie! No one wins XD" )

"""
        print("Player 2 make your move: ")
        y = int(input("Please insert coordenate in y between -1 and 0: "))
        if y == 0 or y ==-1:
            x = int(input("Please insert coordenate in x: "))
            if x>=0 and x<Cards:
                if value1x == -2 & value1y == -2:
                    value1x = x
                    value1y = y
                    Board2[y][x] = Board[y][x]
                    number1 = Board[y][x]
                    print(Board2)
                    i+=1
                else: 
                    value2x = x
                    value2y = y
                    Board2[y][x] = Board[y][x]
                    number2 = Board[y][x]
                    print(Board2)
                    i+=1
            else:
                print ("You inserted a coordenate out of range")
        else: 
            print ("You inserted a coordenate out of range")
    break 
"""        
        
#if value1 == value2:
#    f = find(value1,Board,Board2)
   
        