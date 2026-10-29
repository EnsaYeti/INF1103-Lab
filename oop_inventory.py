import json
import os

from product_class import Product
from inventory_class import Inventory

base_dir = os.path.dirname(os.path.abspath(__file__))
file_name = os.path.join(base_dir, "inventory.json")


def aesthetic_lines():
    print("------------------")


# ---------- File handling ----------

def load_inventory():
    """Build an Inventory from inventory.json if it exists, otherwise start empty."""
    inventory = Inventory()
    if os.path.exists(file_name):
        try:
            with open(file_name, "r") as f:
                data = json.load(f)
            for item in data:
                inventory.add_product(Product.from_dict(item))
            print("inventory.json found.")
            print("Inventory loaded successfully.\n")
        except (json.JSONDecodeError, KeyError, TypeError):
            print("Inventory file is corrupted. Starting with an empty inventory.")
            inventory = Inventory()
    return inventory


def save_inventory(inventory):
    with open(file_name, "w") as f:
        print("Saving inventory.....")
        json.dump(inventory.to_list(), f, indent=4)
        print("Inventory saved successfully to inventory.json.")


# ---------- User input ----------

def get_valid_name():
    return input("Enter Product Name: ")


def get_valid_price():
    while True:
        price_input = input("Enter Product Price: ")
        try:
            price = float(price_input)
            decimals = price_input.split(".")[1] if "." in price_input else ""
            if len(decimals) <= 2 and price > 0:
                return price
            print("Invalid input, try again")
        except ValueError:
            print("Invalid input, try again")


def get_valid_quantity():
    while True:
        quantity = input("Enter Product Quantity: ")
        if not quantity.isdigit() or int(quantity) <= 0:
            print("Please enter valid number as an integer")
        else:
            return int(quantity)


def get_option():
    while True:
        option = input("\nEnter option: ")
        if not option.isdigit() or int(option) <= 0 or int(option) >= 7:
            print("Please enter a valid option")
        else:
            return int(option)


# ---------- Menu actions (they call Inventory/Product methods) ----------

def add_product(inventory):
    print("Add New Product")
    name = get_valid_name()

    if inventory.search_product(name) is not None:
        print("Item already exists, try 'Update stock' instead.")
        return

    price = get_valid_price()
    stock = get_valid_quantity()
    product = Product(inventory.generate_product_id(), name, price, stock)
    inventory.add_product(product)
    print("Product added Successfully!")


def update_stock(inventory):
    print("Update Stock")
    product = inventory.search_product(get_valid_name())

    if product is None:
        print("Item not found in inventory!")
        return

    print("Product Found!")
    product.display_information()
    print()

    product.update_stock(get_valid_quantity())
    print(f"New Stock Quantity: {product.stock}\n")
    print("Stock Updated Successfully!")


def search_product(inventory):
    print("Search Product.")
    product = inventory.search_product(get_valid_name())

    if product is None:
        print("Product not Found!")
        return

    print("Product Found!")
    aesthetic_lines()
    product.display_information()
    aesthetic_lines()


def show_menu():
    print("-------MENU-------")
    print("1. Display All Products")
    print("2. Add Product")
    print("3. Update Stock")
    print("4. Search Product")
    print("5. Save Inventory")
    print("6. Exit without saving (since last save)")
    aesthetic_lines()


# ---------- Main program ----------

def main():
    print("\n=======================================")
    print("INVENTORY MANAGEMENT SYSTEM")
    print("=======================================")
    inventory = load_inventory()
    show_menu()

    while True:
        option = get_option()
        if option == 1:
            inventory.display_all()
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


if __name__ == "__main__":
    main()