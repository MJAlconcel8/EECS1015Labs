#########################
# EECS1015 - Lab 5
# Mark Joseph Alconcel
# 218591115
# alconcm8@my.yorku.ca
# Section A
#########################
print("My name is Mark Joseph Alconcel")
print("My York email address is alconcm8@my.yorku.ca")
print("My student ID is 218591115")
print("I'm in Section A")
print("I'm currently in Scarborough")
def task1():
    from random import randint
    listsize = int(input("Input list size:"))
    maxint = int(input("Input max int:"))
    def generateRandomList(list_size, maximum_integer_value):
        randomlist = []
        for i in range(list_size):
            numbers = randint(0, maximum_integer_value)
            randomlist.append(numbers)
        print(randomlist)
        return randomlist
    def computeAverage(alist):
        a = sum(alist) / len(alist)
        print("Average value = %.4f" % (a))
    list = generateRandomList(listsize, maxint)
    computeAverage(list)
def task2():
    phonenumber = input("Type here:")
    def stringToCharLst(inputString):
        numbers = list(inputString)
        print(numbers)
        return numbers
    def charsToWord(alist):
        dict = {"0": "zero", "1": "one", "2": "two", "3": "three", "4": "four", "5": "five", "6": "six", "7": "seven","8": "eight", "9": "nine", "-": "dash"}
        lists = []
        for i in alist:
            words = dict[i]
            lists.append(words)
        print(lists)
        a_string = "->".join(lists)
        print(a_string)
    alist = stringToCharLst(phonenumber)
    charsToWord(alist)
def main():
    print("\n--------- TASK 1: Random List -------------")
    task1()
    print("\n--------- TASK 2: Phone number to text ---")
    task2()
    input("Press Enter To End")
main()