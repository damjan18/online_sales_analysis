class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = float(price)
        self.quantity = int(quantity)
        
    def product_info(self):
        print(f"- Product: {self.name}\nPrice: {self.price}\nQuantity: {self.quantity}")
        
    def add_or_subtract_quantity(self, number):
        add_or_sub = input(f"Press '+' if you want to add or '-' if you want to subtract.")
        if add_or_sub == "+":
            self.quantity += number
        elif add_or_sub == "-":
            self.quantity -= number
        else:
            print("You can only enter '+' or '-'!")
            
        print(f"Quantity: {self.quantity}")
            
            
        