from product_class import Product
from PhysicalProduct_class import PhysicalProduct
from DigitalProduct_class import DigitalProduct
from Supplier import Supplier


class ProductFactory:
    @staticmethod
    def create(product_type: str, product_id: str, name: str, price: float,
               stock_quantity: int, supplier: Supplier,
               weight: float | None = None,
               download_size: float | None = None) -> Product:
        if product_type == "physical":
            if weight is None:
                raise ValueError("A physical product needs a weight.")
            return PhysicalProduct(product_id, name, price, stock_quantity, supplier, weight)
        elif product_type == "digital":
            if download_size is None:
                raise ValueError("A digital product needs a download size.")
            return DigitalProduct(product_id, name, price, stock_quantity, supplier, download_size)
        else:
            raise ValueError(f"Unknown product type: {product_type}")