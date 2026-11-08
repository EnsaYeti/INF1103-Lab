from Supplier import Supplier
from PhysicalProduct_class import PhysicalProduct
from inventory_class import Inventory

supplier = Supplier("Agent 0", "PolandCompany", "PolishSpy@gmail.com")

RaidSuit = PhysicalProduct("P001", "RaidSuit", 25000.45, 10, supplier, 20.1)

inventory_a = Inventory()
inventory_b = Inventory()

inventory_a.add_product(RaidSuit)
print("In A:", inventory_a.find_product("P001") is RaidSuit)

inventory_a.remove_product("P001")
print("In A after removal:", inventory_a.find_product("P001"))
RaidSuit.display_information()
RaidSuit.update_stock(5)
print("Stock:", RaidSuit.stock)

inventory_b.add_product(RaidSuit)
print("In B:", inventory_b.find_product("P001") is RaidSuit)

inventory_b.remove_product("P001")
RaidSuit.display_information()