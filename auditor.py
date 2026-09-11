inventory = 0

while True:
    quantity = input("Whats the quantity of the stock? (Enter 'quit' to exit): ")

    if quantity == "quit":
        break

    elif not quantity.isdigit():
        print("Please enter valid number as an integer")

    else:
        real_quan = quantity

print("Quantity is " +real_quan)
