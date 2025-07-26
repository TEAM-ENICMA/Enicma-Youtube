from Bio import SeqIO

kayit = SeqIO.read("NC_005816.gb", "genbank")
print(kayit)

print(kayit.seq)
print(kayit.id)
print(kayit.name)
print(kayit.description)

print(kayit.letter_annotations)

print(len(kayit.annotations))
print(kayit.annotations)
print(kayit.annotations["source"])

print(kayit.dbxrefs)

print(len(kayit.features))
print(kayit.features)
print(kayit.features[0])