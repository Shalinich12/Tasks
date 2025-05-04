# oops
class Product:
    def __init__(self, name, price, stock):        
        self.name = name
        self.price = price
        self.stock = stock
    def sell(self, quantity):
        self.stock -= quantity
class Phone(Product):
    def __init__(self, name, price, stock, brand, model):
        super().__init__(name, price, stock)
        self.brand = brand
        self.model = model
class Tablet(Product):
    def __init__(self, name, price, stock, brand, model, screen_size):  
        super().__init__(name, price, stock)
        self.screen_size = screen_size

P1=Product("IPhone",80000,10)
P2=Product("Samsung",70000,15)

print("Before Sale:")
print(P1.name, "Price:", P1.price, "Stock:", P1.stock)

# Reduce stock
P1.sell(2)

# Print after sale
print("After Sale:")
print(P1.name, "Price:", P1.price, "Stock:", P1.stock)