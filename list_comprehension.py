# Square numbers in a range:
squares = [x * x for x in range(6)]
print(squares)
# Output: [0, 1, 4, 9, 16, 25]

# Filter even numbers:
numbers = [1, 2, 3, 4, 5, 6]
evens = [n for n in numbers if n % 2 == 0]
print(evens)
# Output: [2, 4, 6]

# Uppercase a list of strings:
names = ["alice", "bob", "charlie"]
upper_names = [name.upper() for name in names]
print(upper_names)
# Output: ['ALICE', 'BOB', 'CHARLIE']

# Product Names (strings)
products = ["laptop", "phone", "tablet", "monitor"]
upper_products = [p.upper() for p in products]
# ['LAPTOP', 'PHONE', 'TABLET', 'MONITOR']

# Prices (numbers)
prices = [1000, 800, 450, 300]
discounted = [price * 0.9 for price in prices]
# [900.0, 720.0, 405.0, 270.0]

# Stock status (boolean)
in_stock = [True, False, True, False]
available = [i for i, stock in enumerate(in_stock) if stock]
# [0, 2]

# Product info as tuples
product_info = [("Laptop", 1000), ("Phone", 800), ("Tablet", 450)]
expensive = [name for name, price in product_info if price > 700]
# ['Laptop', 'Phone']

# List of dictionaries
products_data = [
{"name": "Laptop", "price": 1000, "stock": 3},
{"name": "Phone", "price": 800, "stock": 0},
{"name": "Tablet", "price": 450, "stock": 5}
]
available_names = [p["name"] for p in products_data if
p["stock"] > 0]
# ['Laptop', 'Tablet']

discounted_products = [{p["name"]: p["price"] * 0.9} for p in
products_data if p["stock"] > 0]
# [{'Laptop': 900.0}, {'Tablet': 405.0}]

# Nested List Comprehension
products_colors = [
{"name": "Laptop", "colors": ["Silver", "Black"]},
{"name": "Phone", "colors": ["Gold", "Blue"]}
]
all_colors = [color for product in products_colors for color
in product["colors"]]
# ['Silver', 'Black', 'Gold', 'Blue']

products_data = [
{"name": "Laptop", "price": 1000, "stock": 3},
{"name": "Phone", "price": 800, "stock": 0},
{"name": "Tablet", "price": 450, "stock": 5}
]
result = [f"{p['name']} - ${p['price'] * 0.9:.2f}" for p in
products_data if p["stock"] > 0]
# ['Laptop - $900.00', 'Tablet - $405.00']

