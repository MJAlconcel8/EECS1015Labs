# Lab 8
# Author: Mark Joseph Alconcel
# Email: alconcm8@my.yorku.ca
# Student ID:218591115
# Section A
print("My name is Mark Joseph Alconcel")
print("My York Student ID is 218591115")
print("My York email is alconcm8@my.yorku.ca")
print("I'm in Section A")
print("I'm currently in Scarborough")
from random import randint
from time import sleep
class Snail:
    snailanimation =["__~@", "_~_@", "~__@"]
    def __init__(self, name):
        assert len(name)==2,"Snail's initials must be 2 characters."
        self.name = name.upper()
        self.speed = randint(1,10)/10
        self.frame = 0
        self.position = 0.00
    def move(self):
        self.position = self.position + self.speed
        self.frame = self.frame + 1
        if self.frame >2:
            self.frame = 0
    def getIntPos(self):
        return int(self.position)
    def getName(self):
        return self.name
    def getStr(self):
        move1 = self.getIntPos() * " "
        move2 = (40-(self.getIntPos())) * " "
        snailmoving = Snail.snailanimation[int(self.frame)]
        name = self.name
        string = (move1+snailmoving+move2+name)
        return string
def getSnaillist():
    snailcompetitors = []
    snailparticipant= int(input("How many snails are racing?"))
    for i in range(snailparticipant):
        racername = input("Snail %d two initials:" % (i+1))
        snail = Snail(racername)
        snailcompetitors.append(snail)
    return snailcompetitors
def runRace(listofsnailobjects):
    gameplayvalid = True
    timestamp = 1
    lane = 40 * "-"
    input("Press Enter to Start Race")
    while gameplayvalid:
        print("%s Time %d" % (lane, timestamp))
        for snailracer in listofsnailobjects:
            print(snailracer.getStr())
            snailracer.move()
            if snailracer.getIntPos()>39:
                champ = snailracer.getName()
                gameplayvalid = False
        sleep(0.2)
        timestamp = timestamp + 1
    print("Snail %s WON" % (champ))
def main():
    restartgame = "Y"
    while restartgame == "Y":
        print("Snail Race . . .")
        snailcompetitors = []
        snaillist= getSnaillist()
        runRace(snaillist)
        restartgame = input("Play again (Y)?").upper()
        if restartgame!='Y':
            input('Press Enter To End')
main()

