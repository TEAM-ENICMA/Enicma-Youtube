from Bio import Align

hizalayici = Align.PairwiseAligner()

def bosluk_skor_fonksiyonu(baslangic, uzunluk):

    if baslangic == 2:
        return -1000
    else:
        return -1 * uzunluk
    
hizalayici.query_gap_score = bosluk_skor_fonksiyonu

hizalamalar = hizalayici.align("AACTT", "AATT")

for hizalama in hizalamalar:
    print(hizalama)

#AA C TT
#AA - TT ------> eslesme 1 puan ise toplam skor 4 - 1000 = -996