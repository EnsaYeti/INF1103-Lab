from product_class import Product

class Inventory:
    def __init__(self):
        self.__products: list[Product] = []

    def add_product(self, product: Product) -> bool:
        if self.search_product(product.name) is not None:
            return False
        self.__products.append(product)
        return True

    def remove_product(self, product_id: str) -> bool:
        product = self.find_product(product_id)
        if product is None:
            return False
        self.__products.remove(product)
        return True

    def find_product(self, product_id: str) -> Product | None:
        for product in self.__products:
            if product.product_id == product_id:
                return product
        return None

    def search_product(self, name: str) -> Product | None:
        for product in self.__products:
            if product.name == name:
                return product
        return None

    def display_all(self):
        print("Current Inventory")
        print("------------------")
        if not self.__products:
            print("Inventory is Empty.")
        for product in self.__products:
            product.display_information()
        print("------------------")

    def generate_product_id(self) -> str:
        if not self.__products:
            return "P001"
        highest = max(int(p.product_id[1:]) for p in self.__products)
        return f"P{highest + 1:03d}"

    def to_list(self) -> list[dict]:
        return [product.to_dict() for product in self.__products]