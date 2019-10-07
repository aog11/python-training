# Chapter 10
# Debuggin Coin Toss project

import random
guess = ''
while guess not in ('heads', 'tails'):
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()
toss = random.randint(0, 1) # 0 is tails, 1 is heads
# Bug 1, its equating a number with a string
# Adding the conversion of guess
if guess == 'heads':
    guess = 1
else:
    guess = 0
if toss == guess:
    print('You got it!')
else:
    print('Nope! Guess again!')
    # Bug 2, The guess is saved in a variable named guesss
    # Reusing the guess variable and adding the conversion
    guess = input()
    if guess == 'heads':
        guess = 1
    else:
        guess = 0    
    if toss == guess:
       print('You got it!')
    else:
        print('Nope. You are really bad at this game.')