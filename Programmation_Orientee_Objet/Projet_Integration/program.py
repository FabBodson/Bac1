from classes.files import FileWordSource
from sql.sql_user_repository import SqlUserRepository
from sql.setup_db import create_db
import re


def display_results(results):
    display = "Inspection results:\n"
    display += f"| Critique:{'|':>8} Emails:{'|':>17} Mot de passe:{'|':>8} Role:{'|':>13}\n"
    display += "|-----------------------------------------------------------------------------------|\n"

    for user in results:
        if len(user) > 1:
            for user_bis in user:
                if re.match("ADMIN", user_bis.role):
                    display += f"| {'X':>8} {'|':>8} {user_bis.email} {'|':>4} {user_bis.password} {'|':>14} {user_bis.role} {'|':>4}\n"
                else:
                    display += f"| {'|':>17} {user_bis.email} {'|':>5} {user_bis.password} {'|':>13} {user_bis.role} {'|':>10}\n"

        elif len(user) == 1:
            if re.match("ADMIN", user[0].role):
                display += f"| {'X':>8} {'|':>8} {user[0].email} {'|':>4} {user[0].password} {'|':>14} {user[0].role} {'|':>4}\n"
            else:
                display += f"| {'|':>17} {user[0].email} {'|':>5} {user[0].password} {'|':>13} {user[0].role} {'|':>10}\n"

    return display


def print_in_file(text):
    try:
        with open("files/results.md", "a") as result_file:
            result_file.write(text)

    except Exception:
        print("Error to open file")


def _main():
    word_source = FileWordSource("files/words.txt")
    user_repository = SqlUserRepository("poo.db", "sha256")

    create_db("poo.db")  # Création DB, ouverture et fermeture dedans.

    if len(user_repository.users) == 0:
        # user_repository.get_users_from_csv("files/users.csv")  # Création liste des users àpd'un fichier csv.
        user_repository.get_users_from_database()

    results = []
    for word in word_source.words:
        results.append(user_repository.get_users_matching(word))

    print(display_results(results))
    print_in_file(display_results(results))


if __name__ == '__main__':
    _main()
