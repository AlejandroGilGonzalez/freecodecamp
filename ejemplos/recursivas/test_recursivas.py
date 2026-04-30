def funcionrecursiva(n):
    print("funcion recursiva start con parametro", n)
    n -= 1
    print("numero", n)

    if n > 0:
        funcionrecursiva(n)

    print("funcion recursiva END con parametro", n)

funcionrecursiva(10) 