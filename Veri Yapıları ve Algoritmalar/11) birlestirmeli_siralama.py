# Birleştirmeli Sıralama Algoritması (Merge Sort Algorithm)

"""
Birleştirmeli siralama algoritmasi, sayisal değerlerine göre karişik siraya sahip bir diziyi, her biri birer eleman içerecek
şekilde küçük alt dizilere bölüp, bu alt diziler arasindaki sayilari büyüklüklerine göre kiyaslayip düzenledikten sonra tekrar
birleştirerek küçükten büyüğe(veya büyükten küçüğe) doğru sirali bir dizi oluşturacak şekilde yeniden düzenleyen bir siralama
algoritmasidir.

Örnek;

[6, 5, 3, 1, 8, 7, 2, 4] listesi birleştirmeli siralama algoritmasi ile siralansin,
"""

def birlestirmeli_siralama(liste):

    if len(liste) > 1:
        
        orta_deger = int(len(liste) / 2)
        sol_yarim = liste[:orta_deger]
        sag_yarim = liste[orta_deger:]

        birlestirmeli_siralama(sol_yarim)
        birlestirmeli_siralama(sag_yarim)

        sol_yineleyici = 0
        sag_yineleyici = 0
        yineleyici = 0

        while sol_yineleyici < len(sol_yarim) and sag_yineleyici < len(sag_yarim):

            if sol_yarim[sol_yineleyici] <= sag_yarim[sag_yineleyici]:
                liste[yineleyici] = sol_yarim[sol_yineleyici]
                sol_yineleyici += 1
            else:
                liste[yineleyici] = sag_yarim[sag_yineleyici]
                sag_yineleyici +=1

            yineleyici += 1

        while sol_yineleyici < len(sol_yarim):

            liste[yineleyici] = sol_yarim[sol_yineleyici]
            sol_yineleyici += 1
            yineleyici += 1

        while sag_yineleyici < len(sag_yarim):

            liste[yineleyici] = sag_yarim[sag_yineleyici]
            sag_yineleyici += 1
            yineleyici += 1

    return liste

"""
Liste oluşturulur.
"""

liste = [6, 5, 3, 1, 8, 7, 2, 4]

"""
Algoritma çaliştirilir ve "sirali_liste" isimli değişkene atanir. Sonuçlar yazdirilir.
"""

sirali_liste = birlestirmeli_siralama(liste)
print(sirali_liste)
