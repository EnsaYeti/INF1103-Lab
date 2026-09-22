def get_valid_input():
    quantity = 0
    total = 0
    failed_ent = 0
    while True:
        quantity = input("Whats the quantity of the stock? (Enter 'quit' to exit): ")

        if quantity == "quit":
            print ("Total Units Processed is " +str(total))
            print ("Number of Failed/Rejected Entries is " +str(failed_ent))
            break

        elif not quantity.isdigit():
            failed_ent = failed_ent + 1
            print("Please enter valid number as an integer")

        else:
            total = total + int(quantity)

    return total 

get_valid_input()