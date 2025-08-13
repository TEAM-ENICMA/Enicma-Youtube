from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord

kayit = SeqRecord(Seq("MMYQQGCFAGGTVLRLAKDLAENNRGARVLVVCSEITAVTFRGPSETHLDSMVGQALFGD"
             "GAGAVIVGSDPDLSVERPLYELVWTGATLLPDSEGAIDGHLREVGLTFHLLKDVPGLISK"
             "NIEKSLKEAFTPLGISDWNSTFWIAHPGGPAILDQVEAKLGLKEEKMRATREVLSEYGNM"
             "SSAC"), id = "gi|14150838|gb|AAK54648.1|AF376133_1", description = "chalcone synthase [Cucumis sativus]"
             )

print(kayit)
print(kayit.format("fasta"))