# Check if a number is divisible by both 3 and 5.
a=int(input("enter number"))
b=3
c=5
if a%b==0:
    print("number is divisible by 3")
elif a%c==0:
    print("number is divisible by 5")
else:
    print("number is not divisible by both 3 and 5")
