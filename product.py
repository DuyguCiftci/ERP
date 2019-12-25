class Product:
    def __init__(self, product_name, ingredients, expire_date, quantity):
        self.product_name = product_name
        self.ingredients = ingredients
        self.expire_date = expire_date
        self.quantity = quantity

    def produce(self, storage, amount, storage_2):
        for i in range(amount):
            enable = False
            for material in self.ingredients.items():
                if material[0] in storage.storage_dict.keys():
                    if material[1] <= storage.storage_dict[material[0]].quantity:
                        enable = True
                    else:
                        print("Not enough {0} to produce {1}".format(material[0], self.product_name))
                        enable = False
                        return
                else:
                    enable = False
                    print("No {0} to produce {1}".format(material[0], self.product_name))
                    return
            if enable:
                self.quantity += 1
                storage_2.storage2_dict[self.product_name] = self
                for material in self.ingredients.items():
                    storage.storage_dict[material[0]].quantity -= material[1]



