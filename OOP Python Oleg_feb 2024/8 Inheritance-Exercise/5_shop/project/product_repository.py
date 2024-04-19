from typing import List, Optional

from project import Product


class ProductRepository: # tova e Mixin

    def __init__(self):
        self.products: List[Product] = []

    def add(self, product: Product) -> None:
        self.products.append(product) # adds a product to the  repository

    def find(self, product_name: str) -> Optional[Product]:  # returns  a product(object) with that name
        for p in self.products:
            if p.name == product_name:
                return p

    def remove(self, product_name):  # removes a productfrom the repository
        product = self.find(product_name)
        if product:
            self.products.remove(product)

    def __repr__(self): # override the method, so it returns information for all products in the repository:
        return"\n".join([f"{p.name}: {p.quantity}" for p in self.products])
