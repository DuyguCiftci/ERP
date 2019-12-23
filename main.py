from contract import Contract
from storage import Storage
from material import Material
from storage_2 import Storage2
from product import Product
# P1 = Product("Nike", "01.01.2019", 20)
#
# print(P1.company_name, P1.start_date, P1.quantity)


# def new_product():
#     company_name = input("Company name: ")
#     start_date = input("Start Date: ")
#     quantity = input("Quantity: ")
#     P1 = Product(company_name, start_date, quantity)
#     print(P1.company_name, P1.start_date, P1.quantity)
#     return P1
#
#
#
#
# storage = Storage()
# product = new_product()
# storage.add_product(product)
# print(storage.storage_dict)
# product = new_product()
# storage.add_product(product)
# print(storage.storage_dict)
# product = new_product()
# storage.add_product(product)
# storage.delete_product(1)
# print(storage.storage_dict)

material_storage = Storage()
product_storage = Storage2()
nike = Contract("Nike", "01.01.2019", "01.01.2020")
leather = Material("Leather", 30, "05.01.2019", None, nike)
material_storage.add_product(leather)
string = Material("String", 10, "06.01.2019", "06.02.2019", nike)
material_storage.add_product(string)
nike.add_material(leather)
nike.add_material(string)

for material in nike.materials.values():
    print(material.material_name, material.quantity)
print(nike.materials)

leather.quantity -= 13

for material in nike.materials.values():
    print(material.material_name, material.quantity)

ingredients = {"Leather": 3, "String": 2}
shoe = Product("Shoe", ingredients, "20.10.2021")
shoe.produce(material_storage, 6, product_storage)
for material in nike.materials.values():
    print(material.material_name, material.quantity)
print(nike.materials)
print(shoe.quantity)
print(product_storage.storage2_dict)