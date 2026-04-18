from Bio import AlignIO

hizalama = AlignIO.read("PF05371_seed.sth", "stockholm")
print(format(hizalama, "clustal"))