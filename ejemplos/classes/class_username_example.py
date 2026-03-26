import hashlib

class user:
    username = ""
    password = ""

    def __init__(self, username, password):
        self.username = username
        self.password = hashlib.md5(password.encode()).hexdigest()

    def login(self, username, password) -> bool:
        encrypted_password = hashlib.md5(password.encode()).hexdigest()

        print("username guardado", self.username)
        print("username login", username)
        print("password guardado", self.password)
        print("password login", password)
        print("password login encriptado", encrypted_password)

        if username == self.username and encrypted_password == self.password:
            return True
        else:
            return False


def main() -> int:
    user_1 = user("admin", "1234")

    print("usuario creado", user_1.username, user_1.password)

    logged = user_1.login("admin", "1234")
    print(logged)

main()