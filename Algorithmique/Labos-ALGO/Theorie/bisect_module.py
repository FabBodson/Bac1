import bisect

a = [1, 2, 3, 4, 6]

# Donne la position où mettre l'élément 5
i = bisect.insort(a, 5)

print(a)

print(i)
print(a)
