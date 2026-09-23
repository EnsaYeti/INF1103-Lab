def get_valid_input():
    failed_ent = 0
    while True:
        quantity = input("Whats the quantity of the stock? (Enter 'quit' to exit): ")

        if quantity == "quit":
            return quantity, failed_ent

        elif not quantity.isdigit():
            print("Please enter valid number as an integer")
            failed_ent = 1
            quantity = 0
            return int(quantity), failed_ent

        else:
            return int(quantity), failed_ent

def process_delivery(current_total, new_value):
    total = (current_total) + (new_value)
    return total

def calculate_tax(amount):
    tax = round(amount * 0.1, 1)
    print("Tax for this delivery is ", tax)
    return tax

total = 0
total_fail = 0

while True:
    quantity, failed_ent = get_valid_input()
    total_fail = total_fail + failed_ent

    if quantity != 0 and quantity != "quit":
        tax = calculate_tax(quantity)
        total = process_delivery(total, quantity)
        print("Updated number of units processed is ", + total)

    

    if quantity == "quit":
        print("Number of Failed/Rejected entries is ", total_fail)
        break



print("Total delieveries processed is ", + total)
