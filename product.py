class Product:
    def __init__(self, product_name, ingredients, expire_date):
        self.product_name = product_name
        self.ingredients = ingredients
        self.expire_date = expire_date
        self.quantity = 0

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
                else:
                    enable = False
                    print("Not enough {0} to produce {1}".format(material[0], self.product_name))
            if enable:
                self.quantity += 1
                storage_2.storage2_dict[self.product_name] = self
                for material in self.ingredients.items():
                    storage.storage_dict[material[0]].quantity -= material[1]



