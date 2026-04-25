from Bio import AlignIO

hizalama = AlignIO.read("PF05371_seed.sth", "stockholm")
print(len(hizalama))

for kayit in hizalama:
    print(kayit.seq + " - " + kayit.id)


print(hizalama)
print(hizalama[3 : 7])
print(hizalama[2 , 6])
print(hizalama[2].seq[6])
print(hizalama[: , 6])
print(hizalama[3 : 6 , : 6])
print(hizalama[: , : 6])
print(hizalama[: , 6 : 9])
print(hizalama[: , 9 :])

birlestirilmis = hizalama[: , : 6] + hizalama[: , 9 :]
print(birlestirilmis)

birlestirilmis.sort()
print(birlestirilmis)