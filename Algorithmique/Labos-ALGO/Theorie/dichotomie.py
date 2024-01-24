
def belongs_to(ensemble, searched_nb):
    ensemble.sort()
    print(ensemble)
    if len(ensemble) == 0 or searched_nb not in ensemble:
        print("Liste vide ou nombre inexistant")
        return []
    else:
        if ensemble[0] == searched_nb:
            print("Premier element")
            return [ensemble[0]]
        else:
            half = len(ensemble) // 2
            left_e = ensemble[:half]
            middle_e = ensemble[half]
            right_e = ensemble[half+1:]
            if middle_e == searched_nb:
                print("Nombre du milieu")
                return True
            else:
                if searched_nb < ensemble[half]:
                    belongs_to(left_e, searched_nb)
                else:
                    belongs_to(right_e, searched_nb)


def _main():
    ensemble = [10, 9, 11, 2, 5, 14, 13, 12, 1, 7, 8, 3, 4, 6, 0]
    searched_nb = 5

    belongs_to(ensemble, searched_nb)


if __name__ == '__main__':
    _main()
