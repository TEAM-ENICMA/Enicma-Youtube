import numpy as np
from Bio.Align import PairwiseAligner

hizaliyici = PairwiseAligner()

matris = np.eye(5)
matris[0, 1 : ] = matris[1 : , 0] = -2
matris[2, 2] = 3

print(matris)

hizaliyici.substitution_matrix = matris
hizaliyici.gap_score = -1

dizi1 = np.array([0, 2, 3, 4], np.int32)
dizi2 = np.array([0, 3, 2, 1], np.int32)

hizalamalar = hizaliyici.align(dizi1, dizi2)

print(len(hizalamalar))
print(hizalamalar[0])
print(hizalamalar[1])
print(hizalamalar.score)