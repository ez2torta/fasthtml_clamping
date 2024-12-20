from fasthtml.common import *
import sys
from app.views.viewport import Test
from app.views.index import Index
from app.views.cart import ShoppingCart
from app.views.product import ProductPage
from app.views.pack import PackPage
from app.models import products, packs

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


def pack_dependency(sku):
    for pack in packs:
        if pack.sku == sku:
            return pack
    return None


@rt("/pack/{sku}")
def get_pack(sku: str):
    pack = pack_dependency(sku)
    if pack:
        return PackPage(pack=pack)
    else:
        return {"error": "pack not found"}, 404


@rt("/")
def index_site():
    return Index(products=products, packs=packs)


@rt("/cart")
def cart():
    return ShoppingCart()


@rt("/viewport")
def get():
    return Test()
