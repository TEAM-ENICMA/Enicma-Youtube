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

m_bolunmus = m[2 : -1]
print(m_bolunmus)

print(m_bolunmus.consensus)
print(m_bolunmus.degenerate_consensus)