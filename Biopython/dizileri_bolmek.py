from Bio.Seq import Seq

dizi = Seq("GATCGATGGGCCTATATAGGATCGAAAATCGC")
print(dizi[4:12])

print(dizi[0::3])
print(dizi[1::3])
print(dizi[2::3])

print(dizi[::-1])