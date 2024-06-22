#Stack (Yığın) Yapısı

"""
İşlemlerin belirli bir sirayi izleyerek gerçekleştiği doğrusal bir veri yapisidir.

Örnek vermek gerekirse, yiğin veri yapilari üst üste dizilmiş bir kitap yiğinina benzetilebilir. Bu örnekte kitaplar
verilerdir. Sirasiyla kitaplar üst üste konulduğunda, en altta kalan kitaba ulaşabilmek için üsttekilerin tek tek
kaldirilmasi gerekir. Bu kural 'İlk giren son çikar (FILO - First In Last Out)' veya 'Son giren ilk çikar (LIFO -
Last In First Out)' şeklinde isimlendirilir.

Yiğin veri yapisinin temelde 2 fonksiyonu vardir:
    1) Push: yiğina eleman eklenmesini sağlar.
    2) Pop: yiğindan eleman çikartilmasini sağlar.
    
Ayrica 'peek' fonksiyonu yiğinin en tepesindeki elemani gösterir.

Örnek;
"""

S = []

"""
Farkli dillerde 'push' ismiyle geçen fonksiyon yerine Python'da yaygin olarak 'append' kullanilir.
Dilenirse 'push' fonksiyonu kullanici tarafindan da yazilabilir.
"""

S.append(1)
S.append(2)
S.append(3)
S.append(4)
S.append(5)

print(S) 

S.pop()
S.pop()

print(S)

"""
Yiğin veri yapisinda en son eklenen eleman en üstteki eleman olduğundan, '-1' endeksli elemani gösterdiğimizde,
'peek' fonksiyonunun işini yaptirmiş oluruz.
"""

print(S[-1])
