from product_class import Product

class DigitalProduct(Product):
    def __init__(self, product_id, name, price, stock, download_size):
        super().__init__(product_id, name, price, stock)
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
        return cls(data["ID"], data["Name"], data["Price"], data["Stock"], data["Download Size"])

    def get_fulfilment_info(self):
        return "Digital"