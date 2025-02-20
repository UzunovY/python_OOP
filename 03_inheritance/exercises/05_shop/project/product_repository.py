from typing import List, Optional

from project.product import Product


class ProductRepository:

    def __init__(self) -> None:
        self.products: List[Product] = []

    def add(self, product: Product) -> None:
        self.products.append(product)

    def find(self, product_name: str) -> Optional[Product]:
        return next((product for product in self.products if product.name == product_name), None)

    def remove(self, product_name: str) -> None:
        if product := self.find(product_name):
            self.products.remove(product)

    def __repr__(self) -> str:
        return "\n".join(f"{product.name}: {product.quantity}" for product in self.products)
