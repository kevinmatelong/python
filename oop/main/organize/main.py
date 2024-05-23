
import csv
import pandas as pd
class Item:
    pay_rate = 0.8
    all = []
    def __init__(self,name:str,price:float,quantity=0):
        # self._name = name
        self.__name = name
        self.__price = price
        self.quantity = quantity

        Item.all.append(self)
        
        assert price >= 0, f'Price {price} is greater than or equal to zero'
        assert quantity >= 0, f'Quantity {quantity} is not grater of equal to zero'

    # @property
    # def name(self):
    #     return self._name

    @property
    def price(self):
        return self.__price

    def apply_discount(self): 
        self.__price = self.__price * Item.pay_rate

    def apply_increment(self,increment_value):
        self.__price = self.__price + self.__price * increment_value

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self,value):
        if len(value) > 10:
            raise Exception("The name is too long")
        else:
            self.__name = value

    def calculate_total_price(self):
        return self.__price * self.quantity

    

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

    def __connect(self, smpt_server):
        pass
    def __prepare_body(self):
        return f"""
        Hello Someone
        We have {self.name} {self.quantity} times.
        Regards, Jim 
        """
    def __send(self):
        pass


    def send_email(self):
        self.__connect('')
        self.__prepare_body()
        self.__send()

    def __repr__(self):
        # return f"Item('{self.name} ', '{self.price} ', '{self.quantity}')"
        return f"{self.__class__.__name__}('{self.name} ', '{self.__price} ', '{self.quantity}')"

    # @property
    # def read_only_name(self):
    #     return "AAA"