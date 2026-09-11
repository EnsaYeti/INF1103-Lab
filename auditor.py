quantity = 0
valid_quan = 0
total = 0
failed_ent = 0

while True:
    quantity = input("Whats the quantity of the stock? (Enter 'quit' to exit): ")

    if quantity == "quit":
        print ("Total Units Processed is " +str(total))
        print ("Number of Failed/Rejected Entries is " +str(failed_ent))
        break

    elif not quantity.isdigit() or quantity < "0":
        failed_ent = failed_ent + 1
        print("Please enter valid number as an integer")

    else:
        valid_quan = quantity
        total = total + int(valid_quan)

        if total > 500:
            print("Alert!! Total stock has exceeded 500.")
            break


