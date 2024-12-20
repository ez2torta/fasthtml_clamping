from pydantic import BaseModel
from typing import List


class Product(BaseModel):
    sku: str
    name: str
    description: str
    price: int

    def get_image_link(self) -> str:
        return f"/images/{self.sku}.jpg"

    def get_link(self) -> str:
        return f"/product/{self.sku}"


# Ejemplo de lista de productos
products = [
    Product(
        sku="SKU001",
        name="Sal con Romero",
        description="Sal gourmet con romero",
        price=7990,
        image_url="product1.jpg",
    ),
    Product(
        sku="SKU002",
        name="Sal con Pimentón",
        description="Sal gourmet con pimentón",
        price=6990,
        image_url="product2.jpg",
    ),
    Product(
        sku="SKU003",
        name="Pimienta de Jamaica",
        description="Pimienta aromática",
        price=5500,
        image_url="product3.jpg",
    ),
]


class Offer(BaseModel):
    sku: str
    name: str
    description: str
    price: float

    def get_image_link(self) -> str:
        return f"/images/{self.sku}.jpg"

    def get_link(self) -> str:
        return f"/offer/{self.sku}"


# Ejemplo de lista de ofertas
offers = [
    Offer(
        sku="OFFER001",
        name="Pack Gourmet",
        description="Compra 2, lleva 3 por solo",
        price=25000,
        image_url="promo1.jpg",
    ),
    Offer(
        sku="OFFER002",
        name="Pimienta + Sal",
        description="10% de descuento en combinación",
        price=18000,
        image_url="promo2.jpg",
    ),
    Offer(
        sku="OFFER003",
        name="Sal con Especias",
        description="Descuento del 15% en la compra de 3",
        price=22500,
        image_url="promo3.jpg",
    ),
]
