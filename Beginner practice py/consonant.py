s = input("Enter a string: ")
consonant= "bcdfghjklmnpqrstwxyz"
count = sum(1 for char in s if char in consonant)
print("Number of consonant:", count)