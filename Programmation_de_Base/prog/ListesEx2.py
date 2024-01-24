t = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
m = [0.0, 0.0, 0.0, 0.0, 0.0]
# ou : m = [0.0] * 5

print('De 0 à 3: ')
for i in range(0, 3):
    print(t[i], end=" ")


print('\n\nDe 4 à 7: ')
for j in range(4, 8):
    print(t[j], end=" ")


print('\n\nDe 0 à 8 avec pas de 2: ')
for k in range(0, 9, 2):
    print(t[k], end=" ")

print(f'\n\nt = {t}')
print(f'm = {m}')