radius=float(input("Enter the radius of the circle: "))
area=3.14*radius*radius
circumference=2*3.14*radius
integer_area=int(area)
integer_circumference=int(circumference)
print("The area of the circle is:", integer_area)
print("The circumference of the circle is:", integer_circumference)
print("The area of the circle is:", area)
print("The circumference of the circle is:", circumference)
print("the area of the circe(converted to integer) is:", integer_area)

text=input("Enter a string: ")
sub=input("Enter a sub string: ")
print(f"enter the first string: {text}")
print(f"enter the second string: {sub}")
print(f"the last string is: {text[-1]}")
print(f"enter the first 3characters of the string: {text[:3]}")
print(f"enter the last 3 characters of the string: {text[-3:]}")