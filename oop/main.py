# class Item:
#     def calculate_total_price(self,x,y):
#         return x * y

# item1 = Item()
# item1.name = "Phone"
# item1.price = 100
# item1.quantity = 5

# print(item1.calculate_total_price(item1.price , item1.quantity))

# item2 = Item()
# item2.name = "Laptop"
# item2.price = 1000
# item2.quantity = 3

# print(item2.calculate_total_price(item2.price, item2.quantity))


# class Item:
#     def __init__(self,name:str,price:float,quantity=0):
#         self.name = name
#         self.price = price
#         self.quantity = quantity

#         assert price >= 0, f'Price {price} is greater than or equal to zero'
#         assert quantity >= 0, f'Quantity {quantity} is not grater of equal to zero'

#     def calculate_total_price(self):
#         return self.price * self.quantity

# item1 = Item("Phone",100,-2)
# item2 = Item("Laptop",1000,3)

# print(item1.calculate_total_price())
# print(item1.calculate_total_price())

class Item:
    pay_rate = 0.7
    all = []
    def __init__(self,name:str,price:float,quantity=0):
        self.name = name
        self.price = price
        self.quantity = quantity

        Item.all.append(self)
        
        assert price >= 0, f'Price {price} is greater than or equal to zero'
        assert quantity >= 0, f'Quantity {quantity} is not grater of equal to zero'

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * Item.pay_rate
    def __repr__(self):
        return f"Item('{self.name} ', '{self.price} ', '{self.quantity}')"

item1 = Item("Phone",3000,20)
item2 = Item("Laptop",1000,3)

print(item1.calculate_total_price())
print(item2.calculate_total_price())
print(item1.apply_discount())
print(item1.price)
print(Item.all)


# print(Item.all)
