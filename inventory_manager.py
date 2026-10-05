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

def get_valid_product():
    prod_name = input("\nEnter Product Name: ")
    return prod_name

def get_valid_price():
    while True:
        price_input = input("\nEnter Product Price: ")
        
        try:
            prod_price = float(price_input)
            decimals = price_input.split(".")[1] if "." in price_input else ""
            if len(decimals) <= 2:
                return prod_price
            else:
                print("Too many decimal places")
        except ValueError:
            print("Not a number")
    

def get_valid_quantity():
    while True:
        prod_quant = input("\nEnter Product Quantity: ")
    
        if not prod_quant.isdigit() or int(prod_quant) <= 0:
            print("Please enter valid number as an integer")
            
        else:
            return prod_quant

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

    prod_quant=get_valid_quantity()

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
            item["Stock"] += int(prod_quant)
            return


import json

inventory = [
    {"ID":"P001", "Name":"Pen", "Price": 5.00, "Stock":10},
    {"ID":"P002", "Name":"Pencil", "Price": 3.00, "Stock":5},
    {"ID":"P003", "Name":"Eraser", "Price": 4.00, "Stock":5}
]

add_product(inventory)
update_stock(inventory)

for item in inventory:
    print(f"{item['ID']}  {item['Name']:<10} ${item['Price']:.2f}  Stock: {item['Stock']}")
