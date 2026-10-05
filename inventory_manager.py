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

def add_product(inventory):
    prod_name = input("\nEnter Product Name: ")

    for item in inventory:
        if item["name"] == prod_name:
            print ("Item already exists, try 'Update stock' instead.")
            return

    while True:
        prod_quant = input("\nEnter Product Quantity: ")

        if not prod_quant.isdigit() or int(prod_quant) <= 0:
            print("Please enter valid number as an integer")
        
        else:
            inventory.append(
                    {"name": prod_name, "quantity": prod_quant}
            )
            break

def update_stock(inventory):
    prod_name = input("\nEnter Product Name: ")
    for item in inventory:
        if item["name"] == prod_name:
            break
        else:
            print("Item not found in inventory!")
            return

    while True:
        prod_quant = input("\nEnter Product Quantity: ")
        if not prod_quant.isdigit() or int(prod_quant) <= 0:
            print("Please enter valid number as an integer")

        else:
            break

    for item in inventory:
        if item["name"] == prod_name:
            item["quantity"] += int(prod_quant)
            return


import json

inventory = [
    {"name":"Pen", "quantity":10},
    {"name":"Pencil", "quantity":5},
    {"name":"Eraser", "quantity":5}
]

add_product(inventory)
update_stock(inventory)

print(inventory[-1]["name"])
print(inventory[0].items())