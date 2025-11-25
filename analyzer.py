print("Ghana Market Price analyzer")
# Supplier sets
supplier_A = {"tomato", "onion", "pepper", "yam", "plantain"}
supplier_B = {"onion", "pepper", "cassava", "carrot", "tomato"}

# Set operations
print("Items both suppliers have:", supplier_A.intersection(supplier_B))
print("Items only supplier A has:", supplier_A.difference(supplier_B))
print("Items only supplier B has:", supplier_B.difference(supplier_A))
print("All unique items:", supplier_A.union(supplier_B))

# Prices dictionary
prices = {
    "tomato": 12,
    "pepper": 5,
    "onion": 10,
    "carrot": 8,
    "yam": 20
}

# User lookup
item = input("Enter item name: ").lower()

#loop to show price of items in dictionary
if item in prices:
    print(f"Price of {item}: GHC {prices[item]}")
else:
    print("Item not sold here.")
