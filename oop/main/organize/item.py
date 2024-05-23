from phone import Phone
from main import Item

phone1 = Phone("Samsung",20,5,2)
# Item.instantiate_from_csv()

# print(Phone.all)
# print(Item.all)
item1 = Item("Laptop",750,20)

# print(item1.name)
# print(item1.read_only_name)
# # item1.read_only_name = "BBB"
# print(item1.name)

# item1._name = "Mouse"       #Error  single underscore
# print(item1.name)


# item1.name = "Mouse"  
# print(item1.name)

item1.apply_increment(0.2)
item1.apply_discount()
print(item1)

item1.send_email()


