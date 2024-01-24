
def find_children(santas_list, children):

    enfants_sages = list()

    for enfant in children:

        if enfant in santas_list and enfant not in enfants_sages:
            enfants_sages.append(enfant)

    return sorted(enfants_sages)
