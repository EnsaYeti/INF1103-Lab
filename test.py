from Supplier import Supplier
from PhysicalProduct_class import PhysicalProduct
from DigitalProduct_class import DigitalProduct
from inventory_class import Inventory
from Order import Order

supplier = Supplier("Agent 0", "PolandCompany", "PolishSpy@gmail.com")

RaidSuit = PhysicalProduct("P001", "RaidSuit", 25000.45, 10, supplier, 20.1)
TrojanHorse = DigitalProduct("P002", "TrojanHorse", 23.45, 7, supplier, 200.1)

inventory = Inventory()
inventory.add_product(RaidSuit)

order1 = Order("O001")
order1.add_order_line(RaidSuit, 2)
order1.add_order_line(TrojanHorse, 3)
order1.display_information()
print("Total:", order1.calculate_total())

order2 = Order("O002")
order2.add_order_line(RaidSuit, 1)


print("Same product in both orders:", RaidSuit is RaidSuit)

order1.remove_order_line("P002")
order1.display_information()
TrojanHorse.display_information()
print("Laptop still in inventory:", inventory.find_product("P001") is RaidSuit)

del order2
RaidSuit.display_information()