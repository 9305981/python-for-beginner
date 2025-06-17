#Remove all duplicates from a list
numbers = list(map(int, input("Enter numbers separated by space: ").split()))
unique = list(set(numbers))
print("List after removing duplicates:", unique)
