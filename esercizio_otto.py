# esercizio otto
# all'indirizzo:ù
# http://www.practicepython.org/exercise/2014/03/26/08-rock-paper-scissors.html
# Rock Paper Scissors

# Make a two-player Rock-Paper-Scissors game.
# (Hint: Ask for player plays (using input), compare them,
# print out a message of congratulations to the winner,
# and ask if the players want to start a new game)

# Remember the rules:

#    Rock beats scissors
#    Scissors beats paper
#    Paper beats rock
p1 = ''
p2 = ''

def winner(p1, p2):
    yes_no = 'yes'
    while yes_no == 'yes':

        p1 = input ('carta forbice o sasso\n'); print ("\n" * 1000)
        p2 = input ('carta forbice o sasso\n'); print ("\n" * 1000)

        c = 'carta'
        s = 'sasso'
        f = 'forbice'
        win1 = 'p1 win!! congratulation\n'
        win2 = 'p2 win!! congratulation\n'
        no_win = 'no one win!!'
        if p1 == s and p2 == c:
            print (win2)
        elif p1 == s and p2 == f:
            print (win1)
        elif p1 == s and p2 == s:
            print (no_win)
        elif p1 == f and p2 == s:
            print (win2)
        elif p1 == f and p2 == c:
            print (win1)
        elif p1 == f and p2 == f:
            print (no_win)
        elif p1 == c and p2 == s:
            print (win1)
        elif p1 == c and p2 == f:
            print (win2)
        elif p1 == c and p2 == c or p1 == '' and p2 == '':
            print (no_win)
        yes_no = input('''giochiamo ancora?
yes
no
scrivi uno dei due!\n''')

winner(p1, p2)
    
