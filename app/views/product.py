from fasthtml.common import *
from app.models import Product, Pack
from app.views.common import (
    HeaderSection,
    FooterSection,
    get_random_promotion,
    get_random_suggestion,
)


def get_promotions(product):
    # Aquí puedes agregar lógica para obtener promociones basadas en el producto
    promo1 = get_random_promotion(product)
    promo2 = get_random_promotion(product)
    return Section(H2("Promociones relacionadas"), promo1, promo2, cls="promotions")


def get_suggestions(product):
    # Aquí puedes agregar lógica para obtener sugerencias basadas en el producto
    suggestion1 = get_random_suggestion(product)
    suggestion2 = get_random_suggestion(product)
    return Section(
        H2("También te podría interesar"), suggestion1, suggestion2, cls="suggestions"
    )


def ProductPage(product: Product, add_to_cart_button):

    promotions = get_promotions(product)
    suggestions = get_suggestions(product)
    # Cabecera
    header = HeaderSection("Detalles del Producto")

    # Detalles del producto
    product_image = Div(
        Img(src=product.get_image_link(), alt=product.name), cls="product-image"
    )

    product_details = Div(
        H2(product.name),
        P(B("Precio:"), f" ${product.price}"),
        P(product.description),
        add_to_cart_button,
        Div(id="cart_message", cls="cart-message"),
        cls="product-details",
    )
    product_container = Div(product_image, product_details, cls="product-container")

    # Pie de página
    footer = FooterSection()

    # Página completa
    return header, product_container, promotions, suggestions, footer
