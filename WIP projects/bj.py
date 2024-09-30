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
    def printable(self):
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
yn = strput("Do you know how to play? (y/n)")
if yn != "y":
    timeprint("You are trying to get as close to 21 as possible, without going over 21.")
    timeprint("Face cards are worth 10.")
    timeprint("Aces are worth either 11 or 1, depending on whether or not that would go over 21.")
    timeprint("The dealer will draw after you are done, and also try to get close to 21.")
    timeprint("It will only stop when it will win, or is over 21.")
    timeprint("If you win with exactly 21, you get 1.5 times your bet.")
    strput("Press enter to continue.")
while True:
    bet = -1
    deck = Deck()
    deck.shuffle()
    playerhand = []
    dealerhand = []
    game = True
    turn = True
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
        for i in range(len(dealerhand)):
            card = dealerhand[i]
            timeprint(card.printable())
            if card.value != "ace":
                dpoints += card.value
            else:
                daces += 1
        for i in range(daces):
            if dpoints > 11 - daces:
                dpoints += 1
            else:
                dpoints += 11
        timeprint("This adds up to " + str(dpoints) + " points.")
        timeprint("You have:")
        ppoints = 0
        paces = 0
        for i in range(len(playerhand)):
            card = playerhand[i]
            timeprint(card.printable())
            if card.value != "ace":
                ppoints += card.value
            else:
                paces += 1
        for i in range(paces):
            if ppoints > 11 - paces:
                ppoints += 1
            else:
                ppoints += 11
        timeprint("This adds up to " + str(ppoints) + " points.")
        while turn:
            if ppoints > 21:
                turn = False
            else:
                action = strput("Do you want to draw another card? (y/n)")
                if action != "y":
                    turn = False
                else:
                    timeprint("You drew a " + deck.cards[0].printable() + ".")
                    playerhand.append(deck.cards.pop(0))
                    timeprint("You have:")
                    ppoints = 0
                    paces = 0
                    for i in range(len(playerhand)):
                        card = playerhand[i]
                        timeprint(card.printable())
                        if card.value != "ace":
                            ppoints += card.value
                        else:
                            paces += 1
                    for i in range(paces):
                        if ppoints > 11 - paces:
                            ppoints += 1
                        else:
                            ppoints += 11
                    timeprint("This adds up to " + str(ppoints) + " points.")
        timeprint("It's the dealer's turn.")
        while dpoints < ppoints and dpoints <= 21 and ppoints < 21:
            timeprint("The dealer draws a card.")
            timeprint("He drew a " + deck.cards[0].printable() + ".")
            dealerhand.append(deck.cards.pop(0))
            for i in range(len(dealerhand)):
                card = dealerhand[i]
                if card.value != "ace":
                    dpoints += card.value
                else:
                    daces += 1
            for i in range(daces):
                if dpoints > 11 - daces:
                    dpoints += 1
                else:
                    dpoints += 11
            timeprint("The dealer has " + str(dpoints) + " points.")
        game = False
    if ppoints > 21:
        timeprint("You lose. Stay under 21 points!")
        win = False
    elif dpoints > 21:
        timeprint("The dealer lost. He had over 21 points.")
        win = True
    elif dpoints < ppoints:
        timeprint("You won! The dealer had " + str(dpoints) + " points. You had " + str(ppoints) + ".")
        win = True
    elif ppoints < dpoints:
        timeprint("You lost. The dealer had " + str(dpoints) + " points. You had " + str(ppoints) + ".")
        win = False
    elif ppoints == dpoints:
        timeprint("You tied at " + str(ppoints) + " points.")
        timeprint("Flipping a coin. . .")
        coin = random.randint(0,1)
        if coin == 1:
            timeprint("You won!")
            win = True
        else:
            timeprint("You lost.")
            win = False
    else:
        timeprint("error lol")
        exit()
    strput("Press enter to continue.")
    if win:
        if ppoints == 21:
            timeprint("You got a bonus for getting 21 points.")
            moneys += bet*2.5
            timeprint("You got $" + str(bet * 2.5) + ".")
        else:
            timeprint("You got $" + str(bet*2) + ".")
            moneys += bet*2