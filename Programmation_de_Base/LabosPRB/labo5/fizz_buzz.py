

def _main():
    
    dernier_nombre = int(input('Quel le dernier nombre ? '))

    for i in range(1, dernier_nombre + 1):
        if ((i % 3) == 0 ) and ((i % 5) == 0):
            i = 'fizzbuzz'

        elif ((i % 3) == 0):
            i = 'fizz'

        elif ((i % 5) == 0):
            i = 'buzz'


        print(i)






if __name__ == '__main__':
     _main()