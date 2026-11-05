from product_class import Product
from can_be_shipped import CanBeShipped

class PhysicalProduct(Product, CanBeShipped):
    def __init__(self, product_id, name, price, stock, weight):
        super().__init__(product_id, name, price, stock)
        self.__weight = weight

    @property
    def weight(self):
        return self.__weight

    def display_information(self):
        super().display_information()
        print(f'|  Weight: {self.__weight}kg')

    def to_dict(self):
        data = super().to_dict()
        data["Weight"] = self.__weight
        return data

    @classmethod
    def from_dict(cls, data):
        return cls(data["ID"], data["Name"], data["Price"], data["Stock"], data["Weight"])

    def get_fulfilment_info(self):
        return "Physical"

    def calculate_shipping_cost(self):
        return 2.00 * self.__weight