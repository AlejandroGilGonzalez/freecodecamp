# Create a multidimensional array with fake football teams:

from random import randint
import json

with open('players_array.json', encoding="utf8") as json_file:
    copas = json.load(json_file)

# Definir el ID y la puntuación de cada jugador:

ide = 1
for partido, equipos in copas["copa_america"]["fase_grupos"].items():
    for team, jugadores in equipos.items():
        for jugador, stats in jugadores.items():
            stats["Puntuación"] = randint(50,99)
            json.dump(copas, open("players_array.json", "w", encoding="utf8"))
            print(jugador,stats)

   

# Definir una función que compare las distintas puntuaciones por clase de jugador:        

def lucha (equipo_local:dict, equipo_visitante:dict):
    
    for jugadores in equipo_local.values():
        for jugador, stats in jugadores.items():
            if stats["Posición"] == equipo_visitante[jugadores][stats]["Posición"]:
                print(yes)

    return ""


