from fasthtml.common import *
import asyncio
import sys
from views.viewport import Test
from views.index import Index, css
from views.cart import ShoppingCart
from views.product import ProductPage

if __name__ == "__main__":
    sys.exit("Run this app with `uvicorn main:app`")


app = FastHTML(hdrs=(css))
rt = app.route


@rt("/")
def index_site():
    return Index()

@rt("/cart")
def cart():
    return ShoppingCart()

@rt("/product")
def get_product():
    return ProductPage()
@rt("/viewport")
def get():
    return Test()
