import numpy as np
from Bio.Align import PairwiseAligner

hizalayici = PairwiseAligner()
dizi1 = np.array([2, 10, 10, 13], np.int32)
dizi2 = np.array([2, 10, 13], np.int32)

hizalayici.match = 6
hizalayici.mismatch = -1

hizalamalar = hizalayici.align(dizi1, dizi2)

print(len(hizalamalar))
print(hizalamalar[0])
print(hizalamalar[1])
print(hizalamalar.score)


hizalayici.wildcard = "?"
print(ord(hizalayici.wildcard))

dizi2 = np.array([2, 63, 13], np.int32)
hizalayici.gap_score = -3
hizalamalar = hizalayici.align(dizi1, dizi2)

print(len(hizalamalar))
print(hizalamalar[0])
print(hizalamalar[1])
print(hizalamalar.score)