from product_class import Product
from Supplier import Supplier

class DigitalProduct(Product):
    def __init__(self, product_id: str, name: str, price: float, stock: int, supplier: Supplier, download_size: float):
        super().__init__(product_id, name, price, stock, supplier)
        self.__download_size = download_size

    @property
    def download_size(self):
        return self.__download_size

    def display_information(self):
        super().display_information()
        print(f'  Download size: {self.__download_size}MB')

    def to_dict(self):
        data = super().to_dict()
        data["Download Size"] = self.__download_size
        return data

    @classmethod
    def from_dict(cls, data):
        return cls(data["ID"], data["Name"], data["Price"], data["Stock"],
                 Supplier.from_dict(data["Supplier"]), data["Download Size"])

    def get_fulfilment_info(self):
        return "digital"