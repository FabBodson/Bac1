def tri_insertion(sequence):
    actual_pos = sequence.index(sequence[-1])
    while actual_pos != 0 and sequence[actual_pos] < sequence[actual_pos - 1]:
        low_val = sequence[actual_pos]
        high_val = sequence[actual_pos - 1]

        sequence[actual_pos - 1] = low_val
        sequence[actual_pos] = high_val

        actual_pos = actual_pos - 1


def _main():
    sequence = []
    go_on = "y"
    while go_on == "y":
        new_val = int(input("\nNew value:  "))
        sequence.append(new_val)
        print("Before sort:", sequence)
        tri_insertion(sequence)
        print("After sort:", sequence)

        go_on = str.lower(input("Go on ? (y/n) "))


if __name__ == '__main__':
    _main()
