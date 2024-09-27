# imports
import random
import time
import sys

# functions
def cs(moneys):
    print('\033c')
    print("You have $" + str(moneys) + ".")
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
#start
class Card:
    def __init__(self,name,value):
        self.name = name
        self.value = value
    def __repr__(self):
        return(self.name)
class Deck:
    def __init__(self):
        deck = []
        deck.append(Card("Ace of hearts","ace"))
        for i in range(9):
            val = i + 2
            deck.append(Card(str(val) + " of hearts",val))
        deck.append(Card("Jack of hearts",10))
        deck.append(Card("Queen of hearts",10))
        deck.append(Card("King of hearts",10))
        deck.append(Card("Ace of diamonds","ace"))
        for i in range(9):
            val = i + 2
            deck.append(Card(str(val) + " of diamonds",val))
        deck.append(Card("Jack of diamonds",10))
        deck.append(Card("Queen of diamonds",10))
        deck.append(Card("King of diamonds",10))
        deck.append(Card("Ace of spades","ace"))
        for i in range(9):
            val = i + 2
            deck.append(Card(str(val) + " of spades",val))
        deck.append(Card("Jack of spades",10))
        deck.append(Card("Queen of spades",10))
        deck.append(Card("King of spades",10))
        deck.append(Card("Ace of clubs","ace"))
        for i in range(9):
            val = i + 2
            deck.append(Card(str(val) + " of clubs",val))
        deck.append(Card("Jack of clubs",10))
        deck.append(Card("Queen of clubs",10))
        deck.append(Card("King of clubs",10))
        self.cards = deck
    def shuffle(self):
        random.shuffle(self.cards)
    def __repr__(self):
        return str(self.cards)
moneys = 1000
while True:
    bet = -1
    deck = Deck()
    deck.shuffle()
    playerhand = []
    dealerhand = []
    game = True
    while bet > moneys or bet < 25:
        cs(moneys)
        bet = intput("How much would you like to bet? Minimum of $25.")
        if bet > moneys:
            timeprint("You don't have enough money!")
        elif bet < 25:
            timeprint("You can't bet that little.")
    moneys -= bet
    cs(moneys)
    timeprint("You bet " + str(bet) + " dollars.")
    while game:
        cs(moneys)
        print("The stake for this game is $" + str(bet) + ".")
        dealerhand.append(deck.cards.pop(0))
        for i in range(2):
            playerhand.append(deck.cards.pop(0))
        timeprint("The dealer dealt himself one card.")
        timeprint("The dealer dealt you two cards.")
        timeprint("The dealer has:")
        dpoints = 0
        daces = 0
        for i in dealerhand:
            timeprint(i)
            if i.value != "ace":
                dpoints += i.value
            else:
                daces += 1
        timeprint("You have:")
        ppoints = 0
        paces = 0
        for i in playerhand:
            timeprint(i)
            if i.value != "ace":
                ppoints += i.value
            else:
                paces += 1