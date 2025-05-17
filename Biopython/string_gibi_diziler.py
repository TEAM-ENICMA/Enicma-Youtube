from Bio.Seq import Seq

dizi = Seq("GATCG")

for index, letter in enumerate(dizi):
    print("%i %s" % (index, letter))

print(len(dizi))

print(dizi[0]) # ilk harf
print(dizi[2]) # ucuncu harf
print(dizi[-1]) # son harf

print("AAAA".count("AA"))
print(Seq("AAAA").count("AA"))

dizi = Seq("GATCGATGGGCCTATATAGGATCGAAAATCGC")
print("uzunluk:", len(dizi))
print("G sayisi:", dizi.count("G"))
print("GC icerigi:", (dizi.count("G") + dizi.count("C")) / len(dizi) * 100)

from Bio.SeqUtils import gc_fraction

dizi = Seq("GATCGATGGGCCTATATAGGATCGAAAATCGC")
print(gc_fraction(dizi))