from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio.Align import MultipleSeqAlignment

coklu_hizalamalar = MultipleSeqAlignment(
         [
             SeqRecord(Seq("ACTCCTA"), id = "seq1"),
             SeqRecord(Seq("AAT-CTA"), id = "seq2"),
             SeqRecord(Seq("CCTACT-"), id = "seq3"),
             SeqRecord(Seq("TCTCCTC"), id = "seq4"),
         ]
)

#print(type(coklu_hizalamalar))
print(coklu_hizalamalar)

yeni_stil_hizalamalar = coklu_hizalamalar.alignment
#print(type(yeni_stil_hizalamalar))
print(yeni_stil_hizalamalar)
