
class InsufficientAge(Exception):
    error_number = 101
    age = 98
    
    # Utilizamos SELF porque sino 

    def __init__(self, age):
        self.age = age * 2
        super().__init__(f'error #{self.error_number}: Insufficient age: {self.age} years old')

class TooAge(Exception):
    error_number = 102
    age = 103

    def __init__(self, age):
        # global age = 101 # Definida asi de forma global.
        # age = 102 # Porque estamos pasando 102 en el raise.
        # self.age = 103 # Porque está definida asi en la clase.

        super().__init__(f'error #{self.error_number}: Too much age: {age} years old')

class clase_ejemplo():
    nombre = ""

    def __init__(self,nombre_que_asignas,edad):
        self.nombre = nombre_que_asignas
        self.edad = edad

    def saludo(self):
        print(f"hola {self.nombre} tienes {self.edad}")

age = 101
ejemplo_objeto_1 = clase_ejemplo("Alex",27)
ejemplo_objeto_2 = clase_ejemplo("Oscar",44)
ejemplo_objeto_1.saludo()
ejemplo_objeto_2.saludo()

def main():
    
    try:
        if age < 0:
            raise InsufficientAge(age)

        if age > 100:
            raise TooAge(102)
    except (InsufficientAge,TooAge) as e:
        print(f"error raised:{e}")

# main()
# print (f"age = {age}")