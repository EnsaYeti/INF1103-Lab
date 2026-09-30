def get_valid_product():
    product = input("Enter Product Name (Enter 'quit' to exit): ")
    return product
     

def get_valid_input():
    while True:
        quantity = input("Enter Quantity of the Product: (Enter 'quit' to exit): ")

        if quantity == "quit":
            return quantity

        elif not quantity.isdigit():
            print("Please enter valid number as an integer")
            quantity = 0
            return int(quantity)

        else:
            return int(quantity)

def generate_report(total_units):
    print("Total delieveries processed is ", + total_units)

def load_inventory():
    with open("persist_entries.txt", "a+") as persist_file:
        persist_file.seek(0)
        transactions = persist_file.readlines()
        persist_file.seek(0)
        current_amt = persist_file.read()
    return transactions, current_amt

def save_inventory(prod, quant):
    with open("persist_entries.txt", "a+") as persist_file:
        persist_file.write(f"{prod}, {quant}\n")
        print("\nProduct successfully saved to persist_file.txt")


transactions, current_amt = load_inventory()
print("Current Orders: \n\n", current_amt)

while True:
    product = get_valid_product()

    if product == "quit":
        break

    quantity = get_valid_input()

    if quantity == "quit":
        break

    transactions.append([product, quantity])
    print(f"\nNew Order Added:\n{product}, {quantity}")
    save_inventory(product,quantity)

#for item in transactions:
   # total = sum(int(item[1]))
    #break

print(transactions)