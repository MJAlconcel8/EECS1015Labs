# Lab 4
# Author: Mark Joseph Alconcel
# Email: alconcm8@my.yorku.ca
# Student ID: 218591115
# Section A
print("My name is Mark Joseph Alconcel")
print("My York Email Address is alconcm8@my.yorku.ca")
print("My York student ID is 218591115")
print("I'm in section A")
print("I'm currently in Scarborough")
print("--- Welcome to High-Low ---")
print("Start with 100 points. Each round a card will be drawn and shown.")
print("Select whether you think the 2nd card will be Higher or Lower than the 1st card.")
print("Then enter the amount you want to bet.")
print("If you are right, you win the amount you bet, otherwise you lose.")
print("Try to make it to 500 points within 10 tries.")
from random import randint
def getcardvalue():
    cardvalue = randint(2,14)
    return cardvalue
def getCardstr(cardvalue):
    cardvaluestr = str(cardvalue).replace("10", "T").replace("11", "J").replace("12", "Q").replace("13", "K").replace("14","A")
    return cardvaluestr
def getHLGuess():
    while True:
        betType = input("High or Low (H/L)?:").upper()
        if betType == "H":
            return "HIGH"
        elif betType == "L":
            return "LOW"
def getBetAmount(maximum):
    amount = 0
    while amount<=0  or amount>maximum:
        amount = int(input("Input bet amount: "))
    return amount
def playerguesscorrect(card1, card2, betType):
    if betType == "HIGH" and card1<card2:
        return True
    elif betType == "HIGH" and card1>card2:
        return False
    elif betType == "LOW" and card1>card2:
        return True
    elif betType == "LOW" and card1<card2:
        return False
    elif betType == "LOW" or betType == "HIGH" and card1==card2:
        return False
def main():
    gameplayvalid = True
    points = 100
    round = 1
    while gameplayvalid:
        print("-------------------------------------")
        print("OVERALL POINTS:%d ROUND %d/10" % (points, round))
        cardvalue1 = getcardvalue()
        card1 = getCardstr(cardvalue1)
        print("First card is a [%s]" % (card1))
        guess = getHLGuess()
        bet = getBetAmount(points)
        cardvalue2 = getcardvalue()
        card2 = getCardstr(cardvalue2)
        print("Second card is a [%s]" % (card2))
        if playerguesscorrect(cardvalue1,cardvalue2, guess) == True:
            points = points + bet
            print("You bet '%s' for %d - YOU WON" % (guess,bet))
        else:
            points = points - bet
            print("You bet '%s' for %d - YOU LOSE" % (guess, bet))
        round = round + 1
        if round>10:
            print("-----------LOSE-------------")
            print("ONLY *%d* POINTS IN 10 ROUNDS!" % (points))
            print("-----------------------------")
        if points>= 500:
            print("-----------WIN-------------")
            print("YOU MADE IT TO *%d* POINTS IN %d ROUNDS!" % (points,round))
            print("-----------------------------")
        if points<=0:
            print("-----------LOSE-------------")
            print("YOU HAVE *%d* POINTS AFTER %d ROUNDS!" % (points,round))
            print("-----------------------------")
        if round>10 or points >= 500 or points<=0:
            gameplayvalid = False
main()
input("Press Enter To End")