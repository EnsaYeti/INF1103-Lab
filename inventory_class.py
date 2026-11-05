class Inventory:
    def __init__(self):
        self.__products = []

    def add_product(self, product):
        if self.search_product(product.name) is not None:
            return False
        self.__products.append(product)
        return True

    def search_product(self, name):
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

    def generate_product_id(self):
        if not self.__products:
            return "P001"
        highest = max(int(p.product_id[1:]) for p in self.__products)
        return f"P{highest + 1:03d}"

    def to_list(self):
        return [product.to_dict() for product in self.__products]