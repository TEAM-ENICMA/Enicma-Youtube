from Bio.Seq import Seq, MutableSeq

dizi = Seq("GCCATTGTAATGGGCCGCTGAAAGGGTGCCCGA")
print(dizi.index("ATGGGCCGC"))
print(dizi.index(b"ATGGGCCGC"))
print(dizi.index(bytearray(b"ATGGGCCGC")))
print(dizi.index(Seq("ATGGGCCGC")))
print(dizi.index(MutableSeq("ATGGGCCGC")))

#print(dizi.index("ACTG"))

print(dizi.find("ACTG"))

print(dizi.find("CC"))
print(dizi.rfind("CC"))

for index, sub in dizi.search(["CC", "GGG", "CC"]):
    print(index, sub)