from eval2.files import FileUserRepository, FileWordSource


def _main():
    passwords = FileWordSource("word_source.txt")
    repo = FileUserRepository("user_repository.csv")
    mdp = {}

    try:
        with open("passwords.html", "a") as output_pwd:
            word_list = passwords.get_pwd_from_file()
            user_list = repo.get_users_from_csv()
            print()

            for i in range(0, passwords.count):
                mdp[word_list[i]] = repo.get_users_matching(user_list, word_list[i])

                if mdp[word_list[i]]:
                    for user in mdp[word_list[i]]:
                        print(f'{user} has a weak password = {word_list[i]}')
                        output_pwd.write(f"{user} has a weak password = {word_list[i]}<br>\n")

    except FileNotFoundError:
        print("Erreur avec le fichier")


if __name__ == '__main__':
    _main()
