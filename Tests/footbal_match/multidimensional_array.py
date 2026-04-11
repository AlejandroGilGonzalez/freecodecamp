# Create a multidimensional array with fake football teams:

from random import randint
import json

class Team:

    def __init__(self, name):
        self.name = name.upper()

class Player:
    pass



# Open the Json file with the starting teams and players:

with open('players_array.json', "r", encoding="utf-8") as json_file:
    copas = json.load(json_file)

# Convert every team and player into objects:

teams = []
players = []

# Loops through every match and team in those matches:

for partido, equipos in copas["copa_america"]["fase_grupos"].items():

    # Loops through every player in each team:
    
    for team, jugadores in equipos.items():

        # Creates an object for each team:

        team_obj = Team(f"{team}")
        teams.append(team_obj)

        for jugador, stats in jugadores.items():

        # Creates an object for each player:
            
            player_obj = Player()
            players.append(player_obj)

            for key, value in stats.items():
                setattr(player_obj, key, value)

            
print(team)



    

# Saves changes in the json:

#with open("players_array.json", "w", encoding="utf-8") as f:
#    json.dump(copas, f, ensure_ascii=False, indent=4)
            

# Function that compares players punctuation by same position:        

def lucha (equipo_local:dict, equipo_visitante:dict):
    
    for jugadores in equipo_local.values():
        for jugador, stats in jugadores.items():
            for i in range(len(jugadores.keys())):
                print(jugador)
    return ""


