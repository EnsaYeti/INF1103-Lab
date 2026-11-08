from Supplier import Supplier
from PhysicalProduct_class import PhysicalProduct
from DigitalProduct_class import DigitalProduct
from inventory_class import Inventory
from product_class import Product

def show_product_details(product: Product) -> None:
    product.display_information()
    print(product.get_fulfilment_info())

supplier = Supplier("Agent 0", "PolandCompany", "PolishSpy@gmail.com")

Raidsuit = PhysicalProduct("P001", "RaidSuit", 25000.45, 10, supplier, 20.1)
TrojanHorse = DigitalProduct("P002", "TrojanHorse", 23.45, 7, supplier, 200.1)

show_product_details(Raidsuit)
show_product_details(TrojanHorse)

inventory = Inventory()
inventory.add_product(Raidsuit)
inventory.add_product(TrojanHorse)
inventory.display_all()

for pid in ("P001", "P002"):
    product = inventory.find_product(pid)
    if product is not None:
        product.update_stock(5)
        print(product.name, "stock:", product.stock)

inventory.remove_product("P002")
print(inventory.find_product("P002"))