from reportlab.lib import colors
from reportlab.lib.units import cm
from Bio.Graphics import GenomeDiagram
from Bio import SeqIO
from Bio.SeqFeature import SeqFeature, SimpleLocation

kayit = SeqIO.read("NC_005816.gb", "genbank")

gd_diyagram = GenomeDiagram.Diagram(kayit.id)
gd_iz = gd_diyagram.new_track(1, name = "Annotated Features")
gd_ozellik_kumesi = gd_iz.new_set()

for ozellik in kayit.features:
    if ozellik.type != "gene":
        continue
    if len(gd_ozellik_kumesi) % 2 == 0:
        renk = colors.blue
    else:
        renk = colors.lightblue
    gd_ozellik_kumesi.add_feature(ozellik, color = renk, label = True,
                                  sigil = "ARROW", label_size = 14, label_angle = 0)

for bolge, isim, renk in [
    ("GAATTC", "EcoRI", colors.green),
    ("CCCGGG", "SmaI", colors.orange),
    ("AAGCTT", "HindIII", colors.red),
    ("GGATCC", "BamHI", colors.purple)
]:
    endeks = 0
    while True:
        endeks = kayit.seq.find(bolge, start = endeks)
        if endeks == -1:
            break
        ozellik = SeqFeature(SimpleLocation(endeks, (endeks + len(bolge))))
        gd_ozellik_kumesi.add_feature(ozellik, color = renk, label = True,
                                      name = isim, label_size = 10, label_color = renk)

        endeks += len(bolge)

gd_diyagram.draw(
    format = "linear",
    fragments = 4,
    pagesize = "A4",
    start = 0,
    end = len(kayit)
)

gd_diyagram.write("ornek.pdf", "PDF")

gd_diyagram.draw(
    format = "circular",
    circular = True,
    pagesize = (20 * cm, 20 * cm),
    start = 0,
    end = len(kayit),
    circle_core = 0.5
)

gd_diyagram.write("ornek.pdf", "PDF")