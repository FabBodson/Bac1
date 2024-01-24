def tri_selection(sequence):
    for i in range(0, len(sequence)):
        index_min = i
        minimum = sequence[i]
        for j in range(i+1, len(sequence)):
            if sequence[j] < minimum:
                index_min = j
                minimum = sequence[j]
        tmp = sequence[i]
        sequence[i] = minimum
        sequence[index_min] = tmp


def _main():
    sequence = [11, 2, 16, 10, 2]
    print("Before sort:", sequence)
    tri_selection(sequence)
    print("After sort:", sequence)


if __name__ == '__main__':
    _main()
