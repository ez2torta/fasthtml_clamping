# Tests
from app.logic.shopping_cart import BuyerInfo, CartItem, ShoppingCart


def test_add_item():
    buyer = BuyerInfo(
        name="Jane Doe",
        email="jane.doe@example.com",
        phone="+987654321",
        address="456 Another St",
    )
    cart = ShoppingCart(buyer_info=buyer)
    cart.add_item(CartItem(name="Sugar", sku="SKU125", quantity=2))
    assert len(cart.items) == 1
    assert cart.items[0].name == "Sugar"


def test_remove_item():
    buyer = BuyerInfo(
        name="Jane Doe",
        email="jane.doe@example.com",
        phone="+987654321",
        address="456 Another St",
    )
    cart = ShoppingCart(buyer_info=buyer)
    cart.add_item(CartItem(name="Sugar", sku="SKU125", quantity=2))
    cart.add_item(CartItem(name="Tea", sku="SKU126", quantity=1))
    cart.remove_item("SKU125")
    assert len(cart.items) == 1
    assert cart.items[0].sku == "SKU126"


def test_update_item_quantity():
    buyer = BuyerInfo(
        name="Jane Doe",
        email="jane.doe@example.com",
        phone="+987654321",
        address="456 Another St",
    )
    cart = ShoppingCart(buyer_info=buyer)
    cart.add_item(CartItem(name="Sugar", sku="SKU125", quantity=2))
    cart.update_item_quantity("SKU125", 5)
    assert cart.items[0].quantity == 5


def test_calculate_total():
    buyer = BuyerInfo(
        name="Jane Doe",
        email="jane.doe@example.com",
        phone="+987654321",
        address="456 Another St",
    )
    cart = ShoppingCart(buyer_info=buyer)
    cart.add_item(CartItem(name="Sugar", sku="SKU125", quantity=2))
    cart.add_item(CartItem(name="Tea", sku="SKU126", quantity=1))
    pricing = {"SKU125": 3.0, "SKU126": 5.0}
    assert cart.calculate_total(pricing) == 11.0


def test_check_stock():
    buyer = BuyerInfo(
        name="Jane Doe",
        email="jane.doe@example.com",
        phone="+987654321",
        address="456 Another St",
    )
    cart = ShoppingCart(buyer_info=buyer)
    cart.add_item(CartItem(name="Sugar", sku="SKU125", quantity=2))
    cart.add_item(CartItem(name="Tea", sku="SKU126", quantity=1))
    stock = {"SKU125": 3, "SKU126": 0}
    stock_status = cart.check_stock(stock)
    assert stock_status == {"SKU125": True, "SKU126": False}
