class Cart:
    cart_items = []
    
    
    def add_to_cart(self, product):
        self.cart_items.append(product)
        
    def total_cart_value(self):
        values = [item.price for item in self.cart_items]
        print(f"Total cart value is {sum(values)}")
        
    def view_cart_items(self):
        i = 1
        for item in self.cart_items:
            print(f"Cart item {i}: {item.name}")
            i += 1
        
        