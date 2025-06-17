# Check if all elements in a list are unique.
n=list(map(int,input("enter numbers separated by commas:").split()))
# Check for uniqueness
if len(n) == len(set(n)):
    print(f"{n} -> Unique ✅")
else:
    print(f"{n} -> Not Unique ❌")