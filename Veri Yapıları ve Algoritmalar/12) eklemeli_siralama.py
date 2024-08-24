# Eklemeli Sıralama Algoritması (Insertion Sort Algorithm)

"""
Eklemeli siralama algoritmasi, sayisal değerlerine göre karişik siraya sahip bir dizideki, ilk elemani diziden çikartarak
yeni bir alt dizi haline getirip, geriye kalan elemanlari sirayla alt dizi içerisindeki eleman\elemanlar ile sayisal
büyüklüklerine göre kiyaslayarak alt diziye ekleyip küçükten büyüğe(veya büyükten küçüğe) doğru sirali bir dizi oluşturacak
şekilde düzenleyen bir siralama algoritmasidir.

Örnek;

[6, 5, 3, 1, 8, 7, 2, 4] listesi eklemeli siralama algoritmasi ile siralansin,
"""

def eklemeli_siralama(liste):

    for e in range(1, len(liste)):
        deger = liste[e]
        sirali_eleman_endeksi = e - 1

        while sirali_eleman_endeksi >= 0 and deger < liste[sirali_eleman_endeksi]:
            liste[sirali_eleman_endeksi + 1] = liste[sirali_eleman_endeksi]
            sirali_eleman_endeksi -= 1

        liste[sirali_eleman_endeksi + 1] = deger

    return liste

"""
Liste oluşturulur.
"""

liste = [6, 5, 3, 1, 8, 7, 2, 4]

"""
Algoritma çaliştirilir ve "sirali_liste" isimli değişkene atanir. Sonuçlar yazdirilir.
"""

sirali_liste = eklemeli_siralama(liste)
print(sirali_liste)
