class Storage2:
    def __init__(self):
        self.storage2_dict = {}

    def add_product(self, product):
        self.storage2_dict[product.product_name] = product

    def delete_product(self, product):
        self.storage2_dict.pop(product.product_name)