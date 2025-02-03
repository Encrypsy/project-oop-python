class Film:
    def __init__(self, pelanggan, judul, kapasitas):
        self.pelanggan = pelanggan
        self.judul = judul
        self.kapasitas = kapasitas

    def cek_ketersediaan (self):
        print(f"\n> Tersedia untuk {self.judul} : {self.kapasitas} kursi\n")

    def pesan_tiket(self, jumlah_tiket):
            if self.kapasitas >= jumlah_tiket:
                self.kapasitas -= jumlah_tiket
                print(f'\n> Film {self.judul} sudah dipesan sebanyak {jumlah_tiket} tiket\n')

            else:
                print(f'\n[Kapasitas kursi sudah penuh]\n')

    def info (self):
         print(f'''
Info Reservasi
----------------
Nama: {self.pelanggan}
Judul yang dipesan: {self.judul}
Kapasitas kursi: {self.kapasitas}
''')

malya = Film('Malya', 'Twilight', 50)
malya.pesan_tiket(3)
malya.cek_ketersediaan()




    
        

