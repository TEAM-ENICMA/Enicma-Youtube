from Bio import AlignIO

hizalama = AlignIO.convert("PF05371_seed.sth", "stockholm", "PF05371_seed.aln", "clustal")
print(hizalama)

hizalama1 = AlignIO.parse("PF05371_seed.sth", "stockholm")
hizalama2 = AlignIO.write(hizalama1, "PF05371_seed.aln", "clustal")
print(hizalama2)

hizalama1 = AlignIO.read("PF05371_seed.sth", "stockholm")
hizalama2 = AlignIO.write([hizalama1], "PF05371_seed.aln", "clustal")

hizalama = AlignIO.convert("PF05371_seed.sth", "stockholm", "PF05371_seed.phy", "phylip")
hizalama = AlignIO.convert("PF05371_seed.sth", "stockholm", "PF05371_seed.phy", "phylip-relaxed")

hizalama = AlignIO.read("PF05371_seed.sth", "stockholm")
isim_haritalama = {}

for endeks, kayit in enumerate(hizalama):
    isim_haritalama[endeks] = kayit.id
    kayit.id = "dizi%i" % endeks

print(isim_haritalama)
AlignIO.write([hizalama], "PF05371_seed.phy", "phylip")