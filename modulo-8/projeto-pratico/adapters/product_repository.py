import csv
import os
from entities.product import Product

PRODUCTS_FILE = 'products.csv'

class ProductRepository:
    def load_products(self):
        """
        Carrega os produtos do arquivo CSV para uma lista de Product.
        Saída: Lista de Product.
        """
        products = []
        if os.path.exists(PRODUCTS_FILE):
            with open(PRODUCTS_FILE, mode='r', newline='') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    products.append(Product(row['id'], row['name'], float(row['price']), int(row['quantity'])))
        return products

    def save_products(self, products):
        """
        Salva a lista de Product no arquivo CSV.
        Entrada: Lista de Product.
        """
        with open(PRODUCTS_FILE, mode='w', newline='') as file:
            fieldnames = ['id', 'name', 'price', 'quantity']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for prod in products:
                writer.writerow({'id': prod.id, 'name': prod.name, 'price': prod.price, 'quantity': prod.quantity})