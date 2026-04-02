from random import randint, sample
import re

class User:
    user = ""
    password = ""
    
    def __init__(self, user, password):
        self.user = user
        self.password = password
    
    def login(self, user, password):
        print (user, self.user)
        print (password, self.password)
    

# Open the dictionary.txt:

with open("dics/dics.txt","r", encoding="utf8") as f:
    dictionary = f.read()

# Create a random username and password for each user:

users = ["User1", "User2"]
for i in range(2):
    users[i] = User("".join(sample(re.findall(r"[a-zA-Z]+",dictionary), 2)),randint(1000,9999))

print(users[0].login)
quit()

# Create a username using 2 random words:



print(user.password)