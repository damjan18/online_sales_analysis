class ProductManager:
    products = []
    
    def add_product(self, product):
        self.products.append(product)
        
    def all_products(self):
        i = 1
        for product in self.products:
            print(f"Product {i}: {product.name}")
            i += 1
            
    def total_value(self):
        prod_value = [product.price * product.quantity for product in self.products]
        print(f"Total product value is: {sum(prod_value)}")
        
        
    def remove_product(self, name):
        for product in self.products:
            if product.name == name:
                self.products.remove(product)