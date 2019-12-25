from contract import Contract
from storage import Storage
from material import Material
from storage_2 import Storage2
from product import Product
from database import Database
import os
import pandas as pd

# os.system("git fetch origin")
# os.system("git reset --hard origin/master")
# os.system("git clean -f -d")

database = Database()
material_storage = Storage()
product_storage = Storage2()


def read_contracts():
    contracts = pd.read_excel('contracts.xlsx')

    companies = contracts['Company Name']
    start_dates = contracts['Start Date']
    end_dates = contracts['End Date']

    for i in range(len(companies)):
        contract = Contract(companies[i], start_dates[i], end_dates[i])
        database.add_contract(contract)


def read_materials():
    materials = pd.read_excel('materials.xlsx')

    names = materials['Material Name']
    quantities = materials['Quantity']
    arrivals = materials['Arrival Date']
    expires = materials['Expire Date']
    suppliers = materials['Supplier']
    for i in range(len(names)):
        print(names[i])
        supplier = database.contracts[suppliers[i]]
        M1 = Material(names[i], quantities[i], arrivals[i], expires[i], supplier)
        supplier.add_material(M1)
        material_storage.add_material(M1)


def read_products():

    products = pd.read_excel('products.xlsx', sheet_name='Sheet1')
    sheet2 = pd.read_excel('products.xlsx', sheet_name='Sheet2')

    names = products['Product Name']
    expires = products['Expire Date']
    quantities = products['Quantity']
    ingrds = sheet2['Ingredients']

    for i in range(len(names)):
        ingredients = {}
        for j in range(len(ingrds)):
            ingredients[ingrds[j]] = sheet2[names[i]][j]
        print(ingredients)
        P1 = Product(names[i], ingredients, expires[i], quantities[i])
        print(P1.product_name, P1.expire_date, P1.quantity)
        product_storage.add_product(P1)


def save_materials():
    materials = {'Material Name': [],
                 'Quantity': [],
                 'Arrival Date': [],
                 'Expire Date': [],
                 'Supplier': []
                 }

    for material in material_storage.storage_dict.values():
        materials['Material Name'].append(material.material_name)
        materials['Quantity'].append(material.quantity)
        materials['Arrival Date'].append(material.date)
        materials['Expire Date'].append(material.expiration_date)
        materials['Supplier'].append(material.supplier.company_name)

    materials = pd.DataFrame(materials)

    writer = pd.ExcelWriter('materials.xlsx')
    materials.to_excel(writer)
    writer.save()


def save_contracts():
    contracts = {'Company Name': [],
                 'Start Date': [],
                 'End Date': []
                 }

    for contract in database.contracts.values():
        contracts['Company Name'].append(contract.company_name)
        contracts['Start Date'].append(contract.start_date)
        contracts['End Date'].append(contract.end_date)

    contracts = pd.DataFrame(contracts)

    writer = pd.ExcelWriter('contracts.xlsx')
    contracts.to_excel(writer)
    writer.save()


def save_products():
    products = {'Product Name': [],
                'Expire Date': [],
                'Quantity': []
                }

    for product in product_storage.storage2_dict.values():
        products['Product Name'].append(product.product_name)
        products['Expire Date'].append(product.expire_date)
        products['Quantity'].append(product.quantity)

    products = pd.DataFrame(products)

    writer = pd.ExcelWriter('products_1.xlsx', sheet_name='Sheet1')
    products.to_excel(writer)
    writer.save()


read_contracts()
read_materials()
read_products()

# ingredients = {"Leather": 3, "String": 2}
# shoe = Product("Shoe", ingredients, "20.10.2021")
# shoe.produce(material_storage, 6, product_storage)

# print(shoe.quantity)
# print(product_storage.storage2_dict)
example_product = product_storage.storage2_dict["Milk Chocolate"]
example_product.produce(material_storage, 2, product_storage)
print(example_product.quantity)
print(product_storage.storage2_dict)

save_materials()
save_contracts()
save_products()
os.system("git add -A")
os.system("git commit -m \"Commit.\"")
os.system("git push -u origin master")


