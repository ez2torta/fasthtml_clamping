# Aquí dejaré los estilos
from fasthtml.common import *

css = Style(
    """
/* General */
body {
  font-family: Arial, sans-serif;
  margin: 0;
  padding: 0;
  color: #333;
}

h1, h2 {
  color: #f4b41a;
}

/* Header */
.main-header {
  background: #f4b41a;
  color: white;
  text-align: center;
  padding: 20px;
}

.main-header .logo p {
  font-size: 0.9em;
  margin: 5px 0 0;
}

.nav-links {
  list-style: none;
  padding: 0;
  display: flex;
  justify-content: center;
  gap: 20px;
}

.nav-links a {
  color: white;
  text-decoration: none;
  font-weight: bold;
}

.nav-links a:hover {
  text-decoration: underline;
}

/* Sección de Ofertas */
.section-offers {
  text-align: center;
  padding: 20px;
  background: #fff3e0;
}

.offers-container {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 20px;
}

.offer-card {
  border: 1px solid #ddd;
  padding: 15px;
  border-radius: 5px;
  text-align: center;
  max-width: 200px;
}

.offer-card img {
  width: 100%;
  border-radius: 5px;
}

/* Productos */
.section-products {
  padding: 20px;
}

.products-container {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 20px;
}

.product-card {
  border: 1px solid #ddd;
  padding: 15px;
  border-radius: 5px;
  text-align: center;
  max-width: 200px;
}

.product-card img {
  width: 100%;
  border-radius: 5px;
}

/* Contacto */
.section-contact {
  text-align: center;
  padding: 20px;
  background: #f9f9f9;
}

.contact-form input, .contact-form textarea {
  width: 90%;
  max-width: 400px;
  margin: 10px auto;
  padding: 10px;
  border: 1px solid #ddd;
  border-radius: 5px;
  display: block;
}

.contact-form .contact-btn {
  background: #f4b41a;
  color: white;
  padding: 10px 20px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

.contact-form .contact-btn:hover {
  background: #d89c0f;
}

/* Footer */
footer {
  background: #333;
  color: white;
  text-align: center;
  padding: 15px;
  font-size: 0.9em;
}

footer a {
  color: #f4b41a;
  margin: 0 10px;
  text-decoration: none;
}

footer a:hover {
  text-decoration: underline;
}


  
"""
)

js = Script(
    """


"""
)
