# Find the largest of three numbers using nested if-else.
a=int(input("enter number"))
b=int(input("enter number"))
c=int(input("enter number"))
if a >= b:
    if a >= c:
        largest = a
    else:
        largest = c
else:
    if b >= c:
        largest = b
    else:
        largest = c

print("Largest number is:", largest)