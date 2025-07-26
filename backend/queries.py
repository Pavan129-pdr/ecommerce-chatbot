def get_order_status(order_id: int):
    # Dummy orders dictionary
    orders = {
        1001: "Your order 1001 is out for delivery.",
        1002: "Your order 1002 has been delivered.",
        1003: "Your order 1003 is being prepared."
    }

    if order_id in orders:
        return {"status": orders[order_id]}
    else:
        return {"status": f"Order {order_id} not found."}

def get_top_products():
    # Dummy top products list
    top_products = ["T-Shirt", "Jeans", "Sneakers"]
    return {"top_products": top_products}

def get_stock(product_name: str):
    # Dummy stock info
    stock = {
        "t-shirt": "In stock",
        "jeans": "Out of stock",
        "sneakers": "Only 2 left"
    }

    status = stock.get(product_name.lower(), "Product not found")
    return {"stock": status}
