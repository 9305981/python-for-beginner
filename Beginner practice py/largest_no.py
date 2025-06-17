#Find the second largest number in a list.
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

# Check all possible positions of second largest
if (a > b and a < c) or (a < b and a > c):
    second_largest = a
elif (b > a and b < c) or (b < a and b > c):
    second_largest = b
else:
    second_largest = c

print("Second largest number is:", second_largest)
