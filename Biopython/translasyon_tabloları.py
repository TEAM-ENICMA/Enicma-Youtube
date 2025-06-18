from Bio.Data import CodonTable

standart = CodonTable.unambiguous_dna_by_name["Standard"]
mito = CodonTable.unambiguous_dna_by_name["Vertebrate Mitochondrial"]

standart = CodonTable.unambiguous_dna_by_id[1]
mito = CodonTable.unambiguous_dna_by_id[2]

print(standart)
print(mito)

print(mito.stop_codons)
print(mito.start_codons)
print(mito.forward_table["ACG"])


print(standart.stop_codons)
print(standart.start_codons)
print(standart.forward_table["ACG"])

tablo3 = CodonTable.unambiguous_dna_by_id[3]
tablo4 = CodonTable.unambiguous_dna_by_id[4]

print(tablo3)
print(tablo4)
