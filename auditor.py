quantity = 0
valid_quan = 0
total = 0
stock = 0

while True:
    quantity = input("Whats the quantity of the stock? (Enter 'quit' to exit): ")

    if quantity == "quit":
        break

    elif not quantity.isdigit() or quantity < "0":
        print("Please enter valid number as an integer")

    else:
        valid_quan = quantity
        total = total + int(valid_quan)

stock = str(total)

print("Total stock is is " +stock)
