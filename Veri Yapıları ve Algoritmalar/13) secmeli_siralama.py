# Seçmeli Sıralama Algoritması (Selection Sort Algorithm)

"""
Seçmeli siralama algoritmasi, sayisal değerlerine göre karişik siraya sahip bir dizideki en küçük elemani dizinin
ilk elemani ile yer değiştirerek, ve sonraki her adimda geriye kalan değerler için ayni işlemi uygulayarak küçükten
büyüğe(veya büyükten küçüğe) doğru sirali bir dizi oluşturacak şekilde düzenleyen bir siralama algoritmasidir.

Örnek;

[6, 5, 3, 1, 8, 7, 2, 4] listesi seçmeli siralama algoritmasi ile siralansin,
"""

def secmeli_siralama(liste):

    for e in range(len(liste)):
        en_kucuk_deger_endeksi = e

        for k in range(e + 1, len(liste)):

            if liste[k] < liste[en_kucuk_deger_endeksi]:
                en_kucuk_deger_endeksi = k

        degistirici = liste[e]
        liste[e] = liste[en_kucuk_deger_endeksi]
        liste[en_kucuk_deger_endeksi] = degistirici

    return liste

"""
Liste oluşturulur.
"""

liste = [6, 5, 3, 1, 8, 7, 2, 4]

"""
Algoritma çaliştirilir ve "sirali_liste" isimli değişkene atanir. Sonuçlar yazdirilir.
"""

sirali_liste = secmeli_siralama(liste)
print(sirali_liste)
