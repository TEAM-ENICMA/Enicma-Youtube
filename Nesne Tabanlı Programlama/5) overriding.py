########### Üzerine Yazma (Overriding) Özelliği ###############

class Hastalar:

    def __init__(self, hasta_ismi, hasta_yasi, cinsiyet, teshis):
        self.hasta_ismi = hasta_ismi
        self.hasta_yasi = hasta_yasi
        self.cinsiyet = cinsiyet
        self.teshis = teshis

    def hasta_bilgileri(self):
        return "Hastanin ismi: {}, yasi: {}, cinsiyeti: {}".format(self.hasta_ismi, self.hasta_yasi, self.cinsiyet)
    
class Tedavi(Hastalar):

    def hasta_bilgileri(self):
        return "{} isimli hasta icin konan teshis: {}".format(self.hasta_ismi, self.teshis)
    
    def tedavi_yontemi(self):
        if self.teshis == "enfeksiyon":
            return "ilacli tedavi"
        elif self.teshis == "fiziksel yaralanma":
            return "cerrahi mudahale"
        elif self.teshis == "zihinsel travma":
            return "psikoterapi"
        
hasta1 = Hastalar("Selim", 34, "erkek", "enfeksiyon")
hasta2 = Tedavi("Zeynep", 27, "kadin", "zihinsel travma")

print(hasta1.hasta_bilgileri())
print(hasta2.hasta_bilgileri())