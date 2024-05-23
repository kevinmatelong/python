import csv
import pandas as pd
class Item:
    pay_rate = 0.8
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

    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv','r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
        for item in items:
            # print(item)
            Item(
                name = item.get('name'),
                price = float(item.get('price')),
                quantity = int(item.get('quantity'))
            )

    @staticmethod
    def is_integer(num):
        # count out the floats that are point zero
        if isinstance(num,float):
            # count out the floats that are point zero
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

       

    def __repr__(self):
        return f"Item('{self.name} ', '{self.price} ', '{self.quantity}')"


Item.instantiate_from_csv()
print(Item.all)

 