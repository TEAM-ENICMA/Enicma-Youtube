from Bio import SeqIO

kayit_yineleyici = SeqIO.parse("ls_orchid.fasta", "fasta")
ilk_kayit = next(kayit_yineleyici)
print(ilk_kayit.id)

ilk_kayit.id = "yeni_kimlik"
print(ilk_kayit.id)

ilk_kayit.description = ilk_kayit.id + " " + "istenilen yeni bir tanim"
print(ilk_kayit.format("fasta")[:200])