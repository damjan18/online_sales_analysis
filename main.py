from product_manager import ProductManager
from product import Product
from cart import Cart
import random

ct = Cart()
pm = ProductManager()

pm.add_product(Product("Pepsi", 1.55, 40))
pm.add_product(Product("Coca Cola", 1.75, 55))
pm.add_product(Product("Doritos", 2.07, 25))
pm.add_product(Product("Sinalco", 1.30, 35))
pm.add_product(Product("Fanta", 1.70, 60))
pm.add_product(Product("Sprite", 1.80, 43))

pm.add_product(Product("Pepsi", 1.55, 44))
pm.add_product(Product("Coca Cola", 1.75, 53))
pm.add_product(Product("Doritos", 2.07, 26))
pm.add_product(Product("Sinalco", 1.30, 31))



pm.remove_product("Pepsi")


for i in range(0,3):
    ct.add_to_cart(random.choice(pm.products))
ct.view_cart_items()
ct.total_cart_value()