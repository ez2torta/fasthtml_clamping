from fasthtml.common import *


def ProductPage():
    # Cabecera
    header = Header(Div(H1("Detalles del Producto"), cls="header"))

    # Detalles del producto
    product_image = Div(
        Img(src="product-image.jpg", alt="Producto Gourmet"), cls="product-image"
    )
    product_details = Div(
        H2("Sal Saborizada de Ajo y Perejil"),
        P(B("Precio:"), " $8.99"),
        P(
            "Ideal para carnes y vegetales. Nuestra sal gourmet está llena de sabor natural."
        ),
        A("Agregar al carrito", href="carrito.html", cls="add-to-cart"),
        cls="product-details",
    )
    product_container = Div(product_image, product_details, cls="product-container")

    # Promociones relacionadas
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
    promotions = Section(
        H2("Promociones relacionadas"), promo1, promo2, cls="promotions"
    )

    # Productos sugeridos
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
    suggestions = Section(
        H2("También te podría interesar"), suggestion1, suggestion2, cls="suggestions"
    )

    # Pie de página
    footer = Footer(P("Sales y Aliños - Una pizca de sabor y color en tu mesa"))

    # Página completa
    return header, product_container, promotions, suggestions, footer
