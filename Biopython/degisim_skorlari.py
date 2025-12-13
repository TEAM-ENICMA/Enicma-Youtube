from Bio import Align

hizalayici = Align.PairwiseAligner()
print(hizalayici.match_score)
print(hizalayici.mismatch_score)

skor = hizalayici.score("ACGT", "ACAT")
print(skor)

# ACTG  AC-TG   ACT-G
# ACAT  ACA-G   AC-AG

hizalayici.match_score = 1.0
hizalayici.mismatch_score = -2.0
hizalayici.gap_score = -2.5

skor = hizalayici.score("ACGT", "ACAT")
print(skor)

hizalayici.wildcard = "?"
skor = hizalayici.score("ACGT", "AC?T")
print(skor)

from Bio.Align import substitution_matrices

mx = substitution_matrices.load()
print(mx)

mx = substitution_matrices.load("BLOSUM62")
print(mx)

hizalayici.substitution_matrix = mx
print(hizalayici.score("ACDQ", "ACDQ"))
print(hizalayici.score("ACDQ", "ACNQ"))