from product_class import Product
from Orderline import OrderLine


class Order:
    def __init__(self, order_id: str):
        self.__order_id: str = order_id
        self.__order_lines: list[OrderLine] = []

    @property
    def order_id(self) -> str:
        return self.__order_id

    def add_order_line(self, product: Product, quantity: int) -> None:
        if not isinstance(quantity, int) or quantity <= 0:
            raise ValueError("Quantity must be a positive integer.")
        # The Order creates the OrderLine itself; callers never build one
        self.__order_lines.append(OrderLine(product, quantity))

    def remove_order_line(self, product_id: str) -> bool:
        for line in self.__order_lines:
            if line.product.product_id == product_id:
                self.__order_lines.remove(line)
                return True
        return False

    def calculate_total(self) -> float:
        return sum(line.calculate_subtotal() for line in self.__order_lines)

    def display_information(self) -> None:
        print(f"Order {self.__order_id}")
        print("------------------")
        if not self.__order_lines:
            print("No order lines.")
        for line in self.__order_lines:
            line.display_information()
        print("------------------")
        print(f"Total: ${self.calculate_total():.2f}")