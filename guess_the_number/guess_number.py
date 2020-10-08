# This is a guess the number game

import random

print('Hello, what is your name?')
name = input()
print('Well, ' + name + ', I am thinking of a number between 1 and 20.')

secretNumber = random.randint(1,20)
#Ask the player to guess six times

for guessesTaken in range(1,7):
    
    print('Take a guess.')
    
    try:
        guess = int(input())
    except ValuError:
        print('You must enter an integer.')

    if guess < secretNumber:
        print('Your guess is too low.')
    elif guess > secretNumber:
        print('Your guess is too high.')
    else: 
        break #If it's neither greater nor lower, it's a correct guess. 

if guess == secretNumber:
    print('Correct! Good guessing, ' + name + '. You took ' + str(guessesTaken) + ' guesses.')
else:
    print('That was incorrect. You took ' + str(guessesTaken) + ' guesses. The number I was thinking of was ' + str(secretNumber) + '.')
