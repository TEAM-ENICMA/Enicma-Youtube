from Bio.Seq import Seq

ornekler = [
    Seq("TACAA"),
    Seq("TACGC"),
    Seq("TACAC"),
    Seq("TACCC"),
    Seq("AACCC"),
    Seq("AATGC"),
    Seq("AATGC")
    ]

from Bio import motifs

m = motifs.create(ornekler)
print(m.alignment.sequences)
print(m)
print(len(m))
print(m.counts)

print(m.counts["A"])
print(m.counts["T", 0])
print(m.counts["T", 2])
print(m.counts["T", 3])

print(m.counts[: , 3])

print(m.alphabet)