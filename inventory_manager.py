import json
import os

base_dir = os.path.dirname(os.path.abspath(__file__))
file_name = os.path.join(base_dir, "inventory.json")

def aesthetic_lines():
    print("------------------")

def load_inventory():
    if os.path.exists(file_name):
        try:
            with open(file_name, "r") as f:
                print("inventory.json found.")
                print("Inventory loaded successfully.\n")
                return json.load(f)
        except json.JSONDecodeError:
            print("Inventory file is corrupted. Starting with an empty inventory.")
    return []

def save_inventory(inventory):
    with open(file_name, "w") as f:
        print("Saving inventory.....")
        json.dump(inventory, f, indent=4)
        print("Inventory saved successfully to inventory.json.")

def get_valid_product():
    prod_name = input("Enter Product Name: ")
    return prod_name

def get_valid_price():
    while True:
        price_input = input("Enter Product Price: ")
        
        try:
            prod_price = float(price_input)
            decimals = price_input.split(".")[1] if "." in price_input else ""
            if len(decimals) <= 2 and prod_price > 0:
                return prod_price
            else:
                print("Invalid input, try again")
        except ValueError:
            print("Invalid input, try again")
    

def get_valid_quantity():
    while True:
        prod_quant = input("Enter Product Quantity: ")
    
        if not prod_quant.isdigit() or int(prod_quant) <= 0:
            print("Please enter valid number as an integer")
            
        else:
            return int(prod_quant)

def get_prod_num():
    prod_number = f"P{len(inventory) + 1:03d}"
    return prod_number

def add_product(inventory):
    print("Add New Product")
    prod_name = get_valid_product()

    for item in inventory:
        if item["Name"] == prod_name:
            print ("Item already exists, try 'Update stock' instead.")
            return

    prod_price = get_valid_price()

    prod_quant = get_valid_quantity()

    prod_number = get_prod_num()

    inventory.append(
        {"ID":prod_number, "Name":prod_name, "Price": prod_price, "Stock": prod_quant}
            )
    print("Product added Successfully!")

def update_stock(inventory):
    print("Update Stock")
    prod_name = get_valid_product()

    for item in inventory:
        if item["Name"] == prod_name:
            print("Product Found!")
            print(f"{item["ID"]} | {item["Name"]} | ${item["Price"]:.2f} | Current Stock: {item["Stock"]}\n")
            break 

    else:
        print("Item not found in inventory!")
        return

    prod_quant = get_valid_quantity()

    for item in inventory:
        if item["Name"] == prod_name:
            item["Stock"] += prod_quant
            print(f"New Stock Quantity: {item["Stock"]}\n")
            print("Stock Updated Successfully!")
            return

def search_product(inventory):
    print("Search Product.")
    prod_name = get_valid_product()

    for item in inventory:
        if item["Name"] == prod_name:
            print("Product Found!")
            aesthetic_lines()
            print(f"{item["ID"]} | {item["Name"]} | ${item["Price"]:.2f} | Stock: {item["Stock"]}")
            aesthetic_lines()
            return

    else:
        print("Product not Found!")

def display_all(inventory):
    print("Current Inventory")
    aesthetic_lines()
    for item in inventory:
        print(f"{item["ID"]} | {item["Name"]} | ${item["Price"]:.2f} | Stock: {item["Stock"]}")

    if not inventory: 
        print("Inventory is Empty.")

    aesthetic_lines()

def get_option():
    while True:
        option = input("\nEnter option: ")
        
        if not option.isdigit() or int(option) <= 0 or int(option) >= 7:
            print("Please enter a valid option")
                
        else:
            return int(option)



print("\n=======================================")
print("INVENTORY MANAGEMENT SYSTEM")
print("=======================================")
inventory = load_inventory()

print("-------MENU-------")
print("1. Display All Products")
print("2. Add Product")
print("3. Update Stock")
print("4. Search Product")
print("5. Save Inventory")
print("6. Exit without saving (since last save)")
aesthetic_lines()

while True:
    option = get_option()
    if option == 1:
        display_all(inventory)
    elif option == 2:
        add_product(inventory)
    elif option == 3:
        update_stock(inventory)
    elif option == 4:
        search_product(inventory)
    elif option == 5:
        save_inventory(inventory)
    else:
        break

print("Thank you for using Inventory Management System.\nProgram terminated.")