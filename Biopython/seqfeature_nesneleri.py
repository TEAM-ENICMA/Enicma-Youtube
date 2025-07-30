from Bio import SeqFeature

baslangic_pozisyonu = SeqFeature.AfterPosition(5)
bitis_pozisyonu = SeqFeature.BetweenPosition(9, left = 8, right = 9)

konum = SeqFeature.SimpleLocation(baslangic_pozisyonu, bitis_pozisyonu)

print(konum)

print(konum.start)
print(konum.end)

print(int(konum.start))
print(int(konum.end))

kesin_konum = SeqFeature.SimpleLocation(5, 9, strand = 1)
print(kesin_konum)
print(kesin_konum.start)
print(kesin_konum.end)

kesin_konum.type = "promoter"
print(kesin_konum.type)
print(kesin_konum.strand)