from Bio.Seq import Seq

dizi = Seq("GATCGATGGGCCTATATAGGATCGAAAATCGC")
print("esas dizi:", dizi)

print("tamamlayici:", dizi.complement())
print("ters tamamlayici:", dizi.reverse_complement())

print("dizinin tersi:", dizi[::-1])

protein = Seq("EVRNAK")
print(protein.complement())