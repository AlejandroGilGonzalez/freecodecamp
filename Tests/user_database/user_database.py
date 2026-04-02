from random import randint, sample
import re
import hashlib
import json

# Open the database in json and print the current users:

with open("database.json","r",encoding="utf8") as j:
    data_base = json.load(j)

for users, credentials in data_base["users"].items():
    print(users)
    print(credentials,"\n")

# Define a user class:
 
class User:
    user = ""
    password = ""

    def __init__(self, user, password):

        # Open the dictionary.txt for random name generation:

        with open("dics/dics.txt","r", encoding="utf8") as f:
            dictionary = f.read()

        # Create a random username if no username input:

        if user == "":
            user_name = [w.capitalize() for w in sample(re.findall(r"[a-zA-Z]+",dictionary), 2)]
            user_name = "".join(user_name)
            self.user = user_name

        # If not, use the inputed name:
        
        else:
            self.user = user

        # Use the inputed password encrypted in md5:

        self.password = hashlib.md5(password.encode()).hexdigest()
    

# Create a function for dumping new users into json file:

def main(user,password):

    # Defines the user we are inputing: 

    main_user = User(user, password)

    # Defines the user number:

    new_id = len(data_base["users"]) + 1

    # Defines the new user credentials:

    user_credentials = {f"user{new_id}_id":main_user.user, f"user{new_id}_password":main_user.password}

    # Attaches the new user to the dictionary:

    data_base["users"][f"user{new_id}"] = user_credentials
    
    # Dumps the new info into json database:
     
    with open("database.json","w",encoding="utf8") as f:
        json.dump(data_base, f, indent=4)

    return ""

# Asks the user for credentials:

name = input("Introduzca su nombre: ")
passw = input("Introduzca su password: ")

main(name,passw)
