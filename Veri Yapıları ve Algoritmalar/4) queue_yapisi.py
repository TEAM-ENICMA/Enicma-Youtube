#Queue (Kuyruk) Yapısı

"""
Kuyruk veri yapisi da tipki yiğin veri yapisi gibi doğrusal bir veri yapisidir. Aradaki fark ise, kuyruk veri
yapisindaki gibi tek giriş ve çikişa sahip olmamasidir.

Örnek vermek gerekirse, kuyruk veri yapilari bir bilet kuyruğunda bekleyen insanlara benzetilebilir. Bu örnekte
insanlar verilerdir. Bilet kuyruğuna ilk giren kişi, bileti de ilk alan kişi olup siradan ayrilacaktir. Bu kural
'İlk giren ilk çikar (FIFO - First In First Out)' olarak tanimlanir.

Örnek;
"""

Q = []

Q.insert(0, 1)
Q.insert(0, 2)
Q.insert(0, 3)
Q.insert(0, 4)
Q.insert(0, 5)

print(Q)

Q.pop()
Q.pop()
Q.pop()

print(Q)
