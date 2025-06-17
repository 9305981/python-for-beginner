# Check if a year is a leap year or not.
num=int(input("enter year"))
if (num % 4 == 0 and num % 100 != 0) or (num % 400 == 0):
    print("Leap year ✅")
else:
    print("Not a leap year ❌")
