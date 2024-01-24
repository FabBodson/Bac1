
def shoot(results):
    points_j1 = 0
    points_j2 = 0

    for round in results:
        score_j1 = round[0]['A']
        score_j2 = round[0]['B']

        if round[1] is True:
            points_j1 += 2 * (score_j1.count('X'))
            points_j2 += 2 * (score_j2.count('X'))

        else:
            points_j1 += score_j1.count('X')
            points_j2 += score_j2.count('X')


    if points_j1 > points_j2:
        print(f"Le gagnant est 'A' avec {points_j1}")

    elif points_j1 < points_j2:
        print(f"Le gagnant est 'B' avec {points_j2}")

    else:
        print("It's a draw")




def _main():


    round1 = {
        'A': 'XXO',
        'B': 'XXO'
    }

    round2 = {
        'A': 'XOX',
        'B': 'XXX'
    }

    results1 = [ (round1, False), # Round 1
                 (round2, True)  # Round 2
                ]



    shoot(results1)







if __name__ == '__main__':
    _main()