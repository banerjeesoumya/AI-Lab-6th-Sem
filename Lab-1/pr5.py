n = int(input("Enter the number of items: "))
a = 0
b = 1
while(n > 0):
    print(a)
    c = a + b 
    a = b
    b = c
    n = n - 1