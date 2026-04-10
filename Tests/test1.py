class TooAge(Exception):
    
    error = 101

    def __init__(self, name, age):
        self.age = age
        self.name = name
        super().__init__(f"Error #{self.error}, Too much age {self.age} for dog {self.name}")

    
class InsufficientAge(Exception):

    error = 102

    def __init__(self, name, age):
        self.age = age
        self.name = name
        super().__init__(f"Error #{self.error}, Insuficiente age {self.age} for dog {self.name}")
    

class Dog:

    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def bark(self):
        return (f"{self.name.upper()} says woof woof")

def main(dogs:list) -> str:

    for i in range(len(dogs)):

        name = dogs[i].name
        age = dogs[i].age

        try:
            if age > 20:
                raise TooAge(name,age)
            elif age < 0:
                raise InsufficientAge(name,age)
        except (TooAge,InsufficientAge) as e:
            print(f"Error raised: {e}")
            continue
        
        print(f"The dog {name} has the correct data, therefore {dogs[i].bark()}")


dog1 = Dog("Thunder", 21)
dog2 = Dog("Light", -1)
dog3 = Dog("Puppy", 5)

dogs = [dog1,dog2,dog3]

main(dogs) 

