# imports
import random
import time
import sys

# functions
def cs():
    print('\033c')
def timeprint(text):
    punctuation = {
    "." : 0.25,
    "!" : 0.15,
    "?" : 0.15,
    "," : 0.05,
    ":" : 0.1
    }
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        if char in punctuation:
            time.sleep(punctuation[char])
        else:
            time.sleep(random.random()/25)
    print()
    time.sleep(0.25)
def intput(text):
    while True:
        try:
            timeprint(text)
            ans = input("> ")
            return int(ans)
        except:
            timeprint("That is not a number. Try again.")
def strput(text):
    timeprint(text)
    ans = input("> ")
    return str(ans)
def line():
    return "-----------------------"
def guesser(numberrange):
    number = random.randint(0,numberrange)
    guess = 0
    guesses = 0
    while True:
        cs()
        guesses += 1
        timeprint("This is guess " + str(guesses) + ".")
        guess = intput("Guess a number between 1 and " + str(numberrange) + ".")
        if guess == number:
            break
        else:
            timeprint(str(guess) + " is incorrect.")
            if number > guess:
                timeprint("Guess higher!")
            else:
                timeprint("Guess lower!")
        print(line())
        time.sleep(1)
    timeprint("Correct! The number was " + str(guess) + ".")
    timeprint("You took " + str(guesses) + " guesses.")
    print(line())
    keep = strput("Do you want to keep going? (y/n)")
    print(line())
    return keep,guesses
# actual program
guessaverage = 0
guesstotal = 0
timesplayed = 0
keepgoing = "y"
cs()
numberrange = intput("What should be the maximum range for the number?")
while keepgoing == 'y':
    keepgoing,guesses = guesser(numberrange)
    guesstotal += guesses
    timesplayed += 1
    guessaverage = guesstotal / timesplayed
    timeprint("Your average guesses to guess the number is " + str(guessaverage) + ".")

