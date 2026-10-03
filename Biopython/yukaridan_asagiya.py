from reportlab.lib import colors
from Bio.Graphics import GenomeDiagram
from Bio import SeqIO

kayit = SeqIO.read("NC_005816.gb", "genbank")

gd_diyagram = GenomeDiagram.Diagram("Yersinia pestis")
gd_iz = gd_diyagram.new_track(1, name = "Annotated Features")
gd_ozellik_kumesi = gd_iz.new_set()

for ozellik in kayit.features:
    if ozellik.type != "gene":
        continue
    if len(gd_ozellik_kumesi) % 2 == 0:
        renk = colors.blue
    else:
        renk = colors.lightblue

    gd_ozellik_kumesi.add_feature(ozellik, color = renk, label = True)

gd_diyagram.draw(
    format = "linear",
    orientation = "landscape",
    pagesize = "A4",
    fragments = 4,
    start = 0,
    end = len(kayit)
)

gd_diyagram.write("yersinia.pdf", "PDF")

from reportlab.lib.units import cm

gd_diyagram.draw(
    format = "circular",
    circular = True,
    pagesize = (20 * cm, 20 * cm),
    start = 0,
    end = len(kayit),
    circle_core = 0.7
)

gd_diyagram.write("yersinia.pdf", "PDF")