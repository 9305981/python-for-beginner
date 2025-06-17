s = input("Enter a string: ")
reversed_str = s[::-1]
print("Reversed string:", reversed_str)
 #palindrome
s = input("Enter a string: ")
if s == s[::-1]:
    print("It is a palindrome")
else:
    print("It is not a palindrome")
