#######################
# Lab 6 - Starting code
# Name: Mark Joseph Alconcel
# Student ID: 218591115
# email: alconcm8@my.yorku.ca
# Section A
#######################
print("My name is Mark Joseph Alconcel")
print("My York Student ID is 218591115")
print("My York email is alconcm8@my.yorku.ca")
print("I'm in Section A")
print("I'm currently in Scarborough")
def task1():
    dictmenu = {'Fruits': {'Apple': 1.99, 'Banana': 0.59, 'Kiwi': 1.1, 'Grapes': 2.99, 'Pear': 2.15},'Drinks': {'Water': 1.0, 'Juice': 3.5, 'Coffee': 1.5, 'Soda': 1.5, 'Tea': 1.25},'Dessert': {'Ice Cream': 2.99, 'Pie': 2.5, 'Cake': 2.75},'Main Dishes': {'Masala Dosa': 4.25, 'Jianbing': 2.88, 'Falafel': 5.15, 'Pizza': 8.5}}
    for i in dictmenu:
        foodcategory = i
        print("----" + foodcategory + "----")
        for j in dictmenu[i]:
            price = (dictmenu[i][j])
            item = j
            print("$%.2f %s" % (price, item))
def task2():
    decoder = {80: 'P', 121: 'y', 116: 't', 104: 'h', 111: 'o', 110: 'n', 105: 'i', 115: 's', 99: 'c', 108: 'l',46: '.', 32: ' ', 44: ',', 45: '-', 95: '_', 40: '(', 42: '*', 41: ')', 47: '/', 92: '\\', 61: '=', 39: "'", 124: '|', 96: '`', 58: ':', 59: ';'}
    msg1 = [[80, 121, 116, 104, 111, 110], [105, 115], [99, 111, 111, 108, 46]]
    msg2 = [[32, 32, 32, 44, 45, 46], [32, 95, 40, 42, 95, 42, 41, 95], [40, 95, 32, 32, 111, 32, 32, 95, 41],[32, 32, 47, 32, 111, 32, 92], [32, 40, 95, 47, 32, 92, 95, 41, 32]]
    msg3 = [[32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 40], [32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 41],[32, 32, 32, 32, 32, 95, 95, 46, 46, 45, 45, 45, 46, 46, 95, 95],[32, 44, 45, 61, 39, 32, 32, 47, 32, 32, 124, 32, 32, 92, 32, 32, 96, 61, 45, 46],[58, 45, 45, 46, 46, 95, 95, 95, 95, 95, 95, 95, 95, 95, 95, 95, 46, 46, 45, 45, 59],[32, 92, 46, 44, 95, 95, 95, 95, 95, 95, 95, 95, 95, 95, 95, 95, 95, 44, 46, 47]]
    for items in msg1:
        string = ""
        for x in items:
            string = string + decoder[x]
        print(string)
    for items in msg2:
        string = ""
        for x in items:
            string = string + decoder[x]
        print(string)
    for items in msg3:
        string = ""
        for x in items:
            string = string + decoder[x]
        print(string)


def main():
    print("------ Task 1 ------")
    task1()
    print("------ Task 2 ------")
    task2()
    input('Press enter to finish.')
if __name__ == '__main__':
  main()