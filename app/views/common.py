# Aquí dejaré los estilos
from fasthtml.common import *
from app.models import Product, Pack


# Función para crear el encabezado
def HeaderSection(
    title: str = "Sales y Aliños",
    subtitle: str = "Una pizca de sabor y color en tu mesa",
):
    style = Link(rel="stylesheet", href="/style.css")

    nav_links = Ul(
        Li(A("Inicio", href="/")),
        Li(A("Ofertas", href="/#ofertas")),
        Li(A("Productos", href="/#productos")),
        Li(A("Contacto", href="/#contacto")),
        cls="nav-links",
    )
    logo = Div(H1(title), P(subtitle), nav_links, cls="logo")
    return Header(style, logo, cls="main-header")


# Función para crear una tarjeta de producto
def ProductCard(product: Product):
    return Div(
        Img(src=product.get_image_link(), alt=product.name),
        H3(product.name),
        P(f"Precio: ${int(product.price)}"),
        P(product.description),
        A("Ver Producto", href=product.get_link(), cls="add-to-cart"),
        cls="product-card",
    )


# Función para crear una tarjeta de pack
def PackCard(pack: Pack):
    return Div(
        Img(src=pack.get_image_link(), alt=pack.name),
        H3(pack.name),
        P(f"Precio: ${int(pack.get_price())}"),
        P(pack.get_description()),
        A("Ver Pack", href=pack.get_link(), cls="add-to-cart"),
        cls="pack-card",
    )
    

# Función para crear la sección de packs dinámicamente
def PacksSection(packs: List[Pack]):
    pack_cards = [PackCard(pack) for pack in packs]
    return Section(
        H2("Packs del Mes"),
        Div(*pack_cards, cls="packs-container"),
        cls="section-packs",
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



# Función para crear la sección de productos dinámicamente
def ProductsSection(products: List[Product]):
    product_cards = [ProductCard(product) for product in products]
    return Section(
        H2("Nuestros Productos"),
        Div(*product_cards, cls="products-container"),
        cls="section-products",
    )


def ProductsSectionWithTitle(
    products: List[Product], title: str = "Nuestros Productos"
):
    product_cards = [ProductCard(product) for product in products]
    return Section(
        H2(title),
        Div(*product_cards, cls="products-container"),
        cls="section-products",
    )


# Función para crear el footer
def FooterSection():
    footer_links = Div(
        P("Síguenos en:"),
        A("Facebook", href="https://facebook.com/salgourmet.cl", target="_blank"),
        A("Instagram", href="https://instagram.com/salgourmettiajo", target="_blank"),
        A("Twitter", href="https://twitter.com/MarySuazo7", target="_blank"),
    )
    return Footer(
        footer_links, P("Sales y Aliños - Una pizca de sabor y color en tu mesa")
    )
