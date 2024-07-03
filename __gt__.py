class Order:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def __gt__(self, ord2):
        return self.price > ord2.price


ord1 = Order("Tea", 10)
ord2 = Order("Chips", 25)

print(ord1 > ord2)