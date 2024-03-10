import math

# math modulu araciligiyla matematikteki sabit sayilar elde edilebilir.

pi = math.pi
print("Pi sayisi:", pi)

e_sayisi = math.e
print("e sayisi:", e_sayisi)

# math modulu sayesinde kuvvet alma, karekök alma, logaritma gibi işlemler yapılabilmektedir.

x = 8
kuvvet = math.pow(x, 2)
print(str(x) + "'in 2. kuvveti " + str(kuvvet) + "'dir.")

karekok = math.sqrt(x)
print(str(x) + "'in karekökü " + str(karekok) + "'dir.")

logaritma10 = math.log10(x)
logaritma2 = math.log2(x)

print(str(x) + "'in 10 tabaninda logaritmasi " + str(logaritma10) + "'dir.")
print(str(x) + "'in 2 tabaninda logaritmasi " + str(logaritma2) + "'dir.")

# math modulu ile bir sayının faktoriyeli hesaplanabilir.

a = 5
f = math.factorial(5)
print(str(a) + " sayisinin faktoriyeli " + str(f) + "'dir.")


