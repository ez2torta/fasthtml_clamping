from fasthtml.common import *
import sys
from app.views.viewport import Test
from app.views.common import css
from app.views.index import Index
from app.views.cart import ShoppingCart
from app.views.product import ProductPage
from app.models import products, offers

if __name__ == "__main__":
    sys.exit("Run this app with `uvicorn main:app`")


app = FastHTML(hdrs=(css))
rt = app.route


@rt("/")
def index_site():
    return Index(products=products, offers=offers)


@rt("/cart")
def cart():
    return ShoppingCart()


@rt("/product")
def get_product():
    return ProductPage()


@rt("/viewport")
def get():
    return Test()
