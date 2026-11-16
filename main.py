"""Run a tiny ShopEasy session:  python main.py"""
import auth
import products
import users
from cart import Cart
from checkout import CheckoutService


def main():
    users.create_user(1, "Asha", "asha@example.com")
    products.add_product("MUG", "Coffee mug", 12.50)
    products.add_product("TEE", "T-shirt", 20.00)

    user = auth.login(1)
    cart = Cart(user.user_id)
    cart.add("MUG", 2)
    cart.add("TEE", 1)

    order = CheckoutService().checkout(cart)
    print(f"Order {order.order_id}: status={order.status}, total=${order.total:.2f}")


if __name__ == "__main__":
    main()
