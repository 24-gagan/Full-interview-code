items = [
    {"name": "Apple", "price": 0.5, "category": "Fruit"},
    {"name": "Milk", "price": 1.5, "category": "Dairy"},
    {"name": "Bread", "price": 1.0, "category": "Bakery"},
    {"name": "Orange", "price": 0.75, "category": "Fruit"}
]
filtered_items=[item for item in items if item["price"]<1 and item["category"]=="Fruit"]
print(filtered_items)