def tri_rapide(sequence, debut, fin=None):
    if fin is None:
        fin = len(sequence) - 1

    if debut < fin:
        indice_pivot = len(sequence) // 2
        pivot = sequence[indice_pivot]
        i = debut
        j = fin
        while i < j:
            while pivot > sequence[i]:
                i += 1
            while pivot < sequence[j]:
                j -= 1

            if i < j:
                tmp = sequence[i]
                sequence[i] = sequence[j]
                sequence[j] = tmp
            else:
                break

            i += 1
            j -= 1
            indice_pivot = len(sequence[i:j]) // 2
            pivot = sequence[indice_pivot]

        tri_rapide(sequence, i, indice_pivot)
        tri_rapide(sequence, indice_pivot, j)

    return sequence


def _main():

    a = [11, 20, 16, 10, 2]
    print("Avant:", a)
    b = tri_rapide(a, 0)
    print("Après:", b)

    print()

    a = [2, 3, 1, 5, 4]
    print("Avant:", a)
    b = tri_rapide(a, 0)
    print("Après:", b)


if __name__ == '__main__':
    _main()
