from Bio import Align

hizalayici = Align.PairwiseAligner()
hizalamalar = hizalayici.align("AAA", "AA")

print(len(hizalamalar))

print(hizalamalar[2])
print(hizalamalar[1])
print(hizalamalar[0])

for hizalama in hizalamalar:
    print(hizalama)
    print(hizalama.score)

hizalamalar = list(hizalamalar)

print(hizalamalar.score)