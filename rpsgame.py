import random, sys
from traceback import print_tb

print ('Rock, Paper, Scissors')

wins = 0
loss = 0
ties = 0


while True:
    print ('%s Wins, %s Losses, %s Ties' % (wins, loss, ties))
    while True:
        print('Enter your move, Rock(r), Paper(p), Scissors(s) or Quit(q)')
        playermove = input()
        if playermove == 'q':
            sys.exit() #Exit the program
        if playermove == 'r' or playermove == 'p' or playermove == 's':
            break #Break out of the loop.
        print ('Type one of r, p, s or q')

    if playermove == 'r':
        print ('Rock vs ......')
    if playermove == 'p':
        print ('Paper vs ......')
    if playermove == 's':
        print ('Scissors vs ......')

    #Display what the computer chose
    randomNumber = random.randint(1,3)

    if randomNumber == 1:
        ComputerMove = 'r'
        print ('ROCK')
    if randomNumber == 2:
        ComputerMove = 'p'
        print ('PAPER')
    if randomNumber == 3:
        ComputerMove = 's'
        print ('SCISSORS')

    #Display and record the win loss and tie
    if playermove == ComputerMove:
        print ("It is a tie!")
        ties+=1
    elif playermove == 'r' and ComputerMove == 'p':
        print ("You win!")
        ties+=1
    elif playermove == 'p' and ComputerMove == 'r':
        print('You win!')
        wins = wins + 1
    elif playermove == 's' and ComputerMove == 'p':
        print('You win!')
        wins = wins + 1
    elif playermove == 'r' and ComputerMove == 'p':
        print('You lose!')
        loss = loss + 1
    elif playermove == 'p' and ComputerMove == 's':
        print('You lose!')
        loss = loss + 1
    elif playermove == 's' and ComputerMove == 'r':
        print('You lose!')
        loss = loss + 1