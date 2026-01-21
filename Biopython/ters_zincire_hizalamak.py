from Bio import Align
from Bio.Seq import reverse_complement

dizi1 = "AAAACCC"
dizi2 = "AACC"

hizalayici = Align.PairwiseAligner()
hizalayici.mismatch_score = -1
hizalayici.internal_gap_score = -1


print(hizalayici.score(dizi1, dizi2))
print(hizalayici.score(dizi1, reverse_complement(dizi2), strand = "-"))
print(hizalayici.score(dizi1, dizi2, strand = "-"))
print(hizalayici.score(dizi1, reverse_complement(dizi2)))


hizalamalar = hizalayici.align(dizi1, dizi2)
print(len(hizalamalar))
print(hizalamalar[0])

#print(hizalamalar[0].format("bed"))

hizalamalar = hizalayici.align(dizi1, reverse_complement(dizi2), strand = "-")
print(len(hizalamalar))
print(hizalamalar[0])

hizalayici.left_gap_score = -0.5
hizalayici.right_gap_score = -0.2

print(hizalayici.score(dizi1, dizi2))
hizalamalar = hizalayici.align(dizi1, dizi2)
print(len(hizalamalar))
print(hizalamalar[0])

print(hizalayici.score(dizi1, reverse_complement(dizi2), strand = "-"))
hizalamalar = hizalayici.align(dizi1, reverse_complement(dizi2), strand = "-")
print(len(hizalamalar))
print(hizalamalar[0])