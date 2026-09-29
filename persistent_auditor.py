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

def process_delivery(current_total, new_value):
    total = (current_total) + (new_value)
    return total

def generate_report(total_units):
    print("Total delieveries processed is ", + total_units)

def load_inventory():
    with open("persist_entries.txt", "a+") as persist_file:
        persist_file.seek(0)
        start_amt = persist_file.read()
    return start_amt


total = 0
start_amt = load_inventory()
print("Current Orders: ", start_amt)

while True:
    product = get_valid_product()

    if product == "quit":
        break

    quantity = get_valid_input()

    if quantity != "quit":
       break

    else:
        total = process_delivery(total, quantity)
        print("Updated number of units processed is ", + total)
        print("New Order Added: ", product, quantity)

generate_report(total)
