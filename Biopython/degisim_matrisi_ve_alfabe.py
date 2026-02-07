from Bio.Align import substitution_matrices

matris = substitution_matrices.load("SCHNEIDER")
print(matris.alphabet)

from Bio.Align import PairwiseAligner

hizalayici = PairwiseAligner()
hizalayici.substitution_matrix = matris
hizalayici.gap_score = -1

dizi1 = ("AAT", "CTG", "TTT", "TTT")
dizi2 = ("AAT", "TTA", "TTT")

hizalamalar = hizalayici.align(dizi1, dizi2)

print(len(hizalamalar))
print(hizalamalar[0])
print(hizalamalar[1])

"""
AAT CTG TTT TTT
||| --- ... |||
AAT --- TTA TTT
"""

print(matris["CTG", "TTA"])
print(matris["TTT", "TTA"])