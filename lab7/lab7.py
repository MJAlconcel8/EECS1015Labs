#######################
# Lab 7 - Starting code
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
import pytest
from typing import List
# Accepts a list of integers
def initializeMinMaxList(myList: List[int]) -> None:   # given
    myList.sort()

def insertItem(myList: List[int], item: int) -> None:  # given
    myList.append(item)
    myList.sort()

def getMinMax(myList: List[int], minormax: str) -> int:   # given -- but requires additional assert
    elements = 0
    listlength = len(myList)
    assert listlength!=elements, "The list has no elements, enter numbers into list"
    assert minormax.upper()=="MAX" or minormax.upper()=="MIN", "2nd argument must be 'Min' or 'Max' "
    result: int
    if minormax == "MAX":
        result = myList[-1]
        del myList[-1]
    else:
        result = myList[0]
        del myList[0]
    return result
# Main function is given.
def main():
    aList = [10, 11, 99, 1, 55, 100, 34, 88]
    print("Starting List: ", aList)
    initializeMinMaxList(aList)
    min1 = getMinMax(aList, "MIN")
    print("1st min: %d" % (min1))
    min2 = getMinMax(aList, "MIN")
    print("2nd min: %d" % (min2))
    max1 = getMinMax(aList, "MAX")
    print("1st max: %d" % (max1))
    max2 = getMinMax(aList, "MAX")
    print("2nd max: %d" % (max2))
    print("Insert %d %d %d %d" % (min1 - 1, min2 - 1, max1 + 1, max2 + 1))
    insertItem(aList, min1 - 1)
    insertItem(aList, min2 - 1)
    insertItem(aList, max1 + 1)
    insertItem(aList, max2 + 1)
    min1 = getMinMax(aList, "MIN")
    print("1st min: %d" % (min1))
    min2 = getMinMax(aList, "MIN")
    print("2nd min: %d" % (min2))
    max1 = getMinMax(aList, "MAX")
    print("1st max: %d" % (max1))
    max2 = getMinMax(aList, "MAX")
    print("2nd max: %d" % (max2))
    print("DONE.  Type Enter to exit.")
    input()
    test_getMinMaxRequestError()

if __name__ == "__main__":
    main()
    input("press enter to end")
#####
# WRITE YOUR TEST CASES BELOW HERE
#
######
def test_getMinMaxCase1():
    a=[100,1]
    initializeMinMaxList(a)
    minitem = getMinMax(a, "MIN")
    assert minitem==1, '"Min should be 1", where 1 is the minimum item in the list.'
    maxitem = getMinMax(a, "MAX")
    assert maxitem==100, '"Max should be 100, where 100 is the maximum item in the list.'
def test_getMinMaxCase2():
    a = [8]
    initializeMinMaxList(a)
    minitem = getMinMax(a, "MIN")
    assert minitem==8, '"Min should be 100", where 100 is the single item in the list.'
    backtolist = insertItem(a,8)
    maxitem = getMinMax(a, "MAX")
    assert maxitem==8, '"Max should be 100", where 100 is the single item in the list.'
def test_getMinMaxCase3():
    a = []
    initializeMinMaxList(a)
    itemx = insertItem(a,23)
    itemy = insertItem(a,29)
    minitem=getMinMax(a,"MIN")
    assert minitem==23,'"Min should be 23", where 23 is the minimum item in the list.'
    maxitem=getMinMax(a, "MAX")
    assert maxitem==29,  '"Max should be 29, where 100 is the maximum item in the list.'
def test_getMinMaxRequestError():
    a = [71,72,73]
    initializeMinMaxList(a)
    with pytest.raises(AssertionError) as e:
        middlenumber = getMinMax(a,"MID")
    assert e.typename=="AssertionError", "Should raise AssertionError!"
def test_getMinMaxEmptyError():
    a = []
    initializeMinMaxList(a)
    with pytest.raises(AssertionError) as e:
        minitem= getMinMax(a,"LOW")
    assert e.typename =="AssertionError", "Should raise AssertionError!"
