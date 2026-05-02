from Bio import AlignIO
import numpy as np

hizalama = AlignIO.read("PF05371_seed.sth", "stockholm")
hizalama_numpy = np.array(hizalama)

print(hizalama_numpy.shape)
print(hizalama_numpy)
