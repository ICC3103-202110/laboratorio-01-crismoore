import random
from random import randint

Nummber_of_cards = input("Please insert the number of cards you wish to play with: ")
cards = int(Nummber_of_cards)
player1 = 0
player2 = 0
tablero = list()

for i in range(cards):
    r1 = random.randint(1,cards)
    r2 = random.randint(1,cards)
    tablero.append(r1)
    tablero.append(r2)

