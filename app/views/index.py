from fasthtml.common import *
from app.models import Offer, Product


# Función para crear el encabezado
def HeaderSection():
    logo = Div(
        H1("Sales y Aliños"), P("Una pizca de sabor y color en tu mesa"), cls="logo"
    )
    nav_links = Ul(
        Li(A("Ofertas", href="#ofertas")),
        Li(A("Productos", href="#productos")),
        Li(A("Contacto", href="#contacto")),
        cls="nav-links",
    )
    return Header(logo, Nav(nav_links), cls="main-header")


# Función para crear una tarjeta de oferta
def OfferCard(offer: Offer):
    return Div(
        Img(src=offer.image_url, alt=offer.name),
        H3(offer.name),
        P(f"Precio: ${int(offer.price)}"),
        P(offer.description),
        A("Ver Oferta", href=offer.get_link(), cls="add-to-cart"),
        cls="offer-card",
    )


# Función para crear la sección de ofertas dinámicamente
def OffersSection(offers: List[Offer]):
    offer_cards = [OfferCard(offer) for offer in offers]
    return Section(
        H2("Ofertas del Mes"),
        Div(*offer_cards, cls="offers-container"),
        cls="section-offers",
    )


# Función para crear una tarjeta de producto
def ProductCard(product: Product):
    return Div(
        Img(src=product.image_url, alt=product.name),
        H3(product.name),
        P(f"Precio: ${int(product.price)}"),
        P(product.description),
        A("Ver Producto", href=product.get_link(), cls="add-to-cart"),
        cls="product-card",
    )


# Función para crear la sección de productos dinámicamente
def ProductsSection(products: List[Product]):
    product_cards = [ProductCard(product) for product in products]
    return Section(
        H2("Nuestros Productos"),
        Div(*product_cards, cls="products-container"),
        cls="section-products",
    )


# Función para crear el formulario de contacto
def ContactForm():
    return Form(
        Input(type="text", placeholder="Tu nombre", required=True),
        Input(type="email", placeholder="Tu correo electrónico", required=True),
        Textarea(placeholder="Tu mensaje", required=True),
        Button("Enviar", type="submit", cls="contact-btn"),
        cls="contact-form",
    )


# Función para crear la sección de contacto
def ContactSection():
    contact_form = ContactForm()
    return Section(
        H2("Contacto"),
        P("¿Tienes preguntas? Escríbenos y descubre más sobre nuestros productos."),
        contact_form,
        cls="section-contact",
    )


# Función para crear el footer
def FooterSection():
    footer_links = Div(
        P("Síguenos en:"),
        A("Facebook", href="https://facebook.com", target="_blank"),
        A("Instagram", href="https://instagram.com", target="_blank"),
        A("Twitter", href="https://twitter.com", target="_blank"),
    )
    return Footer(
        footer_links, P("Sales y Aliños - Una pizca de sabor y color en tu mesa")
    )


# Función para crear el índice con productos dinámicos
def Index(offers: List[Offer], products: List[Product]):
    return (
        HeaderSection(),  # Sección de encabezado
        OffersSection(offers),  # Sección de ofertas con datos dinámicos
        ProductsSection(products),  # Sección de productos con datos dinámicos
        ContactSection(),  # Sección de contacto
        FooterSection(),  # Sección de footer
    )
