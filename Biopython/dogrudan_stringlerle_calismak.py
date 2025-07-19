from Bio.Seq import reverse_complement, transcribe, back_transcribe, translate

string = "GCTGTTATGGGTCGTTGGAAGGGTGGTCGTGCTGCTGGTTAG"
print(reverse_complement(string))
print(transcribe(string))
print(back_transcribe(string))
print(translate(string))