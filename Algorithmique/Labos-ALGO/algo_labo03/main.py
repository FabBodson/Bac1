from algo_labo03.algorithm import apply_merge_sort


def _main():
    a = [2, 4, 1, 6, 8, 5, 3, 7]

    b = apply_merge_sort(a)

    print(a)
    print(b)


if __name__ == '__main__':
    _main()
