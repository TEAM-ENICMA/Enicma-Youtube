from Bio.Align.substitution_matrices import Array

dizi = Array("ACGT")

print(dizi)
print(dizi.alphabet)

dizi["C"] = -3
dizi[2] = 7

print(dizi)
print(dizi[1])

#print(dizi["U"])
#dizi["X"] = 6
#print(dizi[7])

dizi = Array("ACGT", dims = 2)

print(dizi)

dizi["A", "C"] = 12.0
dizi[2, 1] = 5.0
dizi[3, "T"] = -2

print(dizi)

#print(dizi["X", 1])
#print(dizi["A", 5])

print(dizi["G"])
print(dizi[ : , "C"])

x = Array("ACGT")
x["C"] = 5

import numpy as np

a = np.array(x)
print(a)

d = dict(x)
print(d)

print(x)
print(a)
print(d)

a = Array("ABCD", dims = 2, data = np.arange(16).reshape(4, 4))
print(a)

b = a.select("CAD")
print(b)

c = a.select("DEC")
print(c)

dna = Array("ACGT")
rna = Array("ACGU")

#print(dna + rna)