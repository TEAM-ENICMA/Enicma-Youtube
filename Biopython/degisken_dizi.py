from Bio.Seq import Seq

dizi = Seq("GCCATTGTAATGGGCCGCTGAAAGGGTGCCCGA")
print(dizi)

#dizi[5] = "G"

from Bio.Seq import MutableSeq
degisken_dizi = MutableSeq(dizi)
degisken_dizi = MutableSeq("GCCATTGTAATGGGCCGCTGAAAGGGTGCCCGA")
print(degisken_dizi)

degisken_dizi[5] = "C"
print(degisken_dizi)

degisken_dizi.remove("T")
print(degisken_dizi)

degisken_dizi.reverse()
print(degisken_dizi)

yeni_dizi = Seq(degisken_dizi)
print(yeni_dizi)