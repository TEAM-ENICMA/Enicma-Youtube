from Bio.Seq import Seq

dizi = Seq({117512683: "TTGAAAACCTGAATGTGAGAGTCAGTCAAGGATAGT"}, length = 159345973)

try:
    print(dizi[1000:1020])
except:
    print("Seq(None, length=%i)" % len(dizi[1000:1020]))

try:
    print(dizi[117512670:117512690])
except:
    print("Seq({%i:%s}, length=%i)" % ((117512683 - 117512670), dizi[117512683:117512690], (117512690 - 117512670)))