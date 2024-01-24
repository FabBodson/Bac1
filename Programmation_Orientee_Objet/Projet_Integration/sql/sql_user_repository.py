from classes.files import FileUserRepository
from sql.setup_db import script_to_get_users, get_role_of_user
import sqlite3
import hashlib


class SqlUserRepository(FileUserRepository):

    def __init__(self, db_path, hash_algorithm):
        super().__init__()
        self.db_path = db_path
        self.hash_algorithm = hash_algorithm

    def get_users_from_database(self):
        try:
            db = sqlite3.connect(self.db_path)
            cursor = db.cursor()

            script_to_get_users(self, cursor)
            get_role_of_user(self.users, cursor)

            db.close()

        except FileNotFoundError:
            print("DataBase not found.")

    def get_users_matching(self, clear_pwd, hashed_pwd=""):
        if self.hash_algorithm == "sha1":
            hashed_pwd = hashlib.sha1(clear_pwd.encode('utf-8')).hexdigest()

        elif self.hash_algorithm == "sha224":
            hashed_pwd = hashlib.sha224(clear_pwd.encode('utf-8')).hexdigest()

        elif self.hash_algorithm == "sha256":
            hashed_pwd = hashlib.sha256(clear_pwd.encode('utf-8')).hexdigest()

        elif self.hash_algorithm == "sha384":
            hashed_pwd = hashlib.sha384(clear_pwd.encode('utf-8')).hexdigest()

        elif self.hash_algorithm == "sha512":
            hashed_pwd = hashlib.sha512(clear_pwd.encode('utf-8')).hexdigest()

        elif self.hash_algorithm == "md5":
            hashed_pwd = hashlib.md5(clear_pwd.encode('utf-8')).hexdigest()

        else:
            return False

        return super().get_users_matching(clear_pwd, hashed_pwd)
