total = 0
num_items = int(input("Number of items: "))

for i in range(num_items):
    price = float(input(f"Price of item {i+1}: $"))
    total += price

if total > 100:
    total *= 0.9

print(f"Total price for {num_items} items is ${total:.2f}")