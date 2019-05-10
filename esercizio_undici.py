# Exercise 11 (and Solution)

# http://www.practicepython.org/exercise/2014/04/16/11-check-primality-functions.html

# Ask the user for a number and determine whether the number is prime or not.
# (For those who have forgotten, a prime number is a number that has no
# divisors.). You can (and should!) use your answer to Exercise 4 to help you.
# Take this opportunity to practice using functions, described below.

# Discussion

# Concepts for this week:

#    Functions
#    Reusable functions
#    Default arguments

def prime(num):
    if num == 1:
        print("uno non fa parte dei numeri primi")
    elif num == 2:
        print("e' due... quindi primo")
    elif num == 3:
        print("e' tre quindi primo")
    elif num % 2 == 0:
        print("{} e' pari quindi non primo".format(num))
    elif num % 2 != 0:
        divisori = ""
        for x in range(2, num):
            if num % x == 0:
                divisori = divisori + " " + str(x)
        if len(divisori) == 0:
            print ("primo")
        else:
            print ("{} non e' primo si divide per {}".format(num, divisori))
    else:
        print("primo")

num = int(input("...e' primo o no?\ninserisci un numero da testare:\n"))
prime(num)
