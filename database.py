class Database:
    def __init__(self):
        self.contracts = {}

    def add_contract(self, contract):
        self.contracts[contract.company_name] = contract

    def delete_contract(self, contract):
        self.contracts.pop(contract.company_name)

    def update_contract(self, contract):
        pass