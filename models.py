"""Plain data classes used across the shop."""
from dataclasses import dataclass, field


@dataclass
class User:
    user_id: int
    name: str
    email: str


@dataclass
class Product:
    sku: str
    name: str
    price: float


@dataclass
class Order:
    order_id: int
    user_id: int
    items: list = field(default_factory=list)   # list of (sku, qty)
    total: float = 0.0
    status: str = "NEW"                          # NEW -> PAID
