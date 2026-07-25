from Bio import Phylo

agac = Phylo.read("simple.dnd", "newick")
print(agac)

#Phylo.draw_ascii(agac)

agac.rooted = True
Phylo.draw(agac)
