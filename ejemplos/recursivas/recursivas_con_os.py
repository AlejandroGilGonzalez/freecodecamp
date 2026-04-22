import os

def listar_ruta_recursivamente(ruta: str, nivel: int = 0) -> None:
    """
    Muestra todos los ficheros y subdirectorios encontrados dentro de ruta.
    """
    try:
        # Leemos el contenido de la carpeta actual y lo ordenamos para que la
        # salida sea más fácil de seguir.
        elementos = sorted(os.listdir(ruta))
    except FileNotFoundError:
        # Si la ruta no existe, mostramos el error y detenemos esta rama.
        print(f'{"  " * nivel}Ruta no encontrada: {ruta}')
        return
    except PermissionError:
        # Si no tenemos permisos para entrar en una carpeta, avisamos y
        # continuamos con el resto del recorrido.
        print(f'{"  " * nivel}Sin permisos: {ruta}')
        return

    for elemento in elementos:
        # Construimos la ruta completa porque elemento solo contiene el
        # nombre dentro de la carpeta actual.
        ruta_completa = os.path.join(ruta, elemento)

        # Mostramos el nombre con sangrado para que se vea en qué nivel de la
        # estructura de carpetas estamos.
        print(f'{"  " * nivel}- {elemento}')

        if os.path.isdir(ruta_completa):
            # Si el elemento es una carpeta, volvemos a llamar a la misma
            # función para explorar su contenido.
            listar_ruta_recursivamente(ruta_completa, nivel + 1)


ruta = "c:\Var\projects\python"
listar_ruta_recursivamente(ruta)