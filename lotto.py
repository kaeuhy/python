import random

def makeLotto():
    myList = []
    while len(myList) != 6:
        number = random.randint(1, 45)
        if number not in myList:
            myList.append(number)
    return myList

print(sorted(makeLotto()))