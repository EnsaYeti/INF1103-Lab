from product_class import Product
from PhysicalProduct_class import PhysicalProduct
from DigitalProduct_class import DigitalProduct

item1 = PhysicalProduct("D01", "PolishSpy", 3.89, 4, 45.6)
item2 = DigitalProduct("D02", "Image", 4.5, 3, 8.4)

item1.display_information()
item2.display_information()

print(item1.get_fulfilment_info())
print(item2.get_fulfilment_info())

print("Cost is " + str(item1.calculate_shipping_cost()))