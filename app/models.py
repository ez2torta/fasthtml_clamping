from pydantic import BaseModel
import json


class Product(BaseModel):
    sku: str
    name: str
    description: str
    price: float
    bajada: str
    categorias: list[str]
    etiquetas: list[str]
    fecha_de_publicacion: str
    estado: str
    foto_producto: str

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            sku=data["SKU"],
            name=data["Nombre"],
            description=data["Descripción"],
            price=float(data["Precio"].replace("$", "").replace(",", "")),
            bajada=data["Bajada (Resumen)"],
            categorias=data["Categorías (Separado por Comas)"].split(","),
            etiquetas=data["Etiquetas"].split(", "),
            fecha_de_publicacion=data["Fecha de Publicación"],
            estado=data["Estado (Publicado/No Publicado)"],
            foto_producto=data["Foto Producto"],
        )

    def get_image_link(self) -> str:
        return f"/{self.foto_producto}"

    def get_link(self) -> str:
        return f"/product/{self.sku}"


json_products = json.load(open("./app/json_files/productos.json"))
products = [Product.from_dict(prod_dict) for prod_dict in json_products]


class Pack(BaseModel):
    name: str
    products: list[Product]

    @classmethod
    def from_dict(cls, data: dict, products: list[Product]):
        product_skus = [data["SKU1"], data["SKU2"], data["SKU3"]]
        pack_products = [prod for prod in products if prod.sku in product_skus]
        return cls(name=data["Nombre Pack"], products=pack_products)

    def get_image_link(self) -> str:
        return f"/images/packs/{self.name.replace(' ', '_')}.jpg"

    def get_link(self) -> str:
        return f"/pack/{self.name.replace(' ', '_')}"
    
    def get_price(self) -> float:
        return sum([prod.price for prod in self.products])
    
    def get_description(self) -> str:
        return " + ".join([prod.name for prod in self.products])


json_packs = json.load(open("./app/json_files/packs.json"))
packs = [Pack.from_dict(pack_dict, products) for pack_dict in json_packs]
