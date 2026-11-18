from Order import Order
from DiscountStrategy import BulkDiscount, PercentageDiscount
from DigitalProduct_class import DigitalProduct
from Supplier import Supplier

supplier = Supplier("S001", "GarrysMachine", "GarrysMachine@gmail.com")
product = DigitalProduct("P001", "Game", 50.0, 10, supplier, 100.0)

order = Order("O001")
order.add_order_line(product, 5) 

order.set_discount(BulkDiscount(200, 20))
print(f"Bulk(200, 20): {order.calculate_total():.2f}")

order.set_discount(PercentageDiscount(10))
print(f"Percentage(10):{order.calculate_total():.2f}")