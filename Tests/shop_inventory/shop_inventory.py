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

    def __init__(self, name, price,size):
        self.name = name
        self.price = price
        self.size = size
    
    def discount(self):
        if self.name.lower() == "shirt":
            price = int(self.price) * 0.9
            return f"${price:05.2f}"
        elif self.name.lower() == "pants":
            price = int(self.price) * 0.8
            return f"${price:05.2f}"

# Ask user to Insert a new product or create a new one:
action = input ("Create or search? ")

# When choice is create:
if action.lower() == "create":

    while True:

        # Asks the user for the product ID:
        ID = input("Enter the product ID: ")
        ID = f"ID_{ID}"

        #If ID already exists return error:
        if ID in inventory:
            print("ID already exists in the system, try again.")

        #If it doesn't exist, create it:
        else:
            inventory[ID] = {}
            break
    
    while True:

        # Asks the user for the required atributes:
        required_atributes = ["name","price","size"]
        atributes = input ("Add Name, Price and Size separated with a comma: ")

        # Converts the atributes into a list:
        atributes = [atribute.strip() for atribute in atributes.split(",")]

        if len(atributes) < len(required_atributes):
            print("Some atribute is missing")
            continue
        else:
            break

    #Creates an object for the product:
    new_object = Product(*atributes)        
    
    # Applies the discount with the function:
    discount_price = new_object.discount()
    setattr(new_object,"price",discount_price)

    # Loops over the atributes to input into the inventory:
    for attr in dir(new_object):
        if not attr.startswith("__") and not callable(getattr(new_object,attr)):
            value = getattr(new_object, attr)
            
            # Adds to the inventory
            inventory[ID][attr] = value

# When choice is search:
elif action.lower() == "search":

    while True:
        # Asks the user for the products ID:
        ID = input("Enter the products ID: ")
        ID = f"ID_{ID}"

        # Check if the product exists:
        if ID not in inventory:
            print(f"{ID} not actually in inventory.")
            continue
        else:
            break
    
    # Searches for the specific ID in the inventory and prints it:
    for key,value in inventory[ID].items():
        print(f"{key} --> {value}")


with open("inventory.json", "w", encoding="utf-8") as f:
    json.dump(inventory, f, indent=4)