
def identify_weapon(character):
    personnage = {
        "Laval": "Shado Valious",
        "Cragger": "Vengdualize",
        "Lagravis": "Blazeprowlor",
        "Crominus": "Grandorius",
        "Tormak": "Tygafyre",
        "LiElla": "Roarburn"
    }

    if character in personnage:
        print(character, '->', personnage[character])

    else:
        print('Not a character')


def _main():
    identify_weapon('Crominus')
    identify_weapon('Lagravis')
    identify_weapon('Gloona')


if __name__ == '__main__':
    _main()
