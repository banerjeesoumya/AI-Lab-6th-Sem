l = (float)(input("Enter the length of the rectangle "))
b = (float)(input("Enter the breadth of the rectangle "))

rectangle_area = l * b

print ("The area of the rectangle: ", rectangle_area)

a = b / 2;

square_area = a * a

print ("The area of the square: ", square_area)

if (rectangle_area > square_area):
    print("Area of the rectangle is greater than that of the square")
else :
    print("Area of the square is greater than that of the rectangle")