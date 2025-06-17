'''Calculate electricity bill:

First 100 units: ₹5/unit

Next 100 units: ₹7/unit

Above 200 units: ₹10/unit'''
# Define the electricity bill
# Input total units consumed
units = int(input("Enter total units consumed: "))

# Initialize bill amount
bill = 0

if units <= 100:
    bill = units * 5
elif units <= 200:
    bill = (100 * 5) + ((units - 100) * 7)
else:
    bill = (100 * 5) + (100 * 7) + ((units - 200) * 10)

# Print the total bill
print(f"Total electricity bill for {units} units is ₹{bill}")
