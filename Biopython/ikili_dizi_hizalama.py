from Bio import Align

hizalayici = Align.PairwiseAligner()
hizalayici = Align.PairwiseAligner(match_score = 1.0)

dizi1 = "GAACT"
dizi2 = "GAT"

skor = hizalayici.score(dizi1, dizi2)
print(skor)

hizalamalar = hizalayici.align(dizi1, dizi2)

for hizalama in hizalamalar:
    print(hizalama)
    print(hizalama.score)
    print(hizalama.target)
    print(hizalama.query)

print(hizalamalar.score)


hizalama = hizalamalar[0]
print(hizalama.coordinates)
print(len(hizalama))
print(hizalama.length)
print(hizalama.aligned)

hizalama = hizalamalar[1]
print(hizalama.aligned)

hizalayici.mode = "global"
hizalayici.mismatch_score = -10
hizalamalar = hizalayici.align("AAACAAA", "AAAGAAA")

print(len(hizalamalar))

print(hizalamalar[0])
print(hizalamalar[1])

hizalayici.mode = "local"
hizalayici.open_gap_score = -1
hizalayici.extend_gap_score = 0

kromozom = "AAAAAAAACCCCCCCAAAAAAAAAAAGGGGGGAAAAAAAA"
transkript = "CCCCCCCGGGGGG"

hizalamalar1 = hizalayici.align(kromozom, transkript)
print(len(hizalamalar1))
print(hizalamalar1[0])