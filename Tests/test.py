from random import randint, sample
import re

# Open the dictionary.txt:

with open("dics/dics.txt","r", encoding="utf8") as f:
    dictionary = f.read()

# Define a user class:
 
class User:
    user = ""
    password = ""

    # Create a random username and password for each user:

    def __init__(self, user, password):
        self.user = "".join(sample(re.findall(r"[a-zA-Z]+",dictionary), 2))
        self.password = randint(1000,9999)
    
    # Stablish login credentials
    
    def login(self, user, password):
        print (user, self.user)
        print (password, self.password)


def main():

    user = User("user","password")

    print(user.user)
    print(user.password)

    return ""

main()