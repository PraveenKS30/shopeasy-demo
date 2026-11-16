"""Price math. calculate_total is where a discount code would plug in."""
import config


def calculate_total(subtotal):
    """subtotal + tax + shipping."""
    tax = subtotal * config.TAX_RATE
    return round(subtotal + tax + config.SHIPPING_FLAT, 2)
