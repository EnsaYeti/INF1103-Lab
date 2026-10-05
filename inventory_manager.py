def load_inventory():
    transactions = []
    with open("persist_entries.txt", "a+") as persist_file:
        persist_file.seek(0)
        for line in persist_file:
            line = line.strip()

            if line.startswith("9999, Total is,"):
                continue

            prod_num, prod, quant = line.split(", ")
            transactions.append([prod_num, prod, int(quant)])

    return transactions

def save_inventory(inventory,final):
    with open("persist_entries.txt", "w") as file:
        for item in inventory:
            file.write(f"{item[0]}, {item[1]}, {item[2]}\n")
        file.write(f"9999, Total is, {final}")

def add_product():
    prod_name = input("\nEnter Product Name: ")
    while True:
        prod_quant = input("\nEnter Product Quantity: ")

        if not prod_quant.isdigit() or int(prod_quant) <= 0:
            print("Please enter valid number as an integer")
        
        else:
            return prod_name, int(prod_quant)

def update_stock(product, quantity, inventory):
    inventory.append(
        {"name": product, "quantity": quantity}
    )


#transactions = load_inventory()

#for item in transactions:
#    print(f"{item[0]}, {item[1]}, {item[2]}")

#if transactions:
#    prod_num = int(transactions[-1][0])

import json

inventory = [
    {"name":"Pen", "Quantity":10},
    {"name":"Pencil", "Quantity":5},
    {"name":"Eraser", "Quantity":5}
]

print(inventory[0]["name"])

prod_name, prod_quant = add_product()
update_stock(prod_name, prod_quant, inventory)

print(inventory[-1]["name"])