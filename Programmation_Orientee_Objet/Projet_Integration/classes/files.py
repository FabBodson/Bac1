from classes.word_source import WordSource
from classes.user_repository import UserRepository, User
import csv


class FileWordSource(WordSource):
    def __init__(self, source_file):
        super().__init__([])
        try:
            with open(source_file) as file_with_words:
                reader = file_with_words.readlines()
                for line in reader:
                    line = line.rstrip("\n")
                    line = line.split(",")
                    for word in line:
                        self.words.append(word)

        except FileNotFoundError:
            print(f"File '{source_file}' not found.")


class FileUserRepository(UserRepository):
    def __init__(self):
        super().__init__()

    def get_users_from_csv(self, csv_file):
        try:
            with open(csv_file, newline='') as users_file:
                users = csv.DictReader(users_file, delimiter=";")  # Liste de dictionnaires. Dictionnaires correspondent aux users.
                for user in users:
                    self.users.append(User(user['login'], user['email'], user['password']))

        except FileNotFoundError:
            print(f"File '{csv_file}' not found.")

