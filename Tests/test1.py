class Car:

    # Define the initial function:

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def example(self):
        print(self.brand.upper())
    

car = Car("Toyota", "Pryus",)

print(car.brand)
print(car.example())

