from fasthtml.common import *
import sys
from app.views.viewport import Test
from app.views.index import Index
from app.views.cart import ShoppingCart
from app.views.product import ProductPage
from app.views.pack import PackPage
from app.models import get_pack_by_name, get_product_by_sku, products, packs
from app.logic.shopping_cart import ShoppingCart, BuyerInfo, CartItem

if __name__ == "__main__":
    sys.exit("Run this app with `uvicorn main:app`")


app, rt = fast_app(static_path="static")


def get_or_create_session(sess):
    if not sess.get("user"):
        new_buyer = BuyerInfo(
            name="Jane Doe", email="aun@nolose.com", phone="", address=""
        )
        new_cart = ShoppingCart(buyer_info=new_buyer)
        sess["user"] = {"cart": new_cart.model_dump()}
    return sess


def get_cart_from_session(sess):
    curr_sess = get_or_create_session(sess)
    return ShoppingCart(**curr_sess["user"]["cart"])


def set_cart_from_session(sess, cart):
    curr_sess = get_or_create_session(sess)
    curr_sess["user"]["cart"] = cart


@rt("/product/{sku}")
def get_product(sku: str, sess):
    cart = get_cart_from_session(sess)
    product = get_product_by_sku(sku)
    if product:
        # por algun motivo tengo que hacer esto afuera, debe ser debido al decorador de @rt que pierde su efectividad.
        # esto es solo para los hx_post, que en este caso justo es el formulario de agregar al carrito.
        new_inp = Input(name="quantity", value=1), Hidden(name="sku", value=sku)
        add = Form(
            Group(new_inp, Button("Add")),
            hx_post="/add_to_cart",
            target_id="cart_message",
            hx_swap="innerHTML",
        )
        return ProductPage(product, add)
    else:
        return {"error": "Product not found"}, 404


@app.post("/add_to_cart")
def add_to_cart(quantity: int, sku: str, sess):

    cart = get_cart_from_session(sess)
    breakpoint()
    if True:
        # TODO: buscar el nombre del producto
        cart.add_item(CartItem(name="Sugar", sku=sku, quantity=quantity))
        set_cart_from_session(sess, cart)
    return {
        "message": f"Item: {sku} added to cart with quantity {quantity}",
        "cart": cart,
    }


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
def cart(sess):
    cart = get_cart_from_session(sess)
    return ShoppingCart(cart)


@rt("/viewport")
def get():
    return Test()
