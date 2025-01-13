import random

a = (int)(input("Enter the first number: "))
b = (int)(input("Enter the second number: "))

r = random.randint(a, b)

while(True):
    n = (int)(input ("Guess a number in the range "))
    if (n > r):
        print("Guess is too high")
    elif(n < r):
        print("Guess is too low")
    else:
        print("Correct guess")
        break

