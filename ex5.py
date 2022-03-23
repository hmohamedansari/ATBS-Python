import random

secretnumber = random.randint(1, 20)

for guessesTaken in range(1, 7):
    print ('Take a guess.')
    guess = int(input())

    if guess < secretnumber:
        print('Your guess too low')
    elif guess > secretnumber:
        print ('Your guess is too high')
    else:
        break

if guess == secretnumber:
    print ('Good Job, you guessed my number in ' +str(guessesTaken) + ' guesses.')
else:
    print ('Nope, The number I was thinking of was ' + str(secretnumber) + '.')