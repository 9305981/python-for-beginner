# Count how many times each element appears in a list.

n = list(map(int, input("Enter numbers separated by space: ").split()))
print("Element frequencies:")
for num in set(n):
    print(f"{num} appears {n.count(num)} times")
