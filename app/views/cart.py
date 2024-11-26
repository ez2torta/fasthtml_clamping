from fasthtml.common import *


def ShoppingCart():
    # Cabecera
    header = Header(Div(H1("Carrito de Compras"), cls="header"))

    # Tabla del carrito
    table_header = Tr(
        Th("Producto"), Th("Cantidad"), Th("Precio Unitario"), Th("Total"), Th("Acción")
    )

    # Filas de productos
    product_row1 = Tr(
        Td("Sal Saborizada de Ajo y Perejil"),
        Td("1"),
        Td("$8.99"),
        Td("$8.99"),
        Td(A(href="#", inner="Eliminar", cls="action-link")),
    )
    product_row2 = Tr(
        Td("Pimienta Negra Premium"),
        Td("2"),
        Td("$5.50"),
        Td("$11.00"),
        Td(A(href="#", inner="Eliminar", cls="action-link")),
    )

    table_footer = Tr(
        Td("Total", colspan="3", cls="total-label"),
        Td("$19.99", colspan="2", cls="total-amount"),
    )

    table = Table(
        Thead(table_header), Tbody(product_row1, product_row2), Tfoot(table_footer)
    )

    # Promociones
    promo1 = Div(
        Img(src="promo1.jpg", alt="Promo Pack Gourmet"),
        P(B("Pack Gourmet")),
        P("Compra 2, lleva 3 por solo ", Span("$25", cls="highlight")),
        cls="card",
    )
    promo2 = Div(
        Img(src="promo2.jpg", alt="Promo Pimienta"),
        P(B("Pimienta y Sal")),
        P("10% de descuento en combinación."),
        cls="card",
    )
    promotions = Section(H2("Promociones Especiales"), promo1, promo2, cls="promotions")

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
        H2("Te podrían interesar"), suggestion1, suggestion2, cls="suggestions"
    )

    # Botón de checkout
    checkout_button = Div(
        A("Finalizar Compra", href="checkout.html", cls="checkout-btn"),
        style="text-align: center;",
    )

    # Pie de página
    footer = Footer(P("Sales y Aliños - Una pizca de sabor y color en tu mesa"))

    # Página completa
    return header, table, promotions, suggestions, checkout_button, footer
