# count how many odd numbers are in a list
numbers = list(map(int, input("Enter numbers separated by space: ").split()))
odd_count = 0

for i in numbers:
    if i % 2 != 0:
        odd_count += 1

if odd_count > 0:
    print("There are", odd_count, "odd numbers in the list.")
else:
    print("There are no odd numbers in the list.")