from Bio.Seq import Seq
from Bio.SeqFeature import SeqFeature, SimpleLocation

kromozom = Seq("ACCGAGACGGCAAAGGCTAGCATAGGTATGAGACTTCCTTCCTGCCAGTGCTGAGGAACTGGGAGCCTAC")
konum_ozelligi = SeqFeature(SimpleLocation(5, 18, strand = -1), type = "gene")

konum_dizisi = kromozom[konum_ozelligi.location.start : konum_ozelligi.location.end]
print(konum_dizisi)
konum_dizisi = konum_dizisi.reverse_complement()
print(konum_dizisi)

konum_dizisi = konum_ozelligi.extract(kromozom)
print(konum_dizisi)

print(len(konum_dizisi))
print(len(konum_ozelligi))
print(len(konum_ozelligi.location))