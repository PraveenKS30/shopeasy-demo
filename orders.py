"""Create orders and mark them paid."""
import db
from models import Order

_next_id = 1


def create_order(user_id, items, total):
    global _next_id
    order = Order(_next_id, user_id, items, total)
    _next_id += 1
    db.save("orders", order.order_id, order)
    return order


def mark_paid(order):
    order.status = "PAID"
    db.save("orders", order.order_id, order)


def order_total(order_id):
    """Read the stored total (so discounts must be applied BEFORE the order is saved)."""
    return db.get("orders", order_id).total
