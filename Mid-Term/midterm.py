####
# EECS1015 - Midterm
# Name: Mark Joseph Alconcel
# Student ID: 218591115
# Email: alconcm8@my.yorku.ca
# Section A
##
def task0():
    print("My name is Mark Joseph Alconcel")
    print("My York email is alconcm8@my.yorku.ca")
    print("My student ID is 218591115")
    print("I'm in Section A")
    print("I'm currently in Scarborough")
def task1():
    name = input("Your first name:").title().strip()
    lastname = input("Your last name:").upper().strip()
    amount = float(input("Initial funds to invest:"))
    annualreturn = float(input("Annual return percentage:"))
    year1 = amount + amount * (annualreturn / 100)
    year2 = year1 + year1 * (annualreturn / 100)
    year3 = year2 + year2 * (annualreturn / 100)
    year4 = year3 + year3 * (annualreturn / 100)
    year5 = year4 + year4 * (annualreturn / 100)
    print("Yearly return for %s %s" % (name, lastname))
    print("Initial deposit: $%.2f" % (amount))
    print("Year 1: $%.2f" % (year1))
    print("Year 2: $%.2f" % (year2))
    print("Year 3: $%.2f" % (year3))
    print("Year 4: $%.2f" % (year4))
    print("Year 5: $%.2f" % (year5))

def task2():
    money = float(0)
    vendingmachinevalid = True
    while vendingmachinevalid:
        print("Current amount $%.2f out of $1.00" % (money))
        print("Insert Coin")
        Toonie = float(2)
        Loonie = float(1)
        Quarter = float(0.25)
        Dime = float(0.10)
        Nickel = float(0.05)
        print("1: Toonie ($%.2f)" % (Toonie))
        print("2: Loonie ($%.2f)" % (Loonie))
        print("3: Quarter ($%.2f)" % (Quarter))
        print("4: Dime ($%.2f)" % (Dime))
        print("5: Nickel ($%.2f)" % (Nickel))
        coins = input("Selection [1-5]")
        if coins == "1":
            money = money + Toonie
            if money > 1:
                print("Total amount provided: $%.2f" % (money))
                change = money - 1
                print("Thank you for your purchase")
                print("Please take your change: $%.2f" % (change))
        elif coins == "2":
            money = money + Loonie
            if money == 1:
                print("Total amount provided: $%.2f" % (money))
                print("Thank you for your purchase")
        elif coins == "3":
            money = money + Quarter
            if money > 1:
                print("Total amount provided: $%.2f" % (money))
                change = money - 1
                print("Thank you for your purchase")
                print("Please take your change: $%.2f" % (change))
            elif money == 1:
                print("Total amount provided: $%.2f" % (money))
                print("Thank you for your purchase")
        elif coins == "4":
            money = money + Dime
            if money > 1:
                print("Total amount provided: $%.2f" % (money))
                change = money - 1
                print("Thank you for your purchase")
                print("Please take your change: $%.2f" % (change))
            elif money == 1:
                print("Total amount provided: $%.2f" % (money))
                print("Thank you for your purchase")
        elif coins == "5":
            money = money + Nickel
            if money > 1:
                print("Total amount provided: $%.2f" % (money))
                change = money - 1
                print("Thank you for your purchase")
                print("Please take your change: $%.2f" % (change))
            elif money == 1:
                print("Total amount provided: $%.2f" % (money))
                print("Thank you for your purchase")
        if money >= 1:
            vendingmachinevalid = False

def task3():
    from random import randint
    gameplayvalid = True
    while gameplayvalid:
        print("Dice Game")
        print("Rolling Die 10 times")
        points = 0
        se = 0
        for m in range(1, 12-1):
            die = randint(1, 6)
            print("Roll %d: [%d]" % (m, die))
            points = points + die
            if die == 1:
                se = se + 1
        if se == 2:
            points = points + 10
            print("+10 Bonus for snake eyes [1][1]!")
        if points > 35:
            print("Total %d -- OVER 35 POINTS [YOU WIN!]" % (points))
        else:
            print("Total %d -- TOO FEW POINTS [YOU LOSE!]" % (points))
        playagain = input("Enter 'Y' to play again:").upper()
        if playagain == "Y":
            gameplayvalid = True
        else:
            gameplayvalid = False

def task4():
    sentence = input("Enter string with one word with quotes:")
    def countCases(string):
        uc = 0
        lc = 0
        for i in range(len(string)):
            if string[i].isupper():
                uc = uc + 1
            elif string[i].islower():
                lc = lc + 1
        casecount= print("This string has %d uppercase characters." % (uc)), print("This string has %d lowercase characters." % (lc))
        return casecount
    def flipCase(string):
        caseswitch = string.swapcase()
        return print("Case flip: %s" % (caseswitch))
    def cutQuotedText(string):
        for k in range(len(string) -1, 0, -1):
            if string[k] == '"':
                y = k
        for j in range(0, len(string)):
            if string[j] == '"':
                x = j
        if string.count('"') == 2:
            string = string.replace(string[y:x + 1], "")
            print_string = print("Quote removed: %s" % (string))
            return print_string
        else:
            error = print("Quote removed: 'ERROR! No quoted text.'")
            return error
    countCases(sentence)
    flipCase(sentence)
    cutQuotedText(sentence)
def main():
    task0()
    print("\n----------Task 1-----------")
    task1()
    print("\n----------Task 2-----------")
    task2()
    print("\n----------Task 3-----------")
    task3()
    print("\n----------Task 4-----------")
    task4()
    input("\nPress enter to exit.")
main()