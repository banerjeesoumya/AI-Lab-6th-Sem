import yoursearch
import yoursort
import random

r = (int)(input("Enter the range of the array :" ))
arr=[]
for i in range(r):
    arr.append(random.randint(1, 100))
print("The Original Array is ", arr)

print("1. Bubble Sort")
print("2. Insertion Sort")
print("3. Selection Sort")
print("4. Linear Search")
print("5. Binary Search")

ch = (int)(input("Enter your choice : "))

if (ch == 1):
    yoursort.bubble_sort(arr)
    print("The Sorted Array is ", arr)
elif (ch == 2):
    yoursort.insertion_sort(arr)
    print("The Sorted Array is ", arr)
elif (ch == 3):
    yoursort.selection_sort(arr)
    print("The Sorted Array is ", arr)
elif (ch == 4):
    key = (int)(input("Enter the number to be searched : "))
    res = yoursearch.linear_search(arr, key)
    if (res == -1):
        print("The number is not found")
    else:
        print("The number is found at index ", res)
elif (ch == 5): 
    key = (int)(input("Enter the number to be searched : "))
    res = yoursearch.binary_search(arr, key)
    if (res == -1):
        print("The number is not found")
    else:
        print("The number is found at index ", res)
else:   
    print("Invalid Choice")
