"""A shopping cart: a list of (sku, quantity)."""
import products


class Cart:
    def __init__(self, user_id):
        self.user_id = user_id
        self.items = []          # list of (sku, qty)

    def add(self, sku, qty=1):
        if products.get_product(sku) is None:
            raise ValueError(f"Unknown product: {sku}")
        self.items.append((sku, qty))

    def subtotal(self):
        return sum(products.get_product(sku).price * qty for sku, qty in self.items)
