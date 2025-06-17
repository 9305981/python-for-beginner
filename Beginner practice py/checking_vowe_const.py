# Check if a character is a vowel or consonant.
n=input("enter character:")

if n in "aeiou":
    print(n, "is a vowel ✅")
elif n in "bcdfghjklmnpqrstvwxyz":
    print(n, "is a consonant ✅")
else:
    print(n, "is not a valid alphabet letter ❌")
