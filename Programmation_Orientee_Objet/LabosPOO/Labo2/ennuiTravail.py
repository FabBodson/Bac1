
def compute_boredom(team):

    ennui = 0
    for cle in team:
        if team[cle] == 'accounts':
            nouvelle_cle = 1
            ennui += nouvelle_cle

        elif team[cle] == 'finance':
            nouvelle_cle = 2
            ennui += nouvelle_cle

        elif team[cle] == 'canteen':
            nouvelle_cle = 10
            ennui += nouvelle_cle

        elif team[cle] == 'regulation':
            nouvelle_cle = 3
            ennui += nouvelle_cle

        elif team[cle] == 'trading' or team[cle] == 'change':
            nouvelle_cle = 6
            ennui += nouvelle_cle

        elif team[cle] == 'IS':
            nouvelle_cle = 8
            ennui += nouvelle_cle

        elif team[cle] == 'retail':
            nouvelle_cle = 8
            ennui += nouvelle_cle

        elif team[cle] == 'cleaning':
            nouvelle_cle = 4
            ennui += nouvelle_cle

        elif team[cle] == 'pissing about':
            nouvelle_cle = 25
            ennui += nouvelle_cle

    return ennui


def _main():


    team = {
    "tim": "IS",
    "jim": "finance",
    "randy": "pissing about",
    "sandy": "cleaning",
    "andy": "cleaning",
    "katie": "cleaning",
    "laura": "pissing about",
    "saajid": "regulation",
    "alex": "regulation",
    "john": "accounts",
    "mr": "canteen"


    }

    score_ennui = compute_boredom(team)

    if score_ennui <= 80:
        print('kill me now')

    elif 80 <= score_ennui < 100:
        print('i can handle this')

    else:
        print('party time !')

if __name__ == '__main__':
    _main()