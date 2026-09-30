def get_valid_product():
    product = input("\nEnter Product Name (Enter 'quit' to exit): ")
    return product
     

def get_valid_input():
    while True:
        quantity = input("Enter Quantity of the Product: (Enter 'quit' to exit): ")

        if quantity == "quit":
            return quantity

        elif not quantity.isdigit() or int(quantity) <= 0:
            print("Please enter valid number as an integer")

        else:
            return int(quantity)

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

total = 0
prod_num = 999
transactions = load_inventory()
print("Current Orders: \n")

for item in transactions:
    print(f"{item[0]}, {item[1]}, {item[2]}")

if transactions:
    prod_num = int(transactions[-1][0])

while True:
    product = get_valid_product()

    if product == "quit":
        break

    quantity = get_valid_input()

    if quantity == "quit":
        break

    prod_num += 1
    transactions.append([prod_num,product, quantity])
    print(f"\nNew Order Added:\n{prod_num}, {product}, {quantity}")
    print("\nOrder successfully saved to persist_entries.txt")

for item in transactions:
    total += item[2]

save_inventory(transactions,total)

print("Running total is " ,total)