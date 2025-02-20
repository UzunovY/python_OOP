from project.products.base_product import BaseProduct
from project.products.chair import Chair
from project.products.hobby_horse import HobbyHorse
from project.stores.base_store import BaseStore
from project.stores.furniture_store import FurnitureStore
from project.stores.toy_store import ToyStore


class FactoryManager():

    def __init__(self, name: str):
        self.name = name
        self.income: float = 0.0
        self.products: list[BaseProduct] = []
        self.stores: list[BaseStore] = []

    def produce_item(self, product_type: str, model: str, price: float):
        valid_types = {"Chair": Chair, "HobbyHorse": HobbyHorse}

        if product_type not in valid_types:
            raise Exception("Invalid product type!")

        new_product = valid_types[product_type](model, price)
        self.products.append(new_product)

        return f"A product of sub-type {new_product.SUB_TYPE} was produced."

    def register_new_store(self, store_type: str, name: str, location: str):
        valid_types = {"FurnitureStore": FurnitureStore, "ToyStore": ToyStore}

        if store_type not in valid_types:
            raise Exception(f"{store_type} is an invalid type of store!")

        new_store = valid_types[store_type](name, location)
        self.stores.append(new_store)

        return f"A new {store_type} was successfully registered."

    def sell_products_to_store(self, store: BaseStore, *products: BaseProduct):
        if len(products) > store.capacity:
            return f"Store {store.name} has no capacity for this purchase."

        filtered_products = [p for p in products if p.sub_type.upper() in store.store_type.upper()]

        if not filtered_products:
            return "Products do not match in type. Nothing sold."

        for p in filtered_products:
            store.products.append(p)
            store.capacity -= 1
            self.products.remove(p)
            self.income += p.price

        return f"Store {store.name} successfully purchased {len(filtered_products)} items."

    def unregister_store(self, store_name: str):
        store = next((s for s in self.stores if s.name == store_name), None)

        if not store:
            raise Exception("No such store!")

        if store.products:
            return "The store is still having products in stock! Unregistering is inadvisable."

        self.stores.remove(store)
        return f"Successfully unregistered store {store_name}, location: {store.location}."

    def discount_products(self, product_model: str):
        filtered_products = [p for p in self.products if p.model == product_model]

        if filtered_products:
            for p in filtered_products:
                p.discount()

        return f"Discount applied to {len(filtered_products)} products with model: {product_model}"

    def request_store_stats(self, store_name: str):
        store = next((s for s in self.stores if s.name == store_name), None)

        if not store:
            return "There is no store registered under this name!"

        return store.store_stats()

    def statistics(self):
        products_sum_price = sum([p.price for p in self.products])
        result = [f"Factory: {self.name}",
                  f"Income: {self.income:.2f}",
                  "***Products Statistics***",
                  f"Unsold Products: {len(self.products)}. Total net price: {products_sum_price:.2f}"
                  ]

        details = {}
        for p in self.products:
            if p.model not in details:
                details[p.model] = 0
            details[p.model] += 1

        for model, count in sorted(details.items()):
            result.append(f"{model}: {count}")

        result.append(f"***Partner Stores: {len(self.stores)}***")

        sorted_stores = sorted([s.name for s in self.stores])

        for store_name in sorted_stores:
            result.append(f"{store_name}")

        return "\n".join(result).strip()
