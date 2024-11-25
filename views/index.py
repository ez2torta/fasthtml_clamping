from fasthtml.common import *

css = Style(
    """
/* styles.css */

body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
    line-height: 1.6;
    color: #333;
}

header {
    background: #f4b41a;
    color: white;
    padding: 20px;
    text-align: center;
}

header .logo h1 {
    margin: 0;
    font-size: 2rem;
}

header nav ul {
    list-style: none;
    padding: 0;
    display: flex;
    justify-content: center;
    gap: 20px;
}

header nav a {
    color: white;
    text-decoration: none;
    font-weight: bold;
}

#hero {
    background: url('hero-image.jpg') no-repeat center center/cover;
    color: white;
    text-align: center;
    padding: 60px 20px;
}

#hero .cta-button {
    display: inline-block;
    background: #333;
    color: white;
    padding: 10px 20px;
    margin-top: 20px;
    text-decoration: none;
    border-radius: 5px;
}

#ofertas,
#productos {
    padding: 40px 20px;
    text-align: center;
}

.oferta,
.producto {
    margin: 20px 0;
}

.precio {
    color: #f4b41a;
    font-weight: bold;
}

footer {
    background: #333;
    color: white;
    text-align: center;
    padding: 20px;
}


@media (max-width: 768px) {

    header,
    footer {
        text-align: center;
    }

    header div {
        flex-direction: column;
    }

    header h1 {
        margin-bottom: 10px;
    }

    .product-container {
        flex-direction: column;
    }

    .product-image,
    .product-details {
        width: 100%;
    }

    .card {
        width: 100%;
        max-width: 300px;
        margin: 10px auto;
    }
}
  
"""
)

js = Script(
    """


"""
)


def Myheader():
    # div logo
    logo_text = H1("Sales y Aliños")
    logo_paragraph = P("Una pizca de sabor y color en tu mesa")
    logo = Div(logo_text, logo_paragraph, cls="logo")
    # nav
    ofertas = Li(A(href="#ofertas"), "Ofertas")
    productos = Li(A(href="#productos"), "Productos")
    contacto = Li(A(href="#contacto"), "Contacto")
    ul = Ul(ofertas, productos, contacto)
    nav = Nav(ul)
    return Header(logo, nav)


def SectionHero():
    h2 = H2("Descubre sabores únicos")
    p = P(
        "Nuestras sales y aliños son el toque perfecto para cualquier plato. ¡Más saludables y llenas de sazón!"
    )
    a = A(
        "Ver Ofertas",
        href="#ofertas",
        cls="cta-button",
    )
    section = Section(h2, p, a, id="hero")
    return section


def Oferta(titulo="", bajada="", precio=""):
    h3 = H3(titulo)
    span = Span(precio)
    p = P(bajada, span, ".")
    div = Div(h3, p, cls="oferta")
    return div


def SectionOfertas():
    h2 = H2("Ofertas del mes")
    oferta1 = Oferta("Pack Gourmet", "3 sales saborizadas por solo ", "20 USD")
    oferta2 = Oferta("Pimienta Premium", "50% de descuento en la segunda unidad", "")
    section = Section(h2, oferta1, oferta2, id="ofertas")
    return section


def Producto(titulo="", bajada="", precio=""):
    h3 = H3(titulo)
    span = Span(precio)
    p = P(bajada, span, ".")
    div = Div(h3, p, cls="oferta")
    return div


def SectionProductos():
    h2 = H2("Nuestros Productos")
    producto1 = Producto("Sales saborizadas", "Perfectas para realzar tus recetas.")
    producto2 = Producto("Pimientas y especias", "Aromas y sabores intensos.")
    producto3 = Producto("Aliños únicos", "Creaciones exclusivas llenas de color.")
    section = Section(h2, producto1, producto2, producto3, id="productos")
    return section


def SocialLinks():
    p = P("Síguenos en:")
    fb = A(
        "Facebook",
        href="https://web.facebook.com/salgourmet.cl/",
        style="margin: 0 10px; color: white; text-decoration: none;",
    )
    ig = A(
        "Instagram",
        href="https://www.instagram.com/salgourmettiajo/",
        style="margin: 0 10px; color: white; text-decoration: none;",
    )
    twi = A(
        "Twitter",
        href="https://x.com/MarySuazo7/",
        style="margin: 0 10px; color: white; text-decoration: none;",
    )
    p2 = P("Una pizca de sabor y color en tu mesa")
    return p, fb, ig, twi, p2


def Myfooter():
    h2 = H2("Contáctanos")
    email = P(
        "Email: ",
        A("salgourmettiajo@gmail.com", href="mailto:salgourmettiajo@gmail.com"),
    )
    telefono = P(
        "Teléfono: ",
        A("+56962046874", href="https://api.whatsapp.com/send?phone=56962046874"),
    )
    siguenos = Div(
        SocialLinks(),
        style="text-align: center; padding: 15px; background: #f4b41a; color: white;",
    )

    footer = Footer(h2, email, telefono, siguenos, id="contacto")
    return footer


def Index():
    header = Myheader()
    section_hero = SectionHero()
    section_ofertas = SectionOfertas()
    section_productos = SectionProductos()
    footer = Myfooter()
    return header, section_hero, section_ofertas, section_productos, footer
    resize_p = P("Resize the viewport and watch the width change", cls="resize")
    viewport = P(cls="viewport")
    viewport_container = Div(viewport, cls="viewport-container")
    width = P(cls="width")
    rect = Div(width, cls="rect")
    clamp = P("width: clamp(250px, 50vw, 600px);", cls="clamp")
    main = Main(
        Div(resize_p, viewport_container, rect, clamp, cls="container"),
        hx_ext="ws",
        ws_connect="/gol",
    )
    footer = Footer(
        P(
            "Tortita (dot) net 2024",
            AX("Github", href="https://github.com/ez2torta", target="_blank"),
        )
    )
    return H1("Clamp () Example", cls="title"), main, footer, js
