class Storage:
    def __init__(self):
        self.storage_dict = {}

    def add_material(self, material):
        self.storage_dict[material.material_name] = material

    def delete_material(self, material):
        self.storage_dict.pop(material.material_name)