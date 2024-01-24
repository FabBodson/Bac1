

def _main():

    nombre_entier = 4312
    i = 2

    while i <= 20:

        if (nombre_entier % i) == 0:
            print(i)
            nombre_entier = nombre_entier // i


        else:
            i += 1








if __name__ == '__main__':
     _main()