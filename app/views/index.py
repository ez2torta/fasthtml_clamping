from fasthtml.common import *
from app.models import Offer, Product
from app.views.common import (
    HeaderSection,
    ContactForm,
    OffersSection,
    ProductsSection,
    FooterSection,
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


# Función para crear el índice con productos dinámicos
def Index(offers: List[Offer], products: List[Product]):
    return (
        HeaderSection(),  # Sección de encabezado
        OffersSection(offers),  # Sección de ofertas con datos dinámicos
        ProductsSection(products),  # Sección de productos con datos dinámicos
        ContactSection(),  # Sección de contacto
        FooterSection(),  # Sección de footer
    )
