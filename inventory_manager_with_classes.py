import json
import os

from inventory_class import Inventory
from PhysicalProduct_class import PhysicalProduct
from DigitalProduct_class import DigitalProduct

base_dir = os.path.dirname(os.path.abspath(__file__))
file_name = os.path.join(base_dir, "inventory.json")

PRODUCT_TYPES = {
    "physical": PhysicalProduct,
    "digital": DigitalProduct,
}


def aesthetic_lines():
    print("------------------")


def product_from_dict(data):
    product_class = PRODUCT_TYPES[data["Type"]]
    return product_class.from_dict(data)


def load_inventory():
    inventory = Inventory()
    if os.path.exists(file_name):
        try:
            with open(file_name, "r") as f:
                data = json.load(f)
            for item in data:
                inventory.add_product(product_from_dict(item))
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


def get_valid_positive_number(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value > 0:
                return value
            print("Value must be greater than 0.")
        except ValueError:
            print("Invalid input, try again")


def get_product_type():
    print("Product type:")
    print("1. physical")
    print("2. digital")
    while True:
        choice = input("Choose product type (1 or 2): ")
        if choice == "1":
            return "physical"
        if choice == "2":
            return "digital"
        print("Please enter 1 or 2")


def get_option():
    while True:
        option = input("\nEnter option: ")
        if not option.isdigit() or int(option) <= 0 or int(option) >= 7:
            print("Please enter a valid option")
        else:
            return int(option)


def add_product(inventory):
    print("Add New Product")
    product_type = get_product_type()
    name = get_valid_name()

    if inventory.search_product(name) is not None:
        print("Item already exists, try 'Update stock' instead.")
        return

    price = get_valid_price()
    stock = get_valid_quantity()
    product_id = inventory.generate_product_id()

    if product_type == "physical":
        weight = get_valid_positive_number("Enter Product Weight (kg): ")
        product = PhysicalProduct(product_id, name, price, stock, weight)
    else:
        size = get_valid_positive_number("Enter Download Size (MB): ")
        product = DigitalProduct(product_id, name, price, stock, size)

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
    print(f"Fulfilment: {product.get_fulfilment_info()}")
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