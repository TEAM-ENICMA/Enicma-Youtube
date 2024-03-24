import itertools

# itertools modulu ile herhangi bir değişkeni 'n' kez tekrarlayabiliriz

x = 10
tekrar_sayisi = 5

tekrar = list(itertools.repeat(x, tekrar_sayisi))
print(str(x) + " sayisi " + str(tekrar_sayisi) + " kez tekrar etmistir: " + str(tekrar))

x = "A"
tekrar_sayisi = 7

tekrar = list(itertools.repeat(x, tekrar_sayisi))
print(str(x) + " karakteri " + str(tekrar_sayisi) + " kez tekrar etmistir: " + str(tekrar))

# itertools yardimiyla permutasyon ve kombinasyon hesaplanabilmektedir.

p = [0, 1]
q = 2

permutasyon = list(itertools.permutations(p, q))
print(str(p) + " listesinin " + str(q) + "'li permutasyonu: " + str(permutasyon) + " 'dir.")

kombinasyon = list(itertools.combinations(p, q))
print(str(p) + " listesinin " + str(q) + "'li kombinasyonu: " + str(kombinasyon) + " 'dir.")

# itertools aracılığıyla "ATGC" nükleotitlerinin potansiyel dimerlerini hesaplama:

n = "ATGC"

dimer = list(itertools.product(n, repeat = 2))
print("A, T, G, C nükleotitlerinin potansiyel dimerleri:", dimer)
