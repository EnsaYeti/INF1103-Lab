from abc import ABC, abstractmethod
from Supplier import Supplier

class Product(ABC):
    def __init__(self, product_id: str, name: str, price: float, stock: int, supplier: Supplier):
        self.__product_id = product_id
        self.__name = name
        self.__price = price
        self.__stock = stock
        self.__supplier: Supplier = supplier

    @property
    def product_id(self) -> str:
        return self.__product_id

    @property
    def name(self) -> str:
        return self.__name

    @property
    def price(self) -> float:
        return self.__price

    @property
    def stock(self) -> int:
        return self.__stock

    @property
    def supplier(self) -> Supplier:
        return self.__supplier

    def update_stock(self, quantity: int) -> None:
        if not isinstance(quantity, int) or quantity <= 0:
            raise ValueError("Quantity must be a positive integer.")
        self.__stock += quantity

    def display_information(self) -> None:
        print(f'{self.__product_id} | {self.__name} | ${self.__price:.2f} | Stock: {self.__stock}')

    def to_dict(self) -> dict:
        return {
            "Type": self.get_fulfilment_info(),
            "ID": self.__product_id,
            "Name": self.__name,
            "Price": self.__price,
            "Stock": self.__stock,
            "Supplier": self.__supplier.to_dict(),
             }

    @classmethod
    def from_dict(cls, data: dict) -> "Product":
        return cls(data["ID"], data["Name"], data["Price"], data["Stock"], Supplier.from_dict(data["Supplier"]))

    @abstractmethod
    def get_fulfilment_info(self) -> str:
        pass