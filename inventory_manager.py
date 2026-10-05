import json
import os

base_dir = os.path.dirname(os.path.abspath(__file__))
file_name = os.path.join(base_dir, "inventory.json")

def load_inventory():
    if os.path.exists(file_name):
        try:
            with open(file_name, "r") as f:
                return json.load(f)
        except json.JSONDecodeError:
            print("Inventory file is corrupted. Starting with an empty inventory.")
    return []

def save_inventory(inventory):
    with open(file_name, "w") as f:
        json.dump(inventory, f, indent=4)

def get_valid_product():
    prod_name = input("\nEnter Product Name: ")
    return prod_name

def get_valid_price():
    while True:
        price_input = input("\nEnter Product Price: ")
        
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
        prod_quant = input("\nEnter Product Quantity: ")
    
        if not prod_quant.isdigit() or int(prod_quant) <= 0:
            print("Please enter valid number as an integer")
            
        else:
            return int(prod_quant)

def get_prod_num():
    prod_number = f"P{len(inventory) + 1:03d}"
    return prod_number

def add_product(inventory):
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

def update_stock(inventory):
    prod_name = get_valid_product()

    for item in inventory:
        if item["Name"] == prod_name:
            break 

    else:
        print("Item not found in inventory!")
        return

    prod_quant = get_valid_quantity()

    for item in inventory:
        if item["Name"] == prod_name:
            item["Stock"] += prod_quant
            return

def search_product(inventory):
    prod_name = get_valid_product()

    for item in inventory:
        if item["Name"] == prod_name:
            print(f"{item["ID"]} | {item["Name"]} | ${item["Price"]:.2f} | Stock: {item["Stock"]}\n")
            return

    else:
        print("Product not Found!")

def display_all(inventory):
    for item in inventory:
        print(f"{item["ID"]} | {item["Name"]} | ${item["Price"]:.2f} | Stock: {item["Stock"]}")

inventory = load_inventory()

add_product(inventory)
update_stock(inventory)
search_product(inventory)
display_all(inventory)

save_inventory(inventory)
