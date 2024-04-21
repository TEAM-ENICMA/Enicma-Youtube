# Erişim Engelleme - Kapsülleme (Encapsulation) Özelliği

# enfeksiyon ---> ilaclı tedavi
# fiziksel yaralama ---> cerrahi müdahale
# zihinsel travma ---> psikoterapi

class Hastalar:

    def __init__(self, hasta_ismi, hasta_yasi, cinsiyet, teshis):
        self.__hasta_ismi = hasta_ismi
        self.__hasta_yasi = hasta_yasi
        self.__cinsiyet = cinsiyet
        self.teshis = teshis

    def __hasta_bilgileri(self):
        return "Hastanin ismi: {}, yasi: {}, cinsiyeti: {}".format(self.__hasta_ismi, self.__hasta_yasi, self.__cinsiyet)
    
    def __tedavi_yontemi(self):
        if self.teshis == "enfeksiyon":
            return "ilacli tedavi"
        elif self.teshis == "fiziksel yaralanma":
            return "cerrahi mudahale"
        elif self.teshis == "zihinsel travma":
            return "psikoterapi"
        
hasta1 = Hastalar("Selim", 34, "erkek", "enfeksiyon")
hasta2 = Hastalar("Zeynep", 27, "kadin", "zihinsel travma")

print(hasta1.__hasta_ismi)
print(hasta1.__hasta_bilgileri())
print(hasta2.__tedavi_yontemi())