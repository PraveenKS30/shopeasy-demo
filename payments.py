"""Talks to the (fake) payment gateway."""
import config


class PaymentGateway:
    def charge(self, user_id, amount):
        """Pretend to charge a card. Always succeeds for amounts under $10,000."""
        print(f"  [gateway] charging user {user_id}: ${amount:.2f} via {config.PAYMENT_GATEWAY_URL}")
        return amount < 10_000
