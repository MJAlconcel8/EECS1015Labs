# Author: Mark Joseph Alconcel
# Email: alconcm8@my.yorku.ca
# Student ID:218591115
# Section A
def task0():
    print("My name is Mark Joseph Alconcel")
    print("My York email is alconcm8@my.yorku.ca")
    print("My student ID is 218591115")
    print("I'm in Section A")
    print("I'm currently in Scarborough")
def task1():
    def printOutcome(userSelection, computerSelection):
        if userSelection == computerSelection:
            print("A tie!")
        elif userSelection == 1:
            if computerselection == 3:
                print("You win!")
            else:
                print("Hal Wins!")
        elif userselection == 2:
            if computerselection == 1:
                print("You win!")
            else:
                print("Hal Wins!")
        elif userSelection == 3:
            if computerSelection == 2:
                print("You win!")
            else:
                print("Hal Wins!")
    from random import randint
    gameplayvaild = True
    while gameplayvaild:
        print("Rock, Paper, Scissors!")
        print("Make your selection. . .")
        userselection = int(input("(1) rock, (2) paper, (3) scissors?"))
        while userselection >= 4 or userselection <= 0:
            print("Invalid selection. Try again.")
            userselection = int(input("(1) rock, (2) paper, (3) scissors?"))
        if userselection == 1:
            print("You: rock")
        elif userselection == 2:
            print("You: paper")
        elif userselection == 3:
            print("You: Scissors")
        computerselection = randint(1, 3)
        if computerselection == 1:
            print("Hal: rock")
        elif computerselection == 2:
            print("Hal: paper")
        elif computerselection == 3:
            print("Hal: Scissors")
        printOutcome(userselection,computerselection)
        playagain = input("Play again (Y/N)?").upper()
        if playagain == "Y":
            gameplayvaild = True
        elif playagain == "N":
            gameplayvaild = False
def task2():
    def swapAdjacentElements(alist):
        for i in range(0, len(alist) - 1, 2):
            alist[i], alist[i + 1] = alist[i + 1], alist[i]
        print("Modified list")
        print(alist)
        stringversion2 = "".join(alist)
        print("String version: '%s'" % (stringversion2))
    string = input("Input two or more chars separated by spaces:")
    characters = 2
    stringlength = len(string)
    print("Initial list")
    list1 = string.split()
    print(list1)
    stringversion1 = "".join(list1)
    print("String version: '%s'" % (stringversion1))
    assert stringlength >= characters, "Must enter two or more characters!"
    swapAdjacentElements(list1)
def task3():
    from utilities import students
    from utilities import studentsInfo
    emptylist = []
    for names in range(len(students)):
        emptystring = ""
        for categories in studentsInfo:
            if names in studentsInfo[categories]:
                emptystring = emptystring + "" + categories
        space = (10 - len(students[names]))
        emptystring = "(" + emptystring[:6] + ") Program: " + emptystring[6:8] + " Housing: " + emptystring[8:]
        emptystring = ("%s" % (students[names]) + emptystring)
        emptylist.append(emptystring + " " * space)
    emptylist.sort()
    for i in range(len(emptylist)):
        sposition = emptylist[i].rfind("s")
        print(emptylist[i][sposition + 1:] + emptylist[i][:sposition + 1])
def task4():
    from utilities import SeaLife
    from time import sleep
    from random import randint
    input("Press enter to start aquarium.")
    emptylist = []
    for animals in range(0, 5):
        emptylist.append(SeaLife(randint(0, 1), (randint(6, 29))))
    timestamp = 0
    while timestamp < 50:
        timestamp = timestamp + 1
        print("----------------------------------------Time: %d" % (timestamp))
        for animals in emptylist:
            animals.move()
            print(animals.getstr())
        sleep(0.3)
def main():
    print("\n--------- Task0: Submission Info       ------------")
    task0()
    print("\n--------- Task1: Rock, Paper, Scissors ------------")
    task1()
    print("\n--------- Task2: Swap List Elements    ------------")
    task2()
    print("\n--------- Task3: Student Info          ------------")
    task3()
    print("\n--------- Task4: Aquarium              ------------")
    task4()

    input("Press enter to quit.")


if __name__ == "__main__":
    main()

