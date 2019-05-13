#   Reverse Word Order strings
# Exercise 15 (and Solution)

# all'indirizzo:
# http://www.practicepython.org/exercise/2014/05/21/15-reverse-word-order.html

# Write a program (using functions!) that asks the user for a long string
# containing multiple words. Print back to the user the same string,
# except with the words in backwards order.
# For example, say I type the string:

# "My name is Michele"

# Then I would see the string:

# "Michele is name My"

# shown back to me.

frase2 = "annalisa e alisea sono figlie mie"
frase1 = "antonella è bellissima"
frase = "porca miseria ma forse ci sono riuscito"
print ("di seguito le frasi prese in esame da rovesciare\n", frase, "\n", frase1, "\n", frase2, "\n")

# in questa prima funzione si ottiene il rovesciamento della frase/parola
def reverser(string):
    reversed = [string[::-1]]
    return reversed

# in questa seconda funzione si divide la frase grazie a ".split" che senza
# indicazioni tra le parentesi splitta la frase con gli spazi, quindi si
# richiama la prima funzione e si rovescia la frase.
def string_reverser(frase,func):
    frase = frase.split()
    return (func(frase))

print (string_reverser(frase,reverser))
print (string_reverser(frase1,reverser))
print (string_reverser(frase2,reverser))

print ('di seguito le frasi capovolte senza la funzione ".split"\n','\n', reverser(frase), '\n', reverser(frase1), '\n', reverser(frase2))
