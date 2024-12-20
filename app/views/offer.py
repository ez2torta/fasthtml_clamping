from fasthtml.common import *
from app.models import Offer, offers, products
from app.views.common import HeaderSection, FooterSection, ProductsSectionWithTitle


def get_promotions(product):
    # Aquí puedes agregar lógica para obtener promociones basadas en el producto
    return ProductsSectionWithTitle(offers, "Promociones relacionadas")


def get_suggestions(product):
    # Aquí puedes agregar lógica para obtener sugerencias basadas en el producto
    return ProductsSectionWithTitle(products, "También te podría interesar")


def OfferPage(offer: Offer):

    promotions = get_promotions(offer)
    suggestions = get_suggestions(offer)
    # Cabecera
    header = HeaderSection("Detalles del Producto")

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
    footer = FooterSection()

    # Página completa
    return header, offer_container, promotions, suggestions, footer
