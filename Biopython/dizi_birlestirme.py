from Bio.Seq import Seq

dizi1 = Seq("ACTG")
dizi2 = Seq("AACCGG")

print(dizi1 + dizi2)

protein = Seq("EVRNAK")
dna = Seq("ACTG")

print(protein + dna)

dizi_listesi = [Seq("ACTG"), Seq("AACC"), Seq("GGTT")]
birlestirilmis = Seq("")
for d in dizi_listesi:
    birlestirilmis += d

print(birlestirilmis)

dizi_listesi = [Seq("ATG"), Seq("ATCCCG"), Seq("TTGCA")]
bosluklar = Seq("N" * 10)

print(bosluklar.join(dizi_listesi))