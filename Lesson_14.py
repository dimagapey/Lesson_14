# Частично сделал
import csv

class Product:
    def __init__(self, name, product_type, price):
        self.name = name
        self.product_type = self._check_product_type(product_type)
        self.price = float(price)

    def _check_product_type(self, product_type):
        if product_type == 'tea':
            return 'tea'
        if product_type == 'coffee':
            return 'coffee'

    def print_product(self):
            print(f"Name: {self.name}, Product_type: {self._check_product_type}, Price: {self.price}")



class Store:
    def __init__(self):
        self.warehouse = self.import_product()
        self.transactions = []

    def import_product(self):
        with open('inventory.csv', newline = '', encoding='utf-8') as inventory:
            csv_reader = csv.DictReader(inventory, delimiter=',')
            for row in csv_reader:
                print(row['Тип'], ':', row['Наименование'], row['Цена'])

    def all_price(self):
        pass

    def sell_product(self):
        pass


my_store = Store
my_store.import_product()

