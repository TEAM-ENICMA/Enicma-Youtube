#Algoritma Nedir?

"""
Algoritma bir problemin çözümü için geliştirilen yöntem.

Örnek: Bir infüzyon pompasinin her gün saat 4 ile 6 arasinda bir hastaya serum enjekte etmesi gerekiyor ----> problem
       Her 24 saatte bir, saat 4 ile 6 arasinda infüzyon pompasini calistiracak sistemi aktiflestir -----> algoritma

       ##################################################################################################################

       Her 24 saat için,
           Eğer saat 4'ten sonra ve 6'dan önce ise,
               Infüzyon pompasini calistir.
           Değilse,
               Infüzyon pompasini durdur.  -------> yalanci kod (pseudo code)
               
       ###################################################################################################################
               
       def infüzyon_pompasini_calistir()
            pass
            
       def infüzyon_pompasini_durdur()
            pass
       
       gün = 24   
       for saat in range(1, gün + 1):
           if saat >= 4 and saat <= 6:
               infüzyon_pompasini_calistir()
           else:
               infüzyon_pompasini_durdur()  ----------> Python kodu

"""

#Karmaşıklık Nedir?


"""
Hesaplama karmaşikliği (Computational complexity),
bir algoritmayi çaliştirmak için gerekli olan tüm kaynaklardir.

Temelde bu kaynaklar; zaman ve alan olarak ikiye ayrilir.

Doğal olarak zaman karmaşikliği ve alan karmaşikliği isminde iki tür hesap karmaşikliği elde ederiz.

Zaman karmaşikliği, bir algoritmanin çalişma süresini tanimlar.
Alan karmaşikliği, bir algoritmanin bellekte kapladiği yeri tanimlar.

İyi bir algoritma hizli çalişmali ve bellekte az yer kaplamalidir.

Algoritmalarin zaman ve alan karmaşikliklari Büyük O Notasyonu (Big-O Notation) ile gösterilir.
"""

#Kaynaklar

"""
https://medium.com/kodcular/nedir-bu-big-o-notation-b8b9f1416d30

https://medium.com/yaz%C4%B1l%C4%B1m-ve-bili%C5%9Fim-kul%C3%BCb%C3%BC/big-o-notation-notasyonu-nedi%CC%87r-490f41de6f76
"""
