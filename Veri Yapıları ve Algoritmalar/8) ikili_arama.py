# İkili Arama Algoritması (Binary Search Algorithm)
"""
İkili arama algoritmasi, sirali bir dizi içerisinde istenen bir değerin olup olmadiğini bulmaya çalişan bir arama algoritmasidir.
Algoritmanin doğasinda sayilarin büyüklük ve küçüklüklerini kiyaslama olduğundan, dizinin sirali olmasi gerekir.

Çalişma prensibi şu şekildedir; öncelikle dizinin en ortasindaki değere gidilir ve aranan değerin bu olup olmadiği kontrol edilir.
Eğer aranan değer değilse ve aranan değer ortadaki değerden küçükse, ortadaki değerin öncesindeki yarimin orta değerine gidilip
kontrol edilir. Eğer büyükse, ortadaki değerin sonrasindaki yarimin orta değerine gidilip kontrol edilir. Aranan değer dizide varsa,
değer bulunana kadar işlemler devam eder.

Örnek;

[1, 2, 3, 4, 5, 6, 7, 8, 9, 10] listesi içersinde, 7 değeri ikili arama algoritmasi ile bulunsun,

Dizinin ortasindaki değere gidilip kontrol edilir. Eğer aranan değer bu değerden daha küçükse döngü yardimi ile alt yarima,
daha büyükse üst yarima gidilir ve yarimdaki orta değer kontrol edilir. Eğer herhangi bir orta değer aranan değerse fonksiyon
bu değerin endeksini döndürür. Eğer aranan değer yoksa programcinin isteğine göre seçeceği bir karakter veya sayi döndürülür.
"""

def ikili_arama(liste, deger):
    baslangic_endeksi = 0
    orta_endeks = 0
    bitis_endeksi = len(liste) - 1

    while baslangic_endeksi <= bitis_endeksi:
        orta_endeks = (baslangic_endeksi + bitis_endeksi) // 2

        if liste[orta_endeks] < deger:
            baslangic_endeksi = orta_endeks + 1

        elif liste[orta_endeks] > deger:
            bitis_endeksi = orta_endeks - 1

        else:
            return orta_endeks

    return "y"

"""
Liste oluşturulur ve değer değişkenine '7' değeri atanir.
"""

liste = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
deger = 7

"""
Algoritma çaliştirilir, sonuclar yazdirilir. Verdiğimiz örneğe göre 7 sayisi listede vardir ve 6. endekse karşilik gelmektedir.
Bu nedenle 'Aranan elemanin listedeki endeksi: 6' çiktisi oluşacaktir.
"""

sonuc = ikili_arama(liste, deger)

if sonuc == "y":
    print("Aranan eleman listede yok")
else:
    print("Aranan elemanin listedeki endeksi:", sonuc)
