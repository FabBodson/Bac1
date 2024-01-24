
def balanced_num(number):

    number = list(number)
    nb_elements = number.count()

    if nb_elements % 2 == 0:
        moitie = nb_elements // 2

        somme1 = 0
        for element in number[:moitie]:
            somme1 += element

        somme2 = 0
        for element in number[moitie + 2:]:
            somme2 += element

    else:
        moitie = (nb_elements//2) + 1

        somme1 = 0
        for element in number[:moitie]:
            somme1 += element

        somme2 = 0
        for element in number[moitie+1:]:
            somme2 += element


    if somme1 == somme2:
        return 'Balanced !!!'

    else:
        return 'Not balanced...'