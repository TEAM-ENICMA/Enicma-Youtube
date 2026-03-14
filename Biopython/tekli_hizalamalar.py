from Bio import AlignIO

hizalama = AlignIO.read("PF05371_seed.sth", "stockholm")
print(hizalama)

hizalama_uzunlugu = hizalama.get_alignment_length()
print(hizalama_uzunlugu)


for kayit in hizalama:
    print(kayit.seq + " - " + kayit.id)



for kayit in hizalama:
    if kayit.dbxrefs:
        print(kayit.id, kayit.dbxrefs)


for kayit in hizalama:
    print(kayit)


hizalama = AlignIO.read("PF05371_seed.faa", "fasta")
print(hizalama)


help(AlignIO)