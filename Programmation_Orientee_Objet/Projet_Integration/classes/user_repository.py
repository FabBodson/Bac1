import hashlib


class User:
    def __init__(self, login, email, password):
        self.login = login
        self.email = email
        self.password = password
        self.role = ""


class UserRepository:
    def __init__(self):
        self.__users = []

    def get_users_matching(self, clear_pwd, hashed_pwd):
        found = []
        if len(clear_pwd) < 1:
            return found
        for user in self.users:
            if user.password == hashed_pwd:
                user.password = clear_pwd
                found.append(user)
                # print(f"{user.login} has a weak password => '{clear_pwd}'.")
                try:
                    with open("files/found_passwords.html", "a") as dest_file:
                        dest_file.write(f"{user.login} has a weak password => '{clear_pwd}'.<br>\n")

                except FileNotFoundError:
                    print(f"File 'found_passwords.html' not found.")

        return found

    @property
    def users(self):
        return self.__users
