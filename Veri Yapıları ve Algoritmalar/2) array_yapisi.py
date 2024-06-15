#VERİ YAPILARI

#Array(Dizi) Yapısı

"""
Bir değişkene, bir tamsayi veya bir string gibi tek bir değer vermek yerine, bir dizi değerin verilebilmesini sağlayan bir veri yapisidir.

Örnek:
        A_dizisi = [0, 1, 2, 3, 4, 5, 6]

Böylece "A_dizisi" değişkenine 0'dan 6'ya kadar olan 7 tane tamsayi değerinden oluşan bir dizi atanmiş olur.

Bu veri yapisi alan karmaşikliğini azaltmak amaciyla geliştirilmiştir. Normal şartlarda, dizi veri yapisi olmadan,
tek bir değişkene ancak bir değer atanabiliyordu. Dizi veri yapisi sayesinde bir değişkenin içerisine çok sayida
değer girilerek alan karmaşikliğinin azaltilmasi sağlanabilmiştir.

Dizi yapisinda, değişkene atanmiş olan her elemanin bir endeksi vardir. İlgili elemana ulaşabilmek için bu endeks kullanilir.
Endeks ilk elemandan itibaren, 0'dan başlayarak, artarak ilerler. Yukaridaki örneği ele alalim;
    '0' numarali elemanin endeksi 0'dir, '5' numarali elemanin endeksi 5'tir.
Eğer dizi elemanlari 1'den başliyor olsaydi, '1' numarali elemanin endeksi 0 olacakti.

Örnek;
"""
A = [1, 2, 3, 4, 5]
print("A: ", A[0])

"""
Dizideki elemanlar karakterler de olabilirler. Sirasi ile her karaktere 0'dan itibaren endeksler verilir;
"""
B = ["a", "b", "c", "d", "e"]
print("B: ", B[0])
"""
Köşeli parantezin içerisindeki iki endeksin arasina ':' koyularak, aradaki tüm elemanlar da alinabilir;
"""
C = [2, 4, 6, 8, 10]
print("C: ", C[1:4])
