import hashlib


class UserRepository:
    def __init__(self):
        self.__users = []

    @property
    def users(self):
        return self.__users

    def get_users_matching(self, user_list, clear_pwd):

        if isinstance(clear_pwd, str) and len(clear_pwd) > 0:
            hashed_pwd = hashlib.sha256(clear_pwd.encode('utf-8')).hexdigest()
            got_pwd = []
            for user in user_list:
                # Check si le mdp de l'user == le mdp hashé
                if user[2] == hashed_pwd:
                    got_pwd.append(user[0])
            return got_pwd

        else:
            return False
