import random

# random modulu sayesinde belirli bir aralik içerisinde rastgele sayilar uretilebilir.

rastgele_sayi = random.randint(0, 100)
print("0 ile 100 arasinda rastgele bir sayi:", rastgele_sayi)

rastgele_cift_sayi = random.randrange(0, 100, 2)
print("0 ile 100 arasinda rastgele bir sayi cift sayi:", rastgele_cift_sayi)

# random modulu ile bir veri yapisi icerisinden rastgele bir deger secilebilir.

veri_yapisi = [0, 1, 2, 3, 4, 5]
listeden_secilen_deger = random.choice(veri_yapisi)
print("Listeden rastgele seçilen deger:", listeden_secilen_deger)

# Veri yapisi icerisinden rasgele birden fazla deger de secilebilir.

renk_listesi = ["kirmizi", "mavi", "yesil", "sari", "beyaz", "siyah", "mor", "turuncu"]
rastgele_secilen_iki_renk = random.sample(renk_listesi, k = 2)
print("Listeden secilen renkler:", rastgele_secilen_iki_renk)
