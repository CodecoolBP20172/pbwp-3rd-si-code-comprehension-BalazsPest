"""It is a guessing game, the player has 6 chance to get the right number,
the program helps the user with higher and lower guidance"""

import random #import random module

guessesTaken = 0 #variable with the value 0

print('Hello! What is your name?') # printed text
myName = input()  # myName variable calls user input

number = random.randint(1, 20) # number variable gets a number between 1 and 20
print('Well, ' + myName + ', I am thinking of a number between 1 and 20.') # printed text contains myName user input

while guessesTaken < 6:   # a cycle that repeats itself until guesstaken is less than 6
    print('Take a guess.') # printed text
    guess = input() # guess variable calls user input
    guess = int(guess) #  guess converted to integer

    guessesTaken += 1 # guess value plus 1

    if guess < number: # if guess input is lower than number value
        print('Your guess is too low.') #printed text

    if guess > number: # if guess input is higher than number value
        print('Your guess is too high.') #printed text

    if guess == number: # if the user input equals the random number:
        break # breaks the loop

if guess == number: # if the user input equals the random number:
    guessesTaken = str(guessesTaken) #  guessTaken converted to string
    print('Good job, ' + myName + '! You guessed my number in ' + guessesTaken + ' guesses!') #printed text with "myName" and "guessesTaken" values

if guess != number: #if the user input isn't the random calculatad number
    number = str(number) # number converted to string
    print('Nope. The number I was thinking of was ' + number) # printed out text with "number" variable
