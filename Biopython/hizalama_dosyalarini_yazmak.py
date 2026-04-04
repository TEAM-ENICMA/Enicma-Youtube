from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio.Align import MultipleSeqAlignment

hizalama1 = MultipleSeqAlignment(
         [
             SeqRecord(Seq("ACTGCTAGCTAG"), id = "Alpha"),
             SeqRecord(Seq("ACT-CTAGCTAG"), id = "Beta"),
             SeqRecord(Seq("ACTGCTAGDTAG"), id = "Gamma"),
         ]
)

hizalama2 = MultipleSeqAlignment(
         [
             SeqRecord(Seq("GTCAGC-AG"), id = "Delta"),
             SeqRecord(Seq("GACAGCTAG"), id = "Epsilon"),
             SeqRecord(Seq("GTCAGCTAG"), id = "Zeta"),
         ]
)

hizalama3 = MultipleSeqAlignment(
         [
             SeqRecord(Seq("ACTAGTACAGCTG"), id = "Eta"),
             SeqRecord(Seq("ACTAGTACAGCT-"), id = "Theta"),
             SeqRecord(Seq("-CTACTACAGGTG"), id = "Iota"),
         ]
)

hizalamalar = [hizalama1, hizalama2, hizalama3]

from Bio import AlignIO

AlignIO.write(hizalamalar, "ornek.phy", "phylip")