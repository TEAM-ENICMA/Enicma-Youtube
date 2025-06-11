from Bio.Seq import Seq

coding = Seq("ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG")
print("coding:", coding)

template = coding.reverse_complement()
print("template:", template)

mrna = coding.transcribe()
print("mrna:", mrna)

mrna = template.reverse_complement().transcribe()
print("mrna:", mrna)

mrna = Seq("AUGGCCAUUGUAAUGGGCCGCUGAAAGGGUGCCCGAUAG")
coding = mrna.back_transcribe()
print("coding:", coding)

template = mrna.back_transcribe().reverse_complement()
print("template:", template)