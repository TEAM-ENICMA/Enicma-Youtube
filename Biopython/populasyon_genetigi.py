from Bio.PopGen import GenePop

with open("ornek.gen") as dosya:
    kayit = GenePop.read(dosya)

print(kayit)

kayit.remove_population(0)

print(kayit)

kayit.remove_locus_by_position(0)

print(kayit)

kayit.remove_locus_by_name("Locus1")

print(kayit)