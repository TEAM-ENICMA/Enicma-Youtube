from Bio import SeqIO

snp = 4350
kayit = SeqIO.read("NC_005816.gb", "genbank")

for ozellik in kayit.features:
    if snp in ozellik:
        print("%s %s" % (ozellik.type, ozellik.qualifiers.get("db_xref")))