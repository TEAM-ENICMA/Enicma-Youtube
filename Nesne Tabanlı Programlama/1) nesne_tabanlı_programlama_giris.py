class Programlar:
    program_ismi = "program1"
    gelistirildigi_dil = "python"
    platform = "linux"

birinci_program = Programlar

print(birinci_program.program_ismi)
print(birinci_program.gelistirildigi_dil)
print(birinci_program.platform)

ikinci_program = Programlar

ikinci_program.program_ismi = "program2"
ikinci_program.gelistirildigi_dil = "C"
ikinci_program.platform = "windows"

print(ikinci_program.program_ismi)
print(ikinci_program.gelistirildigi_dil)
print(ikinci_program.platform)