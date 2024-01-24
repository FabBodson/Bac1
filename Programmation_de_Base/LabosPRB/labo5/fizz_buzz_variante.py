

def _main():

    dernier_nombre = int(input('Quel le dernier nombre ? '))

    for i in range(1, dernier_nombre + 1):

        string = str(i)
        find3 = string.find('3')
        find5 = string.find('5')


        if find3 >= 0 and find5 >= 0:
            i = 'fizzbuzz'

        elif find3 >= 0:
            i = 'fizz'

        elif find5 >= 0:
            i = 'buzz'

        else:
            i = i

        print(i)


if __name__ == '__main__':
    _main()