from Bio import Phylo

agac = Phylo.read("example.xml", "phyloxml")
print(agac)

Phylo.draw_ascii(agac)
Phylo.draw(agac)

agac.root.color = "blue"
agac.clade[0].color = "red"

Phylo.draw(agac, branch_labels = lambda c: c.branch_length)