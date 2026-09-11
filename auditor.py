quantity = 0
real_quan = 0
stock = 0

while True:
    quantity = input("Whats the quantity of the stock? (Enter 'quit' to exit): ")

    if quantity == "quit":
        break

    elif not quantity.isdigit() or quantity < "0":
        print("Please enter valid number as an integer")

    else:
        real_quan = quantity

stock = str(real_quan)

print("Quantity is " +stock)
