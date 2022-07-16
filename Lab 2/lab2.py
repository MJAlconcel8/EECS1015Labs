print("My name is Mark Joseph Alconcel")
print("My Student ID is 218591115")
print("My york email is alconcm8@my.yorku.ca")
print("I'm in Section A")
print("I'm currently in Scarborough, Ontario")


print("Task 1: BMI Calculator")
name = input("Enter Your First and Last name")
a = name.title()
weight_in_kg_1 = input("Enter Weight in Kilograms")
weight_in_kg_2 = float(weight_in_kg_1)
height_in_cm = input("Enter Height in centimeters")
height_in_m = float(height_in_cm) / 100
BMI = float(weight_in_kg_2) / (height_in_m) **2
print("name:%s weight: %.2fkg height: %.2fm BMI: %.2f" % (a, weight_in_kg_2,height_in_m, BMI))



print("Task 2: Leetspeak converter")
Sentence = input("Enter a Sentence")
a = Sentence.upper().replace("T", "+").replace("A", "@").replace("E", "3").replace("I", "|").replace("B", "8").replace("O", "0").replace("C", "[").replace("S", "5")
print("Type a long string: %s" %(a))




print("Task 3: Flipping a string")
sentence1 = input("Enter a Sentence")
string_length = len(sentence1)
Middle_Letter = int(string_length / 2)
a = sentence1[Middle_Letter]
print("This string is %s characters long. The middle letter is '%s'" %(string_length,a))
part_1 = sentence1[0:Middle_Letter].upper()
part_2 = sentence1[Middle_Letter:string_length].upper()
print("Flipped String")
print("%s|%s" % (part_2, part_1))

print("Task 4")
number_1 = input("Enter A number")
number_2 = input("Enter A number")
a = int(number_1)
b= int(number_2)
product = int(number_1) * int(number_2)
print("Input numbers to multiply: %d * %d" % (a,b))
print("Extracted Numbers %d %d" % (a, b))
print("%d * %d" % (a,b))
print(product)
end = input("Press Enter to End")