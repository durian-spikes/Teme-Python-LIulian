products = [
    {"name": "apple", "price": 3.5, "stock": 12},
    {"name": "bread", "price": 4.2, "stock": 4},
    {"name": "coffee", "price": 29.99, "stock": 2},
    {"name": "milk", "price": 6.5, "stock": 9}
]

# 1. Calculate total inventory value
total_value = 0

for product in products:
    total_value += product["price"] * product["stock"]

print("Total value:", round(total_value, 2))


# 2. Sort products by value (price * stock)
sorted_products = sorted(
    products,
    key=lambda product: product["price"] * product["stock"],
    reverse=True
)

print("\nBy value:")

for product in sorted_products:
    value = product["price"] * product["stock"]
    print(f"{product['name']:<12}{value:.2f}")


# 3. Find products with low stock (stock < 5)
print("\nLow stock:")

for product in products:
    if product["stock"] < 5:
        print(f"{product['name']} ({product['stock']})")


# 4. Calculate average price
total_price = 0

for product in products:
    total_price += product["price"]

average_price = total_price / len(products)

print("\nAverage price:", round(average_price, 2))


# 5. Find the most expensive product per unit
most_expensive = max(products, key=lambda product: product["price"])

print("Most expensive:", most_expensive["name"])