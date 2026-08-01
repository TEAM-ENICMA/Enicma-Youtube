from Bio import Phylo

agac = Phylo.read("simple.dnd", "newick")
print(agac)

agac.root.color = (128, 128, 128)
agac.root.color = "#808080"
agac.root.color = "gray"

mrca = agac.common_ancestor({"name" : "E"}, {"name" : "F"})
mrca.color = "salmon"

agac.clade[0, 1].color = "blue"

Phylo.draw(agac)