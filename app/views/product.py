from fasthtml.common import *
from app.models import Product, Pack 
from app.views.common import HeaderSection, FooterSection

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


def ProductPage(product: Product):

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
        A("Agregar al carrito", href="carrito.html", cls="add-to-cart"),
        cls="product-details",
    )
    product_container = Div(product_image, product_details, cls="product-container")

    # Pie de página
    footer = FooterSection()

    # Página completa
    return header, product_container, promotions, suggestions, footer
