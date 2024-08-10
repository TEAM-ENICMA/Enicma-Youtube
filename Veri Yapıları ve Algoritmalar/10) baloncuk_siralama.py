# SIRALAMA ALGORİTMALARI (SORTING ALGORITHMS)

# Baloncuk Sıralama Algoritması (Bubble Sort Algorithm)

"""
Baloncuk siralama algoritmasi, sayisal değerlerine göre karişik siraya sahip bir dizideki, her adimda iki değeri büyüklüklerine
göre birbirleri ile kiyaslayarak düzelten ve son durumda küçükten büyüğe(veya büyükten küçüğe) doğru sirali bir dizi oluşturacak
şekilde düzenleyen bir siralama algoritmasidir.

Örnek;

[6, 5, 3, 1, 8, 7, 2, 4] listesi baloncuk algoritmasi ile siralansin,
"""

def baloncuk_siralama(liste):

    for e in range(len(liste) - 1, 0, -1):
        for k in range(e):
            print(liste)

            if liste[k] > liste[k + 1]:
                degistirici = liste[k]
                liste[k] = liste[k + 1]
                liste[k + 1] = degistirici

    return liste

"""
Liste oluşturulur.
"""

liste = [6, 5, 3, 1, 8, 7, 2, 4]

"""
Algoritma çaliştirilir ve "sirali_liste" isimli değişkene atanir. Sonuçlar yazdirilir.
"""

sirali_liste = baloncuk_siralama(liste)
print(sirali_liste)
