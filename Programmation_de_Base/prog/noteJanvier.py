cote_max = int(input('Cote sur combien ? '))
nbr_UE = int(input("Nombre d'UE ? "))

note_prb = float(input('Note de Programmation de base: '))
note_archi = float(input("Note d'Architecture des ordinateurs: "))
note_gestion = float(input('Note de Gestion: '))

moyenne = round((note_prb + note_archi + note_gestion) / nbr_UE, 2)

print(moyenne)