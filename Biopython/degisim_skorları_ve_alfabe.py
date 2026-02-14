dizi1 = ("Asn", "Leu", "Leu", "Phe")
dizi2 = ("Asn", "Leu", "Phe")

from Bio.Align import PairwiseAligner

hizalayici = PairwiseAligner()
hizalayici.alphabet = ['Ala', 'Arg', 'Asn', 'Asp', 'Cys',
                        'Gln', 'Glu', 'Gly', 'His', 'Ile',
                        'Leu', 'Lys', 'Met', 'Phe', 'Pro',
                        'Ser', 'Thr', 'Trp', 'Tyr', 'Val']

hizalayici.match = 6
hizalayici.mismatch = -1
hizalamalar = hizalayici.align(dizi1, dizi2)

print(len(hizalamalar))
print(hizalamalar[0])
print(hizalamalar[1])
print(hizalamalar.score)
