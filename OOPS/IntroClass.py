# IntroClass.py

class Item:
	# Constructors
	def __init__(self, name: str, price: float, quantity=0):
		# print(f"I am created! {name}")
		self.name = name
		self.price = price
		self.quantity = quantity

	def calculate_total_price(self):
		return self.price*self.quantity



item1 = Item("Phone", 100, 5)
# item1.price = 100
# item1.quantity = 5
# print(item1.calculate_total_price(item1.price, item1.quantity))
# print(item1.name, item1.price, item1.quantity)

item2 = Item("Laptop", 1000, 3)
# item2.price = 1000
# item2 .quantity = 3
# print(item2.calculate_total_price(item2.price, item2.quantity))
# print(item2.name, item2.price, item2.quantity)

print(item1.calculate_total_price())
print(item2.calculate_total_price())

