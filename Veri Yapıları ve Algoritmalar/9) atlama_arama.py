# Atlama Arama Algoritması (Jump Search Algorithm)
"""
Atlama arama algoritmasi, ikili arama gibi sirali olan bir dizi içerisinde istenilen bir değerin olup olmadiğini bulmaya çalişan bir
arama algoritmasidir.

Çalişma prensibi şu şekildedir; Dizideki eleman sayisindan küçük, belirli bir atlama değeri belirlenir. Dizinin en başindan, atlama
değeri kadar ilerlenir. Atlama değerinin sonundaki endekse sahip eleman, aranan değerden küçükse, atlama adimi kadar ilerlemeye devam
eder. Eğer aranan değerden büyükse, atlama değerinden geriye doğru atlama değerinin bir eksiği kadar ilerler ve aranan değer bulunana
kadar devam eder.

Örnek;

[1, 2, 3, 4, 5, 6, 7, 8, 9] listesi içersinde, 5 değeri atlama arama algoritmasi ile bulunsun (Atlama değeri 3 olarak belirlensin),

Öncelikle dizide atlama değeri kadar ilerlenir. Atlanan noktadaki değerin aranan değerden küçük olmasi durumunda döngü devam eder
ve atlama değeri kadar ilerler. Eğer ilk döngüden hiç çikilmazsa aranan değer yok demektir. Program ilk döngüden çikarsa aranan değer,
atlama değerinin altinda kalmiş demektir. Böylelikle ikinci döngüye girer ve atlama araliğinda, aranan değer bulunana kadar doğrusal
arama yapilir.
"""

def atlama_arama(liste, deger):
    atlama_degeri = 3
    baslangic_endeksi = 0

    while liste[int(min(atlama_degeri, len(liste)) - 1)] < deger:
        baslangic_endeksi = atlama_degeri
        atlama_degeri += 3

        if baslangic_endeksi >= len(liste):
            return "y"

    while liste[int(baslangic_endeksi)] < deger:
        baslangic_endeksi += 1

        if baslangic_endeksi == min(atlama_degeri, len(liste)):
            return "y"

    if liste[int(baslangic_endeksi)] == deger:
        return int(baslangic_endeksi)

    return "y"

"""
Liste oluşturulur ve değer değişkenine '5' değeri atanir.
"""

liste = [1, 2, 3, 4, 5, 6, 7, 8, 9]
deger = 5

"""
Algoritma çaliştirilir, sonuclar yazdirilir. Verdiğimiz örneğe göre 5 sayisi listede vardir ve 4. endekse karşilik gelmektedir.
Bu nedenle 'Aranan elemanin listedeki endeksi: 4' çiktisi oluşacaktir.
"""

sonuc = atlama_arama(liste, deger)

if sonuc == "y":
    print("Aranan eleman listede yok")
else:
    print("Aranan elemanin listedeki endeksi:", sonuc)
