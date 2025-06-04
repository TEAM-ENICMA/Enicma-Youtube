from Bio.Seq import Seq

dizi = Seq("acgtACGT")
print(dizi)

print(dizi.upper())
print(dizi.lower())

print("GTAC" in dizi)
print("GTAC" in dizi.upper())