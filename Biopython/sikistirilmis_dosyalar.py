from Bio import SeqIO

print(sum(len(i) for i in SeqIO.parse("ls_orchid.gbk", "gb")))

with open("ls_orchid.gbk") as dosya:
    print(sum(len(i) for i in SeqIO.parse(dosya, "gb")))
dosya.close()

import gzip

with gzip.open("ls_orchid.gbk.gz", "rt") as dosya:
    print(sum(len(i) for i in SeqIO.parse(dosya, "gb")))

import bz2

with bz2.open("ls_orchid.gbk.bz2", "rt") as dosya:
    print(sum(len(i) for i in SeqIO.parse(dosya, "gb")))