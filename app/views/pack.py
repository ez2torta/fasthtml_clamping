from fasthtml.common import *
from app.models import Pack , products
from app.views.common import HeaderSection, FooterSection, ProductsSectionWithTitle


# def get_promotions(product):
#     # Aquí puedes agregar lógica para obtener promociones basadas en el producto
#     return ProductsSectionWithTitle(packs, "Promociones relacionadas")


def get_suggestions(product):
    # Aquí puedes agregar lógica para obtener sugerencias basadas en el producto
    return ProductsSectionWithTitle(products, "También te podría interesar")


def PackPage(pack: Pack):

    # promotions = get_promotions(pack)
    suggestions = get_suggestions(pack)
    # Cabecera
    header = HeaderSection("Detalles del Producto")

    # Detalles del producto
    pack_image = Div(Img(src=pack.get_image_link(), alt=pack.name), cls="pack-image")
    
    pack_details = Div(
        H2(pack.name),
        P(B("Precio:"), f" ${pack.get_price()}"),
        P(pack.get_description()),
        A("Agregar al carrito", href="carrito.html", cls="add-to-cart"),
        cls="pack-details",
    )
    pack_container = Div(pack_image, pack_details, cls="pack-container")

    # Pie de página
    footer = FooterSection()

    # Página completa
    return header, pack_container, suggestions, footer
