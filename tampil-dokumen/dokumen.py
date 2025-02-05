class Dokumen:
    def tampilkan(self):
        pass

class PDF (Dokumen):
    def tampilkan(self):
        print(f'> Menampilkan dokumen dalam format PDF')

class Word (Dokumen):
    def tampilkan(self):
        print(f'> Menampilkan dokumen dalam format Word')

class TXT (Dokumen):
    def tampilkan(self):
        print(f'> Menampilkan dokumen dalam format TXT')

filee = PDF()
filee1 = Word()
filee2 = TXT()

daftar_file = [filee, filee1, filee2]

for i in daftar_file:
    i.tampilkan()