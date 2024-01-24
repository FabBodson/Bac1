from user_repository import UserRepository
from word_source import WordSource
import csv


class FileWordSource(WordSource):
    def __init__(self, file):
        super().__init__()
        self.__words = []
        self.file = file

    def get_pwd_from_file(self):
        try:
            with open(self.file, "r") as password_file:
                print(f"{self.file} successfully opened")
                for line in password_file.readlines():
                    line = line.rstrip('\n')
                    line = line.split(',')
                    self.__words = line
                return self.__words

        except FileNotFoundError:
            print(f"{self.file} not found")

    @property
    def count(self):
        return len(self.__words)


class FileUserRepository(UserRepository):
    def __init__(self, csv_file):
        super().__init__()
        self.__users = []
        self.csv_file = csv_file

    def get_users_from_csv(self):
        try:
            with open(self.csv_file, newline='') as users_file:
                print(f"{self.csv_file} successfully opened")
                user = csv.reader(users_file, delimiter=';', quotechar='|')
                # line est une liste qui s'ajoute à la liste __users
                for line in user:
                    self.__users.append(line)
                self.__users.remove(self.__users[0])
                return self.__users

        except FileNotFoundError:
            print(f"{self.csv_file} not found")
