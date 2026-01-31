from Bio.Align import substitution_matrices

with open("hg38.chrom.sizes") as dosya:
    tablo = substitution_matrices.read(dosya)

print(tablo)

with open("hg38.chrom.sizes") as dosya:
    tablo = substitution_matrices.read(dosya, int)

print(tablo)

with open("BLOSUM62.txt") as dosya:
    matris = substitution_matrices.read(dosya)

print(matris.alphabet)
print(matris["A", "D"])
print(matris.header[0])

from Bio.Align import PairwiseAligner

hizalayici = PairwiseAligner()
hizalayici.substitution_matrix = matris

metin = str(matris)
print(metin)