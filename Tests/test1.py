class Car:

    # Define the initial function:

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

car = Car("Toyota", "Pryus")

for atribute in dir(car):
    if not "__" in atribute and not callable(getattr(car,atribute)):
        value = getattr(car,atribute)
        print(f"{atribute}:{value}")

