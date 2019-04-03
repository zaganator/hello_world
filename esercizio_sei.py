# esercizio sei
# String Lists
# strings lists index

# Ask the user for a string and print out whether this string
# is a palindrome or not. (A palindrome is a string that reads
# the same forwards and backwards.)

word = input('inserisci una parola:\n')

def reverse_word (x):
    a = x[::-1]
    print(a)
    return a

reverse = reverse_word(word)

if word == reverse:
    print("palindromo")
else:
    print("diverse")


