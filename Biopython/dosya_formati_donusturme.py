from Bio import SeqIO

gb_kayitlar = SeqIO.parse("ls_orchid.gbk", "genbank")
kayit1 = next(gb_kayitlar)
print(kayit1)

fa_kayitlar = SeqIO.convert("ls_orchid.gbk", "genbank", "ls_orchid.fasta", "fasta")
print(fa_kayitlar)

print(help(SeqIO.convert))