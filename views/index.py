from fasthtml.common import *

css = Style(
    """
/* General */
body {
  font-family: Arial, sans-serif;
  line-height: 1.6;
  margin: 0;
  padding: 0;
  color: #333;
}

header, footer {
  background: #f4b41a;
  color: white;
  text-align: center;
  padding: 15px;
}

a {
  color: #f4b41a;
  text-decoration: none;
}

a:hover {
  text-decoration: underline;
}

/* Header */
.header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 10px 20px;
}

.header h1 {
  margin: 0;
}

.header form {
  flex: 1;
  margin-left: 20px;
}

.header input {
  width: 100%;
  padding: 5px;
  border-radius: 5px;
  border: none;
}

/* Product Page */
.product-container {
  display: flex;
  flex-wrap: wrap;
  padding: 20px;
  justify-content: center;
}

.product-image, .product-details {
  flex: 1;
  min-width: 300px;
  padding: 10px;
}

.product-image img {
  width: 100%;
  border-radius: 5px;
}

.product-details h2 {
  margin: 0 0 10px;
}

.add-to-cart {
  background: #333;
  color: white;
  padding: 10px 20px;
  text-decoration: none;
  display: inline-block;
  margin-top: 15px;
  border-radius: 5px;
}

.add-to-cart:hover {
  background: #555;
}

/* Table (Shopping Cart) */
table {
  width: 100%;
  border-collapse: collapse;
  margin: 20px auto;
}

th, td {
  border: 1px solid #ddd;
  padding: 10px;
  text-align: center;
}

th {
  background: #f4b41a;
  color: white;
}

.total-label {
  text-align: right;
  font-weight: bold;
}

.total-amount {
  font-size: 1.2em;
  font-weight: bold;
  color: #f4b41a;
}

.action-link {
  color: #f00;
  cursor: pointer;
}

.action-link:hover {
  text-decoration: underline;
}

/* Cards (Promotions and Suggestions) */
.promotions, .suggestions {
  margin: 20px auto;
  width: 90%;
  text-align: center;
}

.card {
  border: 1px solid #ddd;
  padding: 10px;
  display: inline-block;
  width: 200px;
  margin: 10px;
}

.card img {
  width: 100%;
  border-radius: 5px;
}

.card p {
  font-size: 0.9em;
}

.highlight {
  color: #f4b41a;
  font-weight: bold;
}

/* Footer */
footer {
  text-align: center;
  padding: 15px;
  font-size: 0.9em;
}

/* Button */
.checkout-btn {
  background: #f4b41a;
  color: white;
  padding: 10px 20px;
  text-decoration: none;
  display: inline-block;
  border-radius: 5px;
}

.checkout-btn:hover {
  background: #d89c0f;
}

/* Responsive Design */
@media (max-width: 768px) {
  header, footer {
    text-align: center;
  }

  .header div {
    flex-direction: column;
  }

  .header h1 {
    margin-bottom: 10px;
  }

  .product-container {
    flex-direction: column;
  }

  .product-image, .product-details {
    width: 100%;
  }

  .card {
    width: 100%;
    max-width: 300px;
    margin: 10px auto;
  }

  table {
    font-size: 0.9em;
  }

  .checkout-btn {
    width: 100%;
    max-width: 300px;
    text-align: center;
    display: block;
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
