import random
import numpy as np
from random import randint, sample


Cards = int(input("Please insert the amount of cards you wish to play with: "))


numbers = range(1,Cards+1)
b = sample(numbers, k=Cards)
a = sample(numbers, k=Cards)
#print (b)
#print (a)

arr1 = np.array(b)
arr2 = np.array(a)

#print (arr1)
#print (arr2)

matrix = np.array([arr1, arr2])
print (matrix)