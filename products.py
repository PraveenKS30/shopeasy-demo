"""Product catalog."""
import db
from models import Product


def add_product(sku, name, price):
    product = Product(sku, name, price)
    db.save("products", sku, product)
    return product


def get_product(sku):
    return db.get("products", sku)
