from pydantic import BaseModel
from typing import List


class Product(BaseModel):
    name: str
    description: str
    price: float
    image_url: str
    link: str


# Ejemplo de lista de productos
products = [
    Product(
        name="Sal con Romero",
        description="Sal gourmet con romero",
        price=7.99,
        image_url="product1.jpg",
        link="product",
    ),
    Product(
        name="Sal con Pimentón",
        description="Sal gourmet con pimentón",
        price=6.99,
        image_url="product2.jpg",
        link="product",
    ),
    Product(
        name="Pimienta de Jamaica",
        description="Pimienta aromática",
        price=5.50,
        image_url="product3.jpg",
        link="product",
    ),
]


class Offer(BaseModel):
    name: str
    description: str
    price: float
    image_url: str
    link: str


# Ejemplo de lista de ofertas
offers = [
    Offer(
        name="Pack Gourmet",
        description="Compra 2, lleva 3 por solo",
        price=25.00,
        image_url="promo1.jpg",
        link="oferta1.html",
    ),
    Offer(
        name="Pimienta + Sal",
        description="10% de descuento en combinación",
        price=18.00,
        image_url="promo2.jpg",
        link="oferta2.html",
    ),
    Offer(
        name="Sal con Especias",
        description="Descuento del 15% en la compra de 3",
        price=22.50,
        image_url="promo3.jpg",
        link="oferta3.html",
    ),
]
