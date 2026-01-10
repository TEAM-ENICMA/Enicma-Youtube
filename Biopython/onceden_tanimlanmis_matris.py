from Bio import Align

hizalayici = Align.PairwiseAligner(scoring = "blastn")

print(hizalayici)
print(hizalayici.substitution_matrix[:, :])