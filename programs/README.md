# Project: Inventory Management System
# Team Members:
# 1. L. Navaneesh Reddy
# 2. Mohit
# 3. Chrysolite
# 4. Pavan R.
# 5. Sai Sathwik

import json
import os

FILE = "database.txt"

def load_data():
    """Reads data from the text file and converts it from JSON to a Python list."""
    if not os.path.exists(FILE):
        return []
    try:
        with open(FILE, "r") as f:
            return json.load(f)
    except:
        return []

def save_data(data):
    """Converts the Python list to JSON format and saves it to the text file."""
    with open(FILE, "w") as f:
        json.dump(data, f, indent=4)

def add_item():
    """Takes user input to create a new item dictionary and adds it to the list."""
    data = load_data()
    name = input("Enter item name: ")
    try:
        qty = int(input("Enter quantity: "))
        price = float(input("Enter price: "))
        item = {"name": name, "quantity": qty, "price": price}
        data.append(item)
        save_data(data)
        print("Item added successfully.")
    except ValueError:
        print("Invalid input. Quantity and Price must be numbers.")

def view_items():
    """Iterates through the list and displays items in a formatted table."""
    data = load_data()
    if not data:
        print("Inventory is empty.")
        return

    print("\nNo.  Item Name            Qty        Price")
    print("-" * 45)
    for i, item in enumerate(data, start=1):
        print(f"{i:<4} {item['name']:<20} {item['quantity']:<10} {item['price']}")

def update_item():
    """Finds an item by its index and updates its values."""
    data = load_data()
    view_items()
    if not data: return
    
    try:
        index = int(input("\nEnter item number to update: ")) - 1
        if 0 <= index < len(data):
            data[index]["quantity"] = int(input("New quantity: "))
            data[index]["price"] = float(input("New price: "))
            save_data(data)
            print("Update successful.")
        else:
            print("Invalid selection.")
    except ValueError:
        print("Invalid input.")

def delete_item():
    """Removes an item from the list based on user selection."""
    data = load_data()
    view_items()
    if not data: return

    try:
        index = int(input("\nEnter item number to delete: ")) - 1
        if 0 <= index < len(data):
            removed = data.pop(index)
            save_data(data)
            print(f"Deleted: {removed['name']}")
        else:
            print("Invalid selection.")
    except ValueError:
        print("Invalid input.")

def main():
    """The main control loop for the menu-driven interface."""
    while True:
        print("\nINVENTORY MANAGEMENT SYSTEM")
        print("1. Add Item")
        print("2. View Items")
        print("3. Update Item")
        print("4. Delete Item")
        print("5. Exit")
        
        choice = input("\nSelect an option (1-5): ")

        if choice == "1":
            add_item()
        elif choice == "2":
            view_items()
        elif choice == "3":
            update_item()
        elif choice == "4":
            delete_item()
        elif choice == "5":
            print("Program terminated.")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()
