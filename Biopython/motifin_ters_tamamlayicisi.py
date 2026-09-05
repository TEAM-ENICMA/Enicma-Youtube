from Bio.Seq import Seq
from Bio import motifs

ornekler = [
    Seq("TACAA"),
    Seq("TACGC"),
    Seq("TACAC"),
    Seq("TACCC"),
    Seq("AACCC"),
    Seq("AATGC"),
    Seq("AATGC")
    ]

m = motifs.create(ornekler)
print(m)

t = m.reverse_complement()
print(t.consensus)
print(t.degenerate_consensus)
print(t)