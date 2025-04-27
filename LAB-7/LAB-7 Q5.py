print("Name: VANSH GUPTA ")
print("Roll no: 24BEE158")

prices = {
    "rice": 50,
    "wheat": 40,
    "sugar": 45,
    "oil": 120
}

quantities = {
    "rice": 2,
    "wheat": 3,
    "sugar": 1,
    "oil": 1
}

total_bill = 0

for item in prices:
    price = prices[item]
    qty = quantities.get(item, 0) 
    total_bill += price * qty

print("Total Grocery Bill: ₹", total_bill)
