
import random
t = random.randint(1, 50)
print ("Guess The Number")
print ("")
print ("The program will generate random number from 1 to 50 and you have to guess it, we will give you some hints after you inter the number")
s=''
print(" ")
print ("To Reveal The True Number Enter 0")
def checkIsNumber(s):
    try:
         var = int(s)
         return var
    except ValueError:
        print("That's not an int!")
        return 0
def checkResultAndHints(var):
    if var > t:
        print(" The number is too High ")
    elif var < t:
        print ("The number is too Low")
    elif var ==0 :
        print ("You Lost \n The Answer is : " ,t)
        quit()
    elif var == t :
        print ("YOU GOT IT ")

while (True):
    s = input()
    var = checkIsNumber(s)
    if var == 0:
        continue
    checkResultAndHints(var)
