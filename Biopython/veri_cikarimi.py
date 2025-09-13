from Bio import SeqIO

kayit_yineleyici = SeqIO.parse("ls_orchid.gbk", "genbank")
ilk_kayit = next(kayit_yineleyici)

print(ilk_kayit)
print(ilk_kayit.annotations)
print(ilk_kayit.annotations.keys())
print(ilk_kayit.annotations.values())

print(ilk_kayit.annotations["source"])
print(ilk_kayit.annotations["organism"])

butun_turler = []
for kayit in SeqIO.parse("ls_orchid.gbk", "genbank"):
    butun_turler.append(kayit.annotations["organism"])

print(butun_turler)