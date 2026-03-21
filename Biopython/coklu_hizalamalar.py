from Bio import AlignIO

hizalamalar = AlignIO.parse("coklu_hizalama.phy", "phylip")

for hizalama in hizalamalar:
    print(hizalama)
    print()

hizalamalar = list(hizalamalar)

ilk_hizalama = hizalamalar[0]
son_hizalama = hizalamalar[-1]

print(ilk_hizalama)
print(son_hizalama)