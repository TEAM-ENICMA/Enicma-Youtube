########### Çok Biçimlilik (Polymorphism) Özelliği ###############

class Enfeksiyon_Hastalari:

    def __init__(self, hasta_ismi, hasta_yasi, cinsiyet, teshis):
        self.hasta_ismi = hasta_ismi
        self.hasta_yasi = hasta_yasi
        self.cinsiyet = cinsiyet
        self.teshis = teshis

class Fungal_Enfeksiyonlu_Hastalar(Enfeksiyon_Hastalari):

    def tedavi_yontemi(self):
        return "{} isimli hastaya antifungal ilaclar verilecektir.".format(self.hasta_ismi)
    
class Viral_Enfeksiyonlu_Hastalar(Enfeksiyon_Hastalari):

    def tedavi_yontemi(self):
        return "{} isimli hastaya antiviral ilaclar verilecektir.".format(self.hasta_ismi)
    

hasta1 = Fungal_Enfeksiyonlu_Hastalar("Emre", 19, "erkek", "fungal enfeksiyon")
hasta2 = Viral_Enfeksiyonlu_Hastalar("Aybüke", 22, "kadin", "viral enfeksiyon")

print(hasta1.tedavi_yontemi())
print(hasta2.tedavi_yontemi())


# https://medium.com/rexven/python-ile-nesne-tabanl%C4%B1-programlama-encapsulation-inheritance-abstract-class-overriding-ve-c8553ae7325d