from fasthtml.common import *
import sys
from app.views.viewport import Test
from app.views.index import Index
from app.views.cart import ShoppingCart
from app.views.product import ProductPage
from app.views.offer import OfferPage
from app.models import products, offers

if __name__ == "__main__":
    sys.exit("Run this app with `uvicorn main:app`")


app, rt = fast_app(static_path="static")


def product_dependency(sku):
    for product in products:
        if product.sku == sku:
            return product
    return None


@rt("/product/{sku}")
def get_product(sku):
    product = product_dependency(sku)
    if product:
        return ProductPage(product=product)
    else:
        return {"error": "Product not found"}, 404


def offer_dependency(sku):
    for offer in offers:
        if offer.sku == sku:
            return offer
    return None


@rt("/offer/{sku}")
def get_offer(sku: str):
    offer = offer_dependency(sku)
    if offer:
        return OfferPage(offer=offer)
    else:
        return {"error": "offer not found"}, 404


@rt("/")
def index_site():
    return Index(products=products, offers=offers)


@rt("/cart")
def cart():
    return ShoppingCart()


@rt("/viewport")
def get():
    return Test()
