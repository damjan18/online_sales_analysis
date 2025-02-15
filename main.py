from product_manager import ProductManager
from product import Product

pm = ProductManager()

pm.add_product(Product("Pepsi", 1.55, 44))
pm.add_product(Product("Coca Cola", 1.75, 53))
pm.add_product(Product("Doritos", 2.07, 26))
pm.add_product(Product("Sinalco", 1.30, 31))



pm.remove_product("Pepsi")

