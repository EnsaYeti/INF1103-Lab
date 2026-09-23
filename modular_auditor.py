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

total = 0
total_fail = 0

while True:
    quantity, failed_ent = get_valid_input()
    total_fail = total_fail + failed_ent
    

    if quantity == "quit":
        print("Number of failed is ", total_fail)
        break

    total = process_delivery(total, quantity)


print("Number of units processed is ", + total)
