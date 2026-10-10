from reportlab.lib import colors
from reportlab.lib.units import cm
from Bio.Graphics import GenomeDiagram
from Bio import SeqIO

kayit = SeqIO.read("NC_005816.gb", "genbank")

gd_ozellik_kumesi = GenomeDiagram.FeatureSet()
for ozellik in kayit.features:
    if ozellik.type != "gene":
        continue
    if len(gd_ozellik_kumesi) % 2 == 0:
        renk = colors.blue
    else:
        renk = colors.lightblue

    gd_ozellik_kumesi.add_feature(ozellik, color = renk, label = True)

gd_iz = GenomeDiagram.Track(name = "Annotated Features")
gd_diyagram = GenomeDiagram.Diagram("Yersinia Pestis")

gd_iz.add_set(gd_ozellik_kumesi)
gd_diyagram.add_track(gd_iz, 1)

gd_diyagram.draw(
    format = "circular",
    circular = True,
    pagesize = (20 * cm, 20 * cm),
    start = 0,
    end = len(kayit),
    circle_core = 0.7
)

gd_diyagram.write("yersinia.pdf", "PDF")