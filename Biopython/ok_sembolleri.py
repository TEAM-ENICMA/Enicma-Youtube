from Bio.SeqFeature import SeqFeature, SimpleLocation
from Bio.Graphics import GenomeDiagram
from reportlab.lib.units import cm

gd_diyagram = GenomeDiagram.Diagram("Deneme")
gd_iz = gd_diyagram.new_track(1, greytrack = False)
gd_ozellik_kumesi = gd_iz.new_set()

ozellik = SeqFeature(SimpleLocation(25, 125, strand = +1))
gd_ozellik_kumesi.add_feature(ozellik, name = "Esas Zincir", label = True,
                              sigil = "ARROW", color = "blue", arrowshaft_height = 1.0, arrowhead_length = 0.25)

ozellik = SeqFeature(SimpleLocation(150, 250, strand = None))
gd_ozellik_kumesi.add_feature(ozellik, name = "Zincir Bilinmiyor", label = True,
                              sigil = "ARROW", color = "orange", arrowshaft_height = 0.2, arrowhead_length = 1.0)

ozellik = SeqFeature(SimpleLocation(275, 375, strand = -1))
gd_ozellik_kumesi.add_feature(ozellik, name = "Tamamlayici Zincir", label = True,
                              sigil = "ARROW", color = "red", arrowshaft_height = 0.1, arrowhead_length = 10000)

gd_diyagram.draw(
    format = "linear",
    pagesize = (15 * cm, 4 * cm),
    fragments = 1,
    start = 0,
    end = 400 
)

gd_diyagram.write("deneme.pdf", "PDF")