sequence1 = 'AGWPSGGASAGLAIL'
sequence2 = 'IGWPSAGASAGLWIL'

hamming = 0

for i in range(len(sequence1)):
    if sequence1[i] != sequence2[i]:
        hamming += 1
    else:
        continue
print(hamming)
