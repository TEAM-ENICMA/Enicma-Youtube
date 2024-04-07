class Programlar:

    def __init__(self, program_ismi, gelistirildigi_dil, platform):
        self.program_ismi = program_ismi
        self.gelistirildigi_dil = gelistirildigi_dil
        self.platform = platform

birinci_program = Programlar("program1", "python", "linux")
ikinci_program = Programlar("program2", "C", "windows")

print(birinci_program.gelistirildigi_dil)
print(ikinci_program.gelistirildigi_dil)


class Programlar:

    def __init__(self, program_ismi, gelistirildigi_dil, platform):
        self.program_ismi = program_ismi
        self.gelistirildigi_dil = gelistirildigi_dil
        self.platform = platform

    def detayli_bilgi(self):
        print("{}, {} dilinde, {} platformu icin gelistirilmis bir programdir.".format(self.program_ismi, self.gelistirildigi_dil, self.platform))

    def yeni_versiyon(self):
        if self.platform == "linux":
            print("Programin yeni versiyonu gelistirilecektir.")
        elif self.platform == "windows":
            print("Programin yeni versiyonu gelistirilmeyecektir.")
        else:
            print("Programin gelistirilip gelistirilmeyeceği bilinmiyor.")

birinci_program = Programlar("program1", "python", "linux")
ikinci_program = Programlar("program2", "C", "windows")

birinci_program.detayli_bilgi()
birinci_program.yeni_versiyon()

ikinci_program.detayli_bilgi()
ikinci_program.yeni_versiyon()


# kaynak = https://medium.com/rexven/python-ile-nesne-tabanl%C4%B1-programlama-object-oriented-programming-232134543e7f