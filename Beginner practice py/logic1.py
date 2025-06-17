# Print the largest, smallest, and middle number out of 3 using if-else.
def larg_small_midd(a, b, c):
    nums = sorted([a, b, c])  # Sort the list
    smallest = nums[0]
    middle = nums[1]
    largest = nums[2]

    print("Smallest number:", smallest)
    print("Middle number:", middle)
    print("Largest number:", largest)

# Input
a, b, c = map(int, input("Enter 3 numbers separated by space: ").split())
larg_small_midd(a, b, c)