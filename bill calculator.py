# Define the list of items with price and quantity
items = [
    {"name": "Milk", "price": 25.0, "quantity": 2},
    {"name": "Bread", "price": 30.0, "quantity": 1},
    {"name": "Eggs", "price": 5.0, "quantity": 12},
    {"name": "Butter", "price": 45.5, "quantity": 1}
]

# Initialize total cost
total_cost = 0.0

# Calculate total bill
for item in items:
    item_total = item["price"] * item["quantity"]
    print(f"{item['name']}: {item['quantity']} x {item['price']} = ₹{item_total:.2f}")
    total_cost += item_total

# Print the total bill
print(f"\nTotal Bill: ₹{total_cost:.2f}")
