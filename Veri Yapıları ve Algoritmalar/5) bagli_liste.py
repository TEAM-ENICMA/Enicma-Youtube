# Bağlı Liste (Linked List) Yapısı

"""
Bağli liste veri yapisi, elemanlarinin sirasinin fiziksel bellekteki konumuna göre belirlenmediği doğrusal bir veri
yapisidir. Bu anlamda siralama bakimindan önceki veri yapilarindan farklilik gösterir. Bu veri yapisinda her eleman
kendi değeri ile birlikte sira yapisini da barindirir.

Bağli listeler düğümlerden (nodes) oluşur. Bu düğümler, iki kompartimandan oluşan birer tren vagonuna benzetilebilir.
Kompartimanlardan birisi elemanin değerini içerir, diğeri ise düğümün yani vagonun hangi diğer vagona bağlanacağini
diğer bir deyişle vagonlarin içerisindeki siralamasini gösterir.

Örnek;

Yapiyi yaratmak için, bir düğüm ve bir bağli liste objesi oluşturulmalidir,
"""

class Dugum:

    def __init__(self, deger = None, baglayici = None):
        self.deger = deger
        self.baglayici = baglayici

class BagliListe:

    def __init__(self, baslangic = None):
        self.baslangic = baslangic

    def siralamayiGoster(self):
        sira = self.baslangic
        while sira != None:
            print(sira.deger)
            sira = sira.baglayici

"""
Bağli liste objesinin içerisine ilk düğüm yerleştirilir.
Daha sonra, gerektiği kadar diğer düğümler oluşturulur.

Örneğin: '1' başlangiç değeri olacak şekilde, içinde 1, 2, 3 ve 4 değerlerini taşiyan, bağlantisiz düğümler oluşturulsun,
"""

bagli_liste = BagliListe()
bagli_liste.baslangic = Dugum(1)

ikinci_dugum = Dugum(2)
ucuncu_dugum = Dugum(3)
dorduncu_dugum = Dugum(4)

"""
Başlangiç düğümünden başlayarak, diğer düğümler istenilen sira ile birbirine bağlanabilir.

Örneğin: başlangiç ---> ikinci ---> dördüncü ---> üçüncü, şeklinde birbirine bağlansin,
"""

bagli_liste.baslangic.baglayici = ikinci_dugum
ikinci_dugum.baglayici = dorduncu_dugum
dorduncu_dugum.baglayici = ucuncu_dugum

bagli_liste.siralamayiGoster()
