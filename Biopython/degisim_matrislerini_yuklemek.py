from Bio.Align import substitution_matrices

matris = substitution_matrices.load("BLOSUM62")

print(matris.alphabet)
print(substitution_matrices.load())

matris = substitution_matrices.load("SCHNEIDER")

print(matris.alphabet)