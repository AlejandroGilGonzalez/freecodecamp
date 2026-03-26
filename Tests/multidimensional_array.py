# Create a multidimensional array with fake football teams:

from random import randint

copa_america = {
    "fase_grupos":{
        "partido 1":{
            "equipo 1":{
                "jugador 1":{
                    "ID":0,
                    "Nombre":"Julio",
                    "Posicion":"Delantero",
                    "Puntuación":""
                },
                "jugador 2":{
                    "ID":0,
                    "Nombre":"Oscar",
                    "Posicion":"Portero",
                    "Puntuación":""                    
                },
                "jugador 3":{
                    "ID":0,
                    "Nombre":"Angel",
                    "Posicion":"Medio",
                    "Puntuación":""                    
                },
                "jugador 4":{
                    "ID":0,
                    "Nombre":"Alex",
                    "Posicion":"Defensa",
                    "Puntuación":""                    
                },
                "jugador 5":{
                    "ID":0,
                    "Nombre":"Gabriel",
                    "Posicion":"Delantero",
                    "Puntuación":""                    
                }
            },
            "equipo 2":{
                "jugador 1":{
                    "ID":0,
                    "Nombre":"Ana",
                    "Posicion":"Delantero",
                    "Puntuación":""
                },
                "jugador 2":{
                    "ID":0,
                    "Nombre":"Olga",
                    "Posicion":"Portero",
                    "Puntuación":""                    
                },
                "jugador 3":{
                    "ID":0,
                    "Nombre":"Celia",
                    "Posicion":"Medio",
                    "Puntuación":""
                },
                "jugador 4":{
                    "ID":0,
                    "Nombre":"Lucia",
                    "Posicion":"Defensa",
                    "Puntuación":""
                },
                "jugador 5":{
                    "ID":0,
                    "Nombre":"Sofia",
                    "Posicion":"Delantero",
                    "Puntuación":""
                }
            }
        },
        "partido 2":{
            "equipo 3":{
                "jugador 1":{
                    "ID":0,
                    "Nombre":"Damian",
                    "Posicion":"Delantero",
                    "Puntuación":""
                },
                "jugador 2":{
                    "ID":0,
                    "Nombre":"Masco",
                    "Posicion":"Portero",
                    "Puntuación":""
                },
                "jugador 3":{
                    "ID":0,
                    "Nombre":"Arnau",
                    "Posicion":"Medio",
                    "Puntuación":""
                },
                "jugador 4":{
                    "ID":0,
                    "Nombre":"Lucian",
                    "Posicion":"Defensa",
                    "Puntuación":""
                },
                "jugador 5":{
                    "ID":0,
                    "Nombre":"Gervo",
                    "Posicion":"Delantero",
                    "Puntuación":""
                }
            },
            "equipo 4":{
                "jugador 1":{
                    "ID":0,
                    "Nombre":"Dione",
                    "Posicion":"Delantero",
                    "Puntuación":""
                },
                "jugador 2":{
                    "ID":0,
                    "Nombre":"Mike",
                    "Posicion":"Portero",
                    "Puntuación":""
                },
                "jugador 3":{
                    "ID":0,
                    "Nombre":"Jose",
                    "Posicion":"Medio",
                    "Puntuación":""
                },
                "jugador 4":{
                    "ID":0,
                    "Nombre":"Santa",
                    "Posicion":"Defensa",
                    "Puntuación":""
                },
                "jugador 5":{
                    "ID":0,
                    "Nombre":"Loco",
                    "Posicion":"Delantero",
                    "Puntuación":""
                }
            }
        },
        "partido 3":{
            "equipo 5":{
                "jugador 1":{
                    "ID":0,
                    "Nombre":"Pesca",
                    "Posicion":"Delantero",
                    "Puntuación":""
                },
                "jugador 2":{
                    "ID":0,
                    "Nombre":"Logra",
                    "Posicion":"Portero",
                    "Puntuación":""
                },
                "jugador 3":{
                    "ID":0,
                    "Nombre":"Rubio",
                    "Posicion":"Medio",
                    "Puntuación":""
                },
                "jugador 4":{
                    "ID":0,
                    "Nombre":"Gonza",
                    "Posicion":"Defensa",
                    "Puntuación":""
                },
                "jugador 5":{
                    "ID":0,
                    "Nombre":"Martin",
                    "Posicion":"Delantero",
                    "Puntuación":""
                }
            },
            "equipo 6":{
                "jugador 1":{
                    "ID":0,
                    "Nombre":"Yeri",
                    "Posicion":"Delantero",
                    "Puntuación":""
                },
                "jugador 2":{
                    "ID":0,
                    "Nombre":"Ivan",
                    "Posicion":"Portero",
                    "Puntuación":""
                },
                "jugador 3":{
                    "ID":0,
                    "Nombre":"Ricar",
                    "Posicion":"Medio",
                    "Puntuación":""
                },
                "jugador 4":{
                    "ID":0,
                    "Nombre":"Sabo",
                    "Posicion":"Defensa",
                    "Puntuación":""
                },
                "jugador 5":{
                    "ID":0,
                    "Nombre":"Clara",
                    "Posicion":"Delantero",
                    "Puntuación":""
                }
            }
        },
        "partido 4":{
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
    } 
}

ide = 1

for partido, equipos in copa_america["fase_grupos"].items():
    for equipo, jugadores in equipos.items():
        for jugador, stats in jugadores.items():
            stats["ID"] = ide
            ide += 1
        for jugador, stats in jugadores.items():
            points = randint(50,99)
            stats["Puntuación"] = points
            print(stats)
        




