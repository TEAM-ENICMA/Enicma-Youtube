from Bio import AlignIO

hizalamalar = AlignIO.parse("belirsiz_hizalama.faa", "fasta", seq_count = 2)

for hizalama in hizalamalar:
    print("Hizalama uzunlugu: %i" % hizalama.get_alignment_length())
    for kayit in hizalama:
        print(kayit.seq + " - " + kayit.id)
    print()