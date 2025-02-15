from product_manager import ProductManager
from product import Product

pm = ProductManager()

pm.add_product(Product("Pepsi", 1.55, 40))
pm.add_product(Product("Coca Cola", 1.75, 55))
pm.add_product(Product("Doritos", 2.07, 25))
pm.add_product(Product("Sinalco", 1.30, 35))

pm.all_products()
pm.total_value()

pm.remove_product("Pepsi")
pm.all_products()
