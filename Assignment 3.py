# Task 1

def factorial(x):
    if x<=1:
        return 1
    else:
        return x*factorial(x-1)
x=int(input('Enter a number: '))
print('\nfactorial of', x, 'is:', factorial(x))

# Task 2

n=float(input('\nEnter a number: '))
from math import *

print('\nSquare root:',sqrt(n))
print('logarithm:',log(n))
print('sine:',sin(n))