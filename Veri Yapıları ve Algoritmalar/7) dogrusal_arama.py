## ALGORİTMALAR

# ARAMA ALGORİTMALARI (SEARCHING ALGORITHMS)

# Doğrusal Arama Algoritması (Linear Search Algorithm)
"""
Doğrusal arama algoritmasi, bir dizi içerisinde istenilen değerin olup olmadiğini diziyi en baştaki değerden en sondaki değere
kadar sirasiyla arayarak bulmaya çalişan bir algoritmadir. Arama yönü baştan sona doğru olmakla birlikte, eğer aranan değer dizi
içerisindeyse bulunduğu yerde algoritma durur ve geri kalan değerleri aramaz.

Örnek;

[1, 2, 3, 4, 5, 6, 7] listesi içerisinde, 4 değeri doğrusal arama algoritmasi ile bulunsun,

Öncelikle algoritma yapisi oluşturulur. Döngü yardimi ile liste içerisindeki her eleman sirasiyla gezilir. Aranan değer liste
içerisinde ise değerin endeksi, değilse programcinin isteğine göre seçeceği bir karakter veya sayi döndürülür.
"""

def dogrusal_arama(liste, deger):
    for i in range(0, len(liste)):
        if liste[i] == deger:
            return i
    return "y"

"""
Liste oluşturulur ve değer değişkenine '4' değeri atanir.
"""

liste = [1, 2, 3, 4, 5, 6, 7]
deger = 4

"""
Algoritma çaliştirilir, sonuclar yazdirilir. Verdiğimiz örneğe göre 4 sayisi listede vardir ve 3. endekse karşilik gelmektedir.
Bu nedenle 'Aranan elemanin listedeki endeksi: 3' çiktisi oluşacaktir.
"""

sonuc = dogrusal_arama(liste, deger)

if sonuc == "y":
    print("Aranan eleman listede yok")
else:
    print("Aranan elemanin listedeki endeksi:", sonuc)
