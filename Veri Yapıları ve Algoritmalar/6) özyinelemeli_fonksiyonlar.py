# Özyinelemeli Fonksiyonlar (Recursive Functions)
"""
Bir fonksiyonun direkt veya dolayli olarak kendini çağirmasina 'özyineleme', bu duruma sahip olan fonksiyonlara
'özyinelemeli fonksiyonlar' denir.
Özyinelemeli fonksiyonlari ifade edebilmek için verilen en yaygin örnek faktöriyel hesaplama örneğidir.

Bir sayinin faktöriyeli, 1'den sayiya kadar olan tüm sayilarin çarpimina karşilik gelen değeridir. Şu şekilde ifade edilir:

    n! = n * (n - 1) * (n - 2) * ... * 2 * 1

Örneğin, 5 sayisinin faktöriyelini ele alalim:

    5! = 5 * 4 * 3 * 2 * 1 = 120

Özyinelemeli fonksiyonlar ile faktöriyel hesaplanabilir. Bunu yapabilmek için 'n' parametresi alan bir fonksiyon oluşturulur.
fonksiyonun içerisinde 'n' sayisi 'n - 1' paramtetresi alan ayni fonksiyon ile çarpilir. çarpim işlemi sirasinda farkli parametre
ile ayni fonksiyon çağrildiğindan, bu fonksiyon özyinelemeli bir fonksiyon olur.

Örnek;
"""

def faktoriyel(n):
    if n == 0:
        return 1
    else:
        return n * faktoriyel(n - 1)

print(faktoriyel(5))
