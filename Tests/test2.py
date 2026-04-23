def carga():
    lista = []
    for i in range(4):
        numero = input("Introduzca un número: ")
        lista.append(int(numero))
    return lista

def mayor(lista):
    mayor = 0
    for i in range(len(lista)):
        if lista[i]>mayor:
            mayor = lista[i]
    
    return mayor

def suma(lista):
    return sum(lista)



