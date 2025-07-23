from Bio import SeqIO

kayit = SeqIO.read("NC_005816.fna", "fasta")
print(kayit)

print(kayit.seq)
print(kayit.id)
print(kayit.name)
print(kayit.description)

print(kayit.dbxrefs)
print(kayit.annotations)
print(kayit.letter_annotations)
print(kayit.features)