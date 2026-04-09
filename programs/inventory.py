# Inventory Management System
# Developed by:
# L. Navaneesh Reddy
# Mohit
# Chrysolite
# Pavan R
# Sai Sathwik

import json
import os

FILE = "database.txt"

def load_data():
    if not os.path.exists(FILE):
        return []
    with open(FILE, "r") as f:
        return json.load(f)

def save_data(data):
    with open(FILE, "w") as f:
        json.dump(data, f, indent=4)

def add_item():
    data = load_data()
    name = input("Enter item name: ")
    qty = int(input("Enter quantity: "))
    price = float(input("Enter price: "))
    data.append({"name": name, "quantity": qty, "price": price})
    save_data(data)
    print("Item added!")

def view_items():
    data = load_data()
    if not data:
        print("No items available.")
        return
    for i, item in enumerate(data, 1):
        print(i, item)
        
        # 🔥 Low stock alert
        if item["quantity"] < 5:
            print("⚠️ Low stock alert for:", item["name"])

def update_item():
    data = load_data()
    view_items()
    i = int(input("Enter item number: ")) - 1
    data[i]["quantity"] = int(input("New quantity: "))
    data[i]["price"] = float(input("New price: "))
    save_data(data)
    print("Item updated!")

def delete_item():
    data = load_data()
    view_items()
    i = int(input("Enter item number: ")) - 1
    data.pop(i)
    save_data(data)
    print("Item deleted!")

def main():
    while True:
        print("\n1.Add 2.View 3.Update 4.Delete 5.Exit")
        ch = input("Enter choice: ")
        
        if ch not in ["1","2","3","4","5"]:
            print("Invalid choice! Enter 1-5")
            continue
        
        if ch == "1": add_item()
        elif ch == "2": view_items()
        elif ch == "3": update_item()
        elif ch == "4": delete_item()
        elif ch == "5": break

main()
