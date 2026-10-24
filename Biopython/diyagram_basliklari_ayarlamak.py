from Bio.SeqFeature import SeqFeature, SimpleLocation
from Bio.Graphics import GenomeDiagram
from reportlab.lib.units import cm

gd_diyagram = GenomeDiagram.Diagram("Deneme")
gd_iz = gd_diyagram.new_track(1, greytrack = False)
gd_ozellik_kumesi = gd_iz.new_set()

ozellik = SeqFeature(SimpleLocation(25, 125, strand = +1))
gd_ozellik_kumesi.add_feature(ozellik, name = "Esas Zincir", label = True,
                              color = "green", label_size = 25, label_angle = 0, label_color = "red")

ozellik = SeqFeature(SimpleLocation(150, 250, strand = None))
gd_ozellik_kumesi.add_feature(ozellik, name = "Zincir Bilinmiyor", label = True,
                              color = "purple", label_position = "end", label_size = 10, label_angle = 90, label_color = "red")

ozellik = SeqFeature(SimpleLocation(275, 375, strand = -1))
gd_ozellik_kumesi.add_feature(ozellik, name = "Tamamlayici Zincir", label = True,
                              color = "blue", label_position = "middle", label_size = 8, label_angle = -90, label_color = "red")

gd_diyagram.draw(
    format = "linear",
    pagesize = (15 * cm, 10 * cm),
    fragments = 1,
    start = 0,
    end = 400 
)

gd_diyagram.write("deneme.pdf", "PDF")