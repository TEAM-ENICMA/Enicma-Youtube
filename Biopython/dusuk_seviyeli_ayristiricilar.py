from Bio.SeqIO.FastaIO import SimpleFastaParser

basliklar = []
diziler = []

with open("ls_orchid.fasta") as dosya:
    for baslik, dizi in SimpleFastaParser(dosya):
        basliklar.append(baslik)
        diziler.append(dizi)

print(basliklar[:5])
print(diziler[:5])


from Bio.SeqIO.QualityIO import FastqGeneralIterator

basliklar = []
diziler = []
skorlar = []

with open("aaa.fastq") as dosya:
    for baslik, dizi, skor in FastqGeneralIterator(dosya):
        basliklar.append(baslik)
        diziler.append(dizi)
        skorlar.append(skor)

print(basliklar[:5])
print(diziler[:5])
print(skor[:5])