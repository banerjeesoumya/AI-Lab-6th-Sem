n = int(input("Enter a number: "))
c = 0
for i in range(1, int(n / 2)):
    if(n % i == 0):
        c = c + 1
if(c > 2):
    print(n," is not prime")
else:
    print(n," is prime")