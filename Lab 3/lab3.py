# Lab3
# Author name: Mark Joseph Alconcel
# Student ID: 218591115
# Email address: alconcm8@my.yorku.ca
# Section A

print("My name is Mark Joseph Alconcel")
print("My Student ID is 218591115")
print("My York Email is alconcm8@my.yorku.ca")
print("I'm in section A")
print("I'm currently in Scarborough, Ontario")

# Code for task 1 after this line
print("\n--- Task 1 ---: Compute Fare")
travel_plans = input("(1) one way or (2) round trip\nEnter 1 or 2")
if travel_plans=="1":
    amount_due= 1.80
    age = input("(1) under 12\n(2) 13-64\n(3) 65 or older\nEnter 1, 2, or 3")
    if age == "2":
        print("Total amount: $%.2f [one way (full fare)]" % (amount_due))
    else:
        amount_due = amount_due / 2
        print("Total amount: $%.2f [one way (reduced fare)]" % (amount_due))
elif travel_plans=="2":
    amount_due = 3.50
    age = input("(1) under 12\n(2) 13-64\n(3) 65 or older\nEnter 1, 2, or 3")
    if age == "2":
        print("Total amount: $%.2f [round trip (full fare)]" % (amount_due))
    else:
        amount_due = amount_due / 2
        print("Total amount: $%.2f [round trip (reduced far])]" % (amount_due))

# Code for task 2 after this line
print("\n--- Task 2 ---: Parse string")
sentence = input("Input a string")
for i in range(len(sentence)):
    print("str[%d] = %c" % (i,sentence[i]))
reversed_string = sentence[::-1].replace(" ", "")
print(reversed_string)

# Code for task 3 after this line
print("\n--- Task 3 ---: The maximum *even* number")
print("Keep entering positive integers")
print("To quit, input a negative integer")
max = 0
while True:
    integer = int(input("Enter A number"))
    if (integer<0):
        break
    elif (integer>max) and (integer%2==0):
        max = integer
print("Largest even number: %d" % (max))

# Code for task 4 after this line
print("\n--- Task 4 ---: Better triangle draw")
row = int(input("Enter a number between 5 and 20 "))
while row<5 or row>20:
        row = int(input("Enter a number between 5 and 20 "))
text = "\\"
for l in range(0,1):
    print(text)
for i in range(1,row):
    print("-" * (i) + text)
text_2="|"
for k in range(row,row+1):
    print("-" * (k) + text_2)
text_1 = "/"
for j in range(row):
    print("-"*(row-j-1)+text_1)
input("press enter to end")