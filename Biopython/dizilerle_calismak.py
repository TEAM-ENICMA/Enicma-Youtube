from Bio.Seq import Seq

dizi = Seq("AGTACACTGGT")

dizi
#Output: Seq('AGTACACTGGT', Alphabet())

print(dizi)
print(dizi.complement())
print(dizi.reverse_complement())