from Bio import SeqIO

kayit = SeqIO.read("NC_005816.gb", "genbank")

print(kayit)
print(len(kayit))
print(len(kayit.features))

print(kayit.dbxrefs)
print(kayit.annotations.keys())

birlestirilmis = kayit[2000 : ] + kayit[ : 2000]

print(birlestirilmis)
print(len(birlestirilmis))

print(birlestirilmis.dbxrefs)
print(birlestirilmis.annotations.keys())

birlestirilmis.dbxrefs = kayit.dbxrefs[:]
birlestirilmis.annotations = kayit.annotations.copy()

print(birlestirilmis.dbxrefs)
print(birlestirilmis.annotations.keys())