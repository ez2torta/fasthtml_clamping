from fasthtml.common import *
import sys
from app.views.viewport import Test
from app.views.index import Index
from app.views.cart import ShoppingCart
from app.views.product import ProductPage
from app.views.pack import PackPage
from app.models import get_pack_by_name, get_product_by_sku, products, packs

if __name__ == "__main__":
    sys.exit("Run this app with `uvicorn main:app`")


app, rt = fast_app(static_path="static")


@rt("/product/{sku}")
def get_product(sku: str):
    product = get_product_by_sku(sku)
    if product:
        return ProductPage(product)
    else:
        return {"error": "Product not found"}, 404


@rt("/pack/{sku}")
def get_pack(sku: str):
    pack = get_pack_by_name(sku)
    if pack:
        return PackPage(pack)
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
