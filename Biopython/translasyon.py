from Bio.Seq import Seq

mrna = Seq("AUGGCCAUUGUAAUGGGCCGCUGAAAGGGUGCCCGAUAG")
print("mrna:", mrna)

protein = mrna.translate()
print("protein:", protein)

coding = Seq("ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG")
print("coding:", coding)

protein = coding.translate()
print("protein:", protein)

mitokodriyal = coding.translate(table = "Vertebrate Mitochondrial")
print("mitokondriyal:", mitokodriyal)

mitokodriyal = coding.translate(table = 2)
print("mitokondriyal:", mitokodriyal)

protein = coding.translate()
print("tum protein:", protein)

protein = coding.translate(to_stop = True)
print("durdurulmus protein:", protein)

mitokodriyal = coding.translate(table = 2)
print("tum mitokodriyal:", mitokodriyal)

mitokodriyal = coding.translate(table = 2, to_stop = True)
print("durdurulmus mitokodriyal:", mitokodriyal)

mitokodriyal = coding.translate(table = 2, stop_symbol = "@")
print("sembol:", mitokodriyal)


gen = Seq(
    "GTGAAAAAGATGCAATCTATCGTACTCGCACTTTCCCTGGTTCTGGTCGCTCCCATGGCA"
    "GCACAGGCTGCGGAAATTACGTTAGTCCCGTCAGTAAAATTACAGATAGGCGATCGTGAT"
    "AATCGTGGCTATTACTGGGATGGAGGTCACTGGCGCGACCACGGCTGGTGGAAACAACAT"
    "TATGAATGGCGAGGCAATCGCTGGCACCTACACGGACCGCCGCCACCGCCGCGCCACCAT"
    "AAGAAAGCTCCTCATGATCATCACGGCGGTCATGGTCCAGGCAAACATCACCGCTAA")

protein = gen.translate(table = "Bacterial")
print("bakteriyel protein:", protein)

protein = gen.translate(table = "Bacterial", to_stop = True)
print("durdurulmus protein:", protein)

cds = gen.translate(table = "Bacterial", cds = True)
print("cds:", cds)