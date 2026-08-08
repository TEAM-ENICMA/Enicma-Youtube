from Bio import Phylo

agac = Phylo.read("int_node_labels.nwk", "newick")
print(agac)

agaclar = Phylo.parse("phyloxml_examples.xml", "phyloxml")
for agac in agaclar:
    print(agac)
agac1 = next(agaclar)

Phylo.write(agac1, "agac1.nwk", "newick")
Phylo.write(agaclar, "butun_agaclar.xml", "phyloxml")

Phylo.convert("agac1.nwk", "newick", "agac1.xml", "nexml")
Phylo.convert("butun_agaclar.xml", "phyloxml", "butun_agaclar.nex", "nexus")