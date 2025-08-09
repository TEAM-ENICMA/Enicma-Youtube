from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord

kayit1 = SeqRecord(Seq('ACGT'), id = "test")
kayit2 = SeqRecord(Seq('ACGT'), id = "test")

#print(kayit1 == kayit2)

print(kayit1.seq == kayit2.seq)
print(kayit1.id == kayit2.id)