print("Name: VANSH GUPTA")
print("Roll no: 24BEE158")

menu = [
    ("Burger", 120),
    ("Pizza", 250),
    ("Pasta", 180),
    ("Fries", 100),
    ("Sandwich", 90),
    ("Salad", 150)
]


sorted_menu = sorted(menu, key=lambda item: item[1], reverse=True)


print("Menu sorted by price (high to low):")
for food, price in sorted_menu:
    print(f"{food}: ₹{price}")
