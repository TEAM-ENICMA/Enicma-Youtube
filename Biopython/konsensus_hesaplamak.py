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

print(m.consensus)
print(m.anticonsensus)
print(m.degenerate_consensus)