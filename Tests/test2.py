def suma(a,b):
    return a+b

lista = [(1,2),(2,3)]

# Get the tuppled numbers in the list into suma function:

for i in range(len(lista)):
    a,b = lista[i]

x = map(suma,a,b)

print(list(x))