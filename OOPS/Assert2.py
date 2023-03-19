class Item:
	pay_rate = 0.8 # The pay rate after 20% discount

	all = []

	def __init__(self, name: str, price: float, quantity=0):
		# Run validations to received arguments
		assert price >= 0, f"Price {price} is not greater than or equal to zero"
		assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to zero"


		# Assign to self object
		self.name = name
		self.price = price
		self.quantity = quantity

		# Action to execute

		Item.all.append(self)

	def calculate_total_price(self):
		return self.price*self.quantity

	def apply_discount(self):
		self.price = self.price * self.pay_rate

	def __repr__(self):
		return f"Item('{self.name}', {self.price}, {self.quantity})"


item1 = Item("Phone", 100, 6)

item2 = Item("Laptop", 1000, 3)

item3 = Item("Cable", 10, 5)

item4 = Item("Mouse", 50, 5)

item5 = Item("Keyboard", 75, 5)

# print(Item.__dict__) # All the attributes of class level
# print(item1.__dict__) # All the attributes of instance level
# print(item2.__dict__) # All the attributes of instance level

# item1.apply_discount()
# print(item1.price)

# item2.pay_rate = 0.6
# item2.apply_discount()
# print(item2.price)

# print(Item.all)

# for instance in Item.all:
# 	print(instance.name)

print(Item.all)