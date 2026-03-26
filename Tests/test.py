def lucha (equipo_local:dict, equipo_visitante:dict):
 
    for player,jugadores in equipo_local.items():
        jugadores = jugadores
    for player2, jugadores2 in equipo_visitante.items():
        jugadores2 = jugadores2
    
    for player in equipo_local: 
        if jugadores["Posicion"] == "Delantero":
            print("yes")


partido1 = {
    "equipo 7":{
                "jugador 1":{
                    "ID":0,
                    "Nombre":"Dudu",
                    "Posicion":"Delantero",
                    "Puntuación":""
                },
                "jugador 2":{
                    "ID":0,
                    "Nombre":"Juan",
                    "Posicion":"Portero",
                    "Puntuación":""
                },
                "jugador 3":{
                    "ID":0,
                    "Nombre":"Pedro",
                    "Posicion":"Medio",
                    "Puntuación":""
                },
                "jugador 4":{
                    "ID":0,
                    "Nombre":"Paco",
                    "Posicion":"Defensa",
                    "Puntuación":""
                },
                "jugador 5":{
                    "ID":0,
                    "Nombre":"Lolo",
                    "Posicion":"Delantero",
                    "Puntuación":""
                }
                },
    "equipo 8":{
        "jugador 1":{
            "ID":0,
            "Nombre":"Tango",
            "Posicion":"Delantero",
            "Puntuación":""
        },
        "jugador 2":{
            "ID":0,
            "Nombre":"Serpi",
            "Posicion":"Portero",
            "Puntuación":""
        },
        "jugador 3":{
            "ID":0,
            "Nombre":"Ibai",
            "Posicion":"Medio",
            "Puntuación":""
        },
        "jugador 4":{
            "ID":0,
            "Nombre":"Reve",
            "Posicion":"Defensa",
            "Puntuación":""
        },
        "jugador 5":{
            "ID":0,
            "Nombre":"Juanma",
            "Posicion":"Delantero",
            "Puntuación":""
        }
    }
}

lucha(partido1["equipo 7"],partido1["equipo 8"])
