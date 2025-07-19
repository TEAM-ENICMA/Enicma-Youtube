from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord

dizi = Seq("GATC")
seqr = SeqRecord(dizi)
print(seqr)

print(seqr.id)

seqr.id = "AC12345"
seqr.description = "Hakkinda bir yayin cikarmis olmayi istedigim uydurma bir dizi."

print(seqr.id)
print(seqr.description)
print(seqr.seq)

seqr = SeqRecord(dizi, id = "AC12345", description = "Hakkinda bir yayin cikarmis olmayi istedigim uydurma bir dizi.")
print(seqr)

seqr.annotations["kanit"] = "Hic. Bunu ben uydurdum"
print(seqr.annotations["kanit"])

seqr.letter_annotations["phred_quality"] = [40, 40, 38, 30]
print(seqr.letter_annotations)
print(seqr.letter_annotations["phred_quality"])