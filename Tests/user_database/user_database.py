from random import randint, sample
import re
import hashlib
import json

# Open the database in json and print the current users:

with open("database.json","r",encoding="utf8") as j:
    data_base = json.load(j)

# Open the dictionary.txt for random name generation:

with open("dics/dics.txt","r", encoding="utf8") as f:
    dictionary = f.read()

# Define login error class:

class ActionError(Exception):

    def __init__(self, action):
        self.action = action
        super().__init__(f"Wrong choice {action}, try again")

# Define login error class:

class LoginError(Exception):

    def __init__(self, user, password):
        self.user = user
        self.password = password


# Define a user class:
 
class User:
    user = ""
    password = ""

    def __init__(self, user, password):

        # Create a random username if no username input:

        if user == "":
            user_name = [word.capitalize() for word in sample(re.findall(r"[a-zA-Z]+",dictionary), 2)]
            user_name = "".join(user_name)
            self.user = user_name

        # If not, use the inputed name:
        
        else:
            self.user = user

        # Use the inputed password encrypted in md5:

        self.password = hashlib.md5(password.encode()).hexdigest()
    

# Create a function for dumping new users into json file:

def create_user(user,password):

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

# Create a function for checking the login:

def login(user, password):
    return ""


# Ask the user for login or create new user:

while True:
    action = input("Choose between (login or create): ")
    if action in ("login","create"):
        break
    else:
        print (f"Wrong choice '{action}', try again \n")


# Asks the user for credentials:

name = input("Choose a username (if empty, a random one will be generated): ")
passw = input("Choose your password: ")

main(name,passw)
