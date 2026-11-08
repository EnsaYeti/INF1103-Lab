from Supplier import Supplier
from PhysicalProduct_class import PhysicalProduct
from DigitalProduct_class import DigitalProduct
from inventory_class import Inventory
from Order import Order

supplier = Supplier("Agent 0", "PolandCompany", "PolishSpy@gmail.com")
inventory = Inventory()

inventory.add_product(PhysicalProduct("P001", "RaidSuit", 25000.45, 10, supplier, 20.1))
inventory.add_product(DigitalProduct("P002", "TrojanHorse", 23.45, 7, supplier, 200.1))

for product in inventory.products:
    product.display_information()
    print(product.get_fulfilment_info())