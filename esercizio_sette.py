# esercizio sette
# List Comprehensions
# dal sito:
# http://www.practicepython.org/exercise/2014/03/19/07-list-comprehensions.html
#
# Let’s say I give you a list saved in a variable:
# a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100].
# Write one line of Python that takes this list "a"
# and makes a new list that has only the even
# elements of this list in it.

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

even = []
for num in a:
    if num % 2== 0:
        even.append(num)
print (even)

# to compact the list u must identify  first of all
# what u are seeking in this case "num"
even = [num for num in a if num % 2 == 0]
five = [num for num in a if num % 5 == 0]
more_then = [num for num in a if num > 8]
five_to_ten = [n for n in range(5,11) if n % 2 == 0]
print (five_to_ten)
print (even)
print (five)
print (more_then)
