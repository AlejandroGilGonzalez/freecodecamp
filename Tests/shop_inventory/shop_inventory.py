#
#
# Create a Shop Inventory:
#
#

import json

# Try to open JSON, if not, create a new dictionary:
try:
    with open("inventory.json", "r", encoding="utf-8") as f:
        inventory = json.load(f)
except:
    inventory = {}


# Create a class for the products:
class Product:

    def __init__(self, name, price, size):
        self.name = name
        self.price = price
        self.size = size
    
    def discount(self):
        if self.name.lower() == "shirt":
            price = int(self.price) * 0.9
            return f"{price:05.2f}"
        elif self.name.lower() == "pants":
            return int(self.price) * 0.8

# Ask user to Insert a new product or create a new one:
action = input ("Create or search? ")

# When choice is create:
if action.lower() == "create":

    while 
    # Asks the user for the product ID:
    ID = input("Enter the product ID: ")

    #If ID already exists return error:
    if not inventory[f"ID_{ID}"]:
        inventory[f"ID_{ID}"] = {}
    else:


    # Asks the user for the atributes:
    atributes = input ("Add Name, Price and Size separated with a comma: ")

    # Converts the atributes into a list:
    atributes = [atribute.strip() for atribute in atributes.split(",")]

    #Creates an object for the product:
    new_object = Product(*atributes)
   
    # Applies the discount with the function:
    discount_price = new_object.discount()
    atributes[1] = discount_price

    # Zips atributes and their name for the dictionary:
    atributes = list(zip(["Name","Price","Size"], atributes))

    # Loops over the atributes to input into the inventory:
    for i in range(len(atributes)):
        inventory[f"ID_{ID}"][atributes[i][0]] = atributes[i][1]

# When choice is search:
elif action.lower() == "search":

    # Asks the user for the products ID:
    ID = f"ID_{input("Enter the products ID: ")}"
    
    # Searches for the specific ID in the inventory and prints it:
    for key,value in inventory[ID].items():
        print(f"{key} --> {value}")


with open("inventory.json", "w", encoding="utf-8") as f:
    json.dump(inventory, f, indent=4)