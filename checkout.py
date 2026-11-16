"""Checkout: cart -> total -> order -> payment."""
import orders
import pricing
from payments import PaymentGateway


class CheckoutService:
    def __init__(self):
        self.gateway = PaymentGateway()

    def checkout(self, cart):
        total = pricing.calculate_total(cart.subtotal())
        order = orders.create_order(cart.user_id, cart.items, total)
        if self.gateway.charge(cart.user_id, total):
            orders.mark_paid(order)
        return order
