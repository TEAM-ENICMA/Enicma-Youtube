from Bio import SeqIO

kayit = SeqIO.read("NC_005816.gb", "genbank")

print(kayit)
print(len(kayit))
print(len(kayit.features))

print(kayit.features[20])
print(kayit.features[21])

alt_kayit = kayit[4300:4800]

print(alt_kayit)
print(len(alt_kayit))
print(len(alt_kayit.features))

print(alt_kayit.features[0])
print(alt_kayit.features[1])

print(alt_kayit.annotations)
print(alt_kayit.dbxrefs)

print(kayit.annotations["topology"])

alt_kayit.annotations["topology"] = "linear"
print(alt_kayit.annotations["topology"])

print(alt_kayit.id)
print(alt_kayit.name)
print(alt_kayit.description)

alt_kayit.description = "Yersinia pestis biovar Microtus str. 91001 plasmid pPCP1, partial"
print(alt_kayit.description)

print(alt_kayit.format("genbank")[ : 200] + "...")