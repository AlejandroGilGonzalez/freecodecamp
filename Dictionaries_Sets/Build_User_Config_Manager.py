test_settings = {'theme': 'dark', 'notifications': 'enabled', 'volume': 'high'}

def add_setting(dic,tup):

    """ Adds new settings to the dictionary """
    
    newtup = tuple(x.lower() for x in tup)
    if newtup[0] in dic.keys():
        return (f"Setting '{newtup[0]}' already exists! Cannot add a new setting with this name.")
    else:
        dic[newtup[0]] = newtup[1]
        return (f"Setting '{newtup[0]}' added with value '{newtup[1]}' successfully!")

def update_setting(dic,tup):

    """Updates the value of a setting"""

    newtup = tuple(x.lower() for x in tup)
    if newtup[0] in dic.keys():
        dic[newtup[0]] = newtup[1]
        return (f"Setting '{newtup[0]}' updated to '{newtup[1]}' successfully!")
    else:
        return (f"Setting '{newtup[0]}' does not exist! Cannot update a non-existing setting.")

def delete_setting(dic,key):
    nkey = key.lower()
    if nkey in dic.keys():
        del dic[nkey]
        return (f"Setting '{nkey}' deleted successfully!")
    else:
        return ("Setting not found!")

def view_settings(dic):
    if len(dic) == 0:
        return ("No settings available.")
    else:
        lines = ["Current User Settings:"]
        for key,value in dic.items():
            lines.append(f"{key.capitalize()}: {value}")
        
        return ("\n".join(lines)+"\n")
        

view_settings(test_settings)
