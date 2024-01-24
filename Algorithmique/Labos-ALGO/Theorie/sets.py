myset = {"rouge", "vert", "bleu"}

print(myset)

myset.add(3)
myset.update(["violet", "jaune"])
print(myset)

myset.remove(3)
myset.discard("rouge")
print(myset)

if "rouge" in myset:
    print("jaune")

"""
for x in myset:
    print(x)
"""

a = [1, 2, 3, 3]

print(a)

a = set(a)

print(a)
