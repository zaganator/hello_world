# esercizio nove
# Guessing Game One

# dall'indirizzo:
# http://www.practicepython.org/exercise/2014/04/02/09-guessing-game-one.html

# Generate a random number between 1 and 9 (including 1 and 9).
# Ask the user to guess the number, then tell them whether
# they guessed too low, too high, or exactly right.
# (Hint: remember to use the user input lessons from the very first exercise)

# Extras:
#    Keep the game going until the user types “exit”
#    Keep track of how many guesses the user has taken, and when the game ends,
#    print this out.

import random
x = random.randint(1,9)
answer = 0
counter = 0
while answer != x:
    counter += 1
    answer = int(input('prova ad indovinare un numero tra 1 e 9\ninserisci:\n'))
    if answer < x:
        print('Basso...')
    elif answer > x:
        print('Alto...')
    else:
        print('right')
        print('ci hai messo {} volte ad indovinare'.format(counter))
        break
        
        
