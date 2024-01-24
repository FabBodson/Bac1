def plus_gande_2_valeur(a, b):
    if a < b:
        return b

    elif a > b:
        return a

    else:
        return a



def plus_gande_3_valeur(a, b, c):
    if a < b:
        if b > c:
            return b
        else:
            return c

    elif a > b:
        if a > c:
            return a
        else:
            return c

    else:
        return a


def _main():


    print(plus_gande_3_valeur(3, 2, 3))

if __name__ == '__main__':
    _main()