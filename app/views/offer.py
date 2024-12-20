from fasthtml.common import *
from app.models import Offer


def get_promotions(product):
    # Aquí puedes agregar lógica para obtener promociones basadas en el producto
    promo1 = Div(
        Img(src="promo1.jpg", alt="Promo Pack Gourmet"),
        P(B("Pack Gourmet")),
        P("Compra 2, lleva 3 por solo ", Span("$25", cls="highlight")),
        cls="card",
    )
    promo2 = Div(
        Img(src="promo2.jpg", alt="Promo Pimienta"),
        P(B("Pimienta Negra + Sal")),
        P("10% de descuento al combinar."),
        cls="card",
    )
    return Section(H2("Promociones relacionadas"), promo1, promo2, cls="promotions")


def get_suggestions(product):
    # Aquí puedes agregar lógica para obtener sugerencias basadas en el producto
    suggestion1 = Div(
        Img(src="product1.jpg", alt="Sal con Romero"),
        P(B("Sal con Romero")),
        P("Precio: $7.99"),
        A("Ver producto", href="producto.html", cls="add-to-cart"),
        cls="card",
    )
    suggestion2 = Div(
        Img(src="product2.jpg", alt="Sal con Pimentón"),
        P(B("Sal con Pimentón")),
        P("Precio: $6.99"),
        A("Ver producto", href="producto.html", cls="add-to-cart"),
        cls="card",
    )
    return Section(
        H2("También te podría interesar"), suggestion1, suggestion2, cls="suggestions"
    )


def OfferPage(offer: Offer):

    promotions = get_promotions(offer)
    suggestions = get_suggestions(offer)
    # Cabecera
    header = Header(Div(H1("Detalles del Producto"), cls="header"))

    # Detalles del producto
    offer_image = Div(Img(src=offer.image_url, alt=offer.name), cls="offer-image")
    offer_details = Div(
        H2(offer.name),
        P(B("Precio:"), f" ${offer.price}"),
        P(offer.description),
        A("Agregar al carrito", href="carrito.html", cls="add-to-cart"),
        cls="offer-details",
    )
    offer_container = Div(offer_image, offer_details, cls="offer-container")

    # Pie de página
    footer = Footer(P("Sales y Aliños - Una pizca de sabor y color en tu mesa"))

    # Página completa
    return header, offer_container, promotions, suggestions, footer