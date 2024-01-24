print("Quelle type de température voulez voulez-vous convertir ?")

temp = int(input("1 : Celsius en Kelvin et Fahrenheit\n2 : Kelvin en Celsius et Fahrenheit\n3 : Fahrenheit en Celsius et Kelvin\n"))


iftemp == 1:

    degreC = float(input("Quelle température en °Celsius fait-il ? "))

    degreK = degreC + 273.15
    degreF = degreC * 9 / 5 +32
    print(f"Kelvin : {degreK:.2f} K")
    print(f"Fahrenheit : {degreF:.2f} °F")


if temp == 2:

    degreK = float(input("Quelle température en Kelvin fait-il ? "))

    degreC = degreK - 273.15
    degreF = degreC * 9 / 5 +32
    print(f"Celsius : {degreC:.2f} °C")
    print(f"Fahrenheit : {degreF:.2f} °F")


if temp == 3:

    degreF = float(input("Quelle température en °Fahrenheit fait-il ? "))

    degreC = (degreF - 32) * 5 / 9
    degreK = degreC + 273.1
    print(f"Celsius : {degreC:.2f} °C")
    print(f"Kelvin : {degreK:.2f} K")
