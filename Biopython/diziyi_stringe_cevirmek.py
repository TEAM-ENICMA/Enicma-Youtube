from Bio.Seq import Seq

dizi = Seq("GATCGATGGGCCTATATAGGATCGAAAATCGC")

str_dizi = str(dizi)
print(str_dizi)

fasta_format_string = ">Isim\n%s\n" % dizi
print(fasta_format_string)