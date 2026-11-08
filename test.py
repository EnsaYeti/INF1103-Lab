from Supplier import Supplier
from PhysicalProduct_class import PhysicalProduct
from DigitalProduct_class import DigitalProduct

supplier = Supplier("Agent 0", "PolandCompany", "PolishSpy@gmail.com")

RaidSuit = PhysicalProduct("P001", "Raid Suit", 23001.45, 10, supplier, 20.1)
TrojanHorse = DigitalProduct("P002", "Trojan Horse", 23.45, 25, supplier, 200.41)

RaidSuit.supplier.display_information()
TrojanHorse.supplier.display_information()

print(RaidSuit.supplier is TrojanHorse.supplier) 

del supplier

RaidSuit.supplier.display_information()
TrojanHorse.supplier.display_information()