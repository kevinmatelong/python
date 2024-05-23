from main import Item

class Phone(Item):
    # all = []
    def __init__(self,name:str,price:float,quantity=0,broken_phones=0):
        super().__init__(name,price,quantity)
        self.broken_phones = broken_phones

        assert broken_phones >= 0, f"Broken Phones {broken_phones} is greater or equal to zero"
        # Phone.all.append(self)

