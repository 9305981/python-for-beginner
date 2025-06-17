letter = '''
Dear <|Name|>,
You are selected!
<|Date|>
'''

# Taking inputs from the user
name = input("Enter your name: ")
date = input("Enter the date (e.g., 12 June 2025): ")

# Replacing placeholders with actual values
letter = letter.replace("<|Name|>", name)
letter = letter.replace("<|Date|>", date)

# Displaying the final letter
print("\nFilled Letter:")
print(letter)