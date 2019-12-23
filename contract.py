class Contract:
    def __init__(self, company_name, start_date, end_date):
        self.company_name = company_name
        self.start_date = start_date
        self.end_date = end_date
        self.materials = {}

    def add_material(self, material):
        self.materials[material.material_name] = material

    def delete_material(self, material):
        self.materials.pop(material.material_name)

    def update_material(self, material):
        pass
