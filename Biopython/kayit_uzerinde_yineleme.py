from Bio import SeqIO

kayit_yineleyici = SeqIO.parse("ls_orchid.fasta", "fasta")

ilk_kayit = next(kayit_yineleyici)
print(ilk_kayit.id)
print(ilk_kayit.description)

ikinci_kayit = next(kayit_yineleyici)
print(ikinci_kayit.id)
print(ikinci_kayit.description)

ilk_kayit = next(SeqIO.parse("ls_orchid.gbk", "genbank"))

print(ilk_kayit)