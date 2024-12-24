from typing import List, Optional, Dict
from pydantic import BaseModel, EmailStr, Field
import random
import string

class CartItem(BaseModel):
    name: str
    sku: str
    quantity: int = Field(..., ge=1, description="Quantity must be at least 1")

class BuyerInfo(BaseModel):
    name: str
    email: EmailStr
    phone: str
    address: str

class ShoppingCart(BaseModel):
    items: List[CartItem] = []
    order_code: str = Field(default_factory=lambda: ''.join(random.choices(string.ascii_uppercase + string.digits, k=6)))
    buyer_info: BuyerInfo

    def add_item(self, item: CartItem):
        """Adds an item to the cart."""
        self.items.append(item)

    def remove_item(self, sku: str):
        """Removes an item from the cart by SKU."""
        self.items = [item for item in self.items if item.sku != sku]

    def update_item_quantity(self, sku: str, quantity: int):
        """Updates the quantity of a specific item in the cart."""
        for item in self.items:
            if item.sku == sku:
                item.quantity = quantity
                break

    def calculate_total(self, pricing: Dict[str, float]) -> float:
        """Calculates the total cost of the cart given a pricing dictionary."""
        return sum(pricing[item.sku] * item.quantity for item in self.items if item.sku in pricing)

    def check_stock(self, stock: Dict[str, int]) -> Dict[str, bool]:
        """Checks if the items in the cart are in stock based on the provided stock dictionary."""
        stock_status = {}
        for item in self.items:
            stock_status[item.sku] = stock.get(item.sku, 0) >= item.quantity
        return stock_status

# Example usage
if __name__ == "__main__":
    buyer = BuyerInfo(name="John Doe", email="john.doe@example.com", phone="+123456789", address="123 Main St")
    cart = ShoppingCart(buyer_info=buyer)
    
    cart.add_item(CartItem(name="Salt", sku="SKU123", quantity=2))
    cart.add_item(CartItem(name="Pepper", sku="SKU124", quantity=1))
    print(cart)

    cart.update_item_quantity("SKU123", 3)
    print(cart)

    cart.remove_item("SKU124")
    print(cart)

    # Assuming pricing is defined as follows:
    pricing = {"SKU123": 5.0, "SKU124": 3.0}
    print(f"Total: ${cart.calculate_total(pricing):.2f}")

    # Assuming stock is defined as follows:
    stock = {"SKU123": 5, "SKU124": 0}
    print(f"Stock status: {cart.check_stock(stock)}")

