import numpy as np
from random import sample

def Board_showing_all_cards(card):
    numbers = range(1,card+1)
    list_random_numbers = sample(numbers, k=card)
    list_random_numbers2 = sample(numbers, k=card)
    row1 = np.array(list_random_numbers)
    row2 = np.array(list_random_numbers2)
    board = np.array([row1, row2])
    return board

def Board_cards_facing_down(card):
    c = 0
    list3 = []
    list4 = []
    while c<card:
        list3.append('#')
        list4.append('#')
        c+=1
    row3 = np.array(list3)
    row4 = np.array(list4)
    board = np.array([row3, row4])
    return board

print ("\nWelcome to the Memorice game made by Cristobal Moore")
Amount_of_cards = int(input("Please insert the amount of pairs of cards you wish to play with: "))
Board = Board_showing_all_cards(Amount_of_cards)
Board_facing_down = Board_cards_facing_down(Amount_of_cards)
#print (Board,"\n")
print ("\n",Board_facing_down,"\n")
print ("The origin coordenate of the board is on the top left corner \n")
Points_Player1 = 0
Points_Player2 = 0
flag = True
flag2 = True
 
while (Points_Player1+Points_Player2<Amount_of_cards):
    value1x = 0
    value1y = 0
    value2x = 0
    value2y = 0
    while flag == True:
        if (Points_Player1+Points_Player2 == Amount_of_cards):
            break
        else:
            print ("Player 1 make your move ")
            i = 0
            while i<2:
                y = int(input("Please insert coordenate in y between -1 and 0: "))
                if y == 0 or y ==-1:
                    x = int(input("Please insert coordenate in x: "))
                    if x>=0 and x<Amount_of_cards:
                        if flag2 == True:
                            value1x = x
                            value1y = y
                            Board_facing_down[y][x] = Board[y][x]
                            number1 = Board[y][x]
                            print("\n",Board_facing_down)
                            i+=1
                            flag2 = False
                        else: 
                            value2x = x
                            value2y = y
                            Board_facing_down[y][x] = Board[y][x]
                            number2 = Board[y][x]
                            print("\n",Board_facing_down)
                            i+=1
                            flag2 = True
            
            if number1 == number2: 
                print ("\n Nice! You got a point! It's your turn again \n")
                Points_Player1+=1
                Board_facing_down[value1y][value1x] = ' '
                Board_facing_down[value2y][value2x] = ' '    
                print (Board_facing_down, "\n")
            
            else:
                print ("\n Damn the cards are different, other players turn!")
                Board_facing_down[value1y][value1x] = '#'
                Board_facing_down[value2y][value2x] = '#'
                print ("\n",Board_facing_down,"\n")
                flag = False
        
    while flag == False:
        if (Points_Player1+Points_Player2 == Amount_of_cards):
            break
        else:
            print ("Player 2 make your move ")
            i = 0
            while i<2:
                y = int(input("Please insert coordenate in y between -1 and 0: "))
                if y == 0 or y ==-1:
                    x = int(input("Please insert coordenate in x: "))
                    if x>=0 and x<Amount_of_cards:
                        if flag2 == True:
                            value1x = x
                            value1y = y
                            Board_facing_down[y][x] = Board[y][x]
                            number1 = Board[y][x]
                            print("\n",Board_facing_down)
                            i+=1
                            flag2 = False
                            
                        else: 
                            value2x = x
                            value2y = y
                            Board_facing_down[y][x] = Board[y][x]
                            number2 = Board[y][x]
                            print("\n",Board_facing_down)
                            i+=1
                            flag2 = True
            
            if number1 == number2: 
                print ("\n Nice! You got a point! It's your turn again \n")
                Points_Player2+=1
                Board_facing_down[value1y][value1x] = ' '
                Board_facing_down[value2y][value2x] = ' '    
                print (Board_facing_down, "\n")
            else:
                print ("\n Damn the cards are different, other players turn!")
                Board_facing_down[value1y][value1x] = '#'
                Board_facing_down[value2y][value2x] = '#'
                print ("\n",Board_facing_down,"\n")
                flag = True
            
if Points_Player1>Points_Player2:
    print ("Player 1 is the winner! With", Points_Player1, "points! Congratulations! ")
elif Points_Player2>Points_Player1:
    print ("Player 2 is the winner! With", Points_Player2, "points! Congratulations! ")
else:
    print ("It's a tie! No one wins XD" )

   
        