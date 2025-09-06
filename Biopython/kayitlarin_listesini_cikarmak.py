from Bio import SeqIO

kayitlar = list(SeqIO.parse("ls_orchid.gbk", "genbank"))

print("%i kayit bulundu" % len(kayitlar))

print("Son kayit")
son_kayit = kayitlar[-1]
print(son_kayit.id)
print(repr(son_kayit.seq))
print(len(son_kayit))

print("Ilk kayit")
ilk_kayit = kayitlar[0]
print(ilk_kayit.id)
print(repr(ilk_kayit.seq))
print(len(ilk_kayit))