import random

a = (int)(input("Enter the first number: "))
b = (int)(input("Enter the second number: "))

r = random.randrange(a, b)

while(True):
    n = (int)(input ("Guess a number in the range "))
    if (n > a):
        print("Guess is too high")
    elif(n < a):
        print("Guess is too low")
    else:
        print("Correct guess")
        break

