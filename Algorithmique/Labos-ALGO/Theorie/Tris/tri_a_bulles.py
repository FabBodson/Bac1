
def bubble_sort(sequence):
    """
    Complexite: O(n**2)
    Parcours d'une sequence, comparaison de 2 éléments.
    Permutation si l'element suivant est < que l'element actuel.
    :param sequence:
    :return:
    """
    sequence = sequence.copy()
    sequence_is_not_sorted = True

    while sequence_is_not_sorted:
        sequence_is_not_sorted = False
        for i in range(0, len(sequence)-1):
            if sequence[i+1] < sequence[i]:
                sequence_is_not_sorted = True
                tmp = sequence[i]
                sequence[i] = sequence[i+1]
                sequence[i+1] = tmp

    return sequence


def _main():
    a = [10, 9, 11, 2, 5, 14, 13, 12, 1, 7, 8, 3, 4, 6, 0]
    tri = bubble_sort(a)

    print(a)
    print(tri)


if __name__ == '__main__':
    _main()
