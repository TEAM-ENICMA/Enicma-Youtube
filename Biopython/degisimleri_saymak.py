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

print(coklu_hizalamalar)

degisimler = coklu_hizalamalar.substitutions
print(degisimler)

g_eklenmis_degisimler = degisimler.select("ATCG")
print(g_eklenmis_degisimler)

a_t_degisimler = degisimler.select("AT")
print(a_t_degisimler)