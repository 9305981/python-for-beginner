# Find the grade based on marks (90+ = A, 80+ = B, etc).
marks=int(input("enter a marks"))
if marks>=90:
    print("Grade is A")
elif marks>=80:
    print("Grade is B")
elif marks>=60:
    print("Grade is C")
elif marks>=40:
    print("Grade is D")
else:
    print("F")