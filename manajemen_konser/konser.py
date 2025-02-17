class Konser:
    def __init__(self, nama, artis, jumlah, harga):
        self.namaKonser = nama
        self.artis = artis
        self.__totalTiket = jumlah
        self.__jumlahTiket = jumlah
        self.__hargaTiket = harga

    def get_totalTiket (self):
        return self.__totalTiket

    def get_jumlahTiket (self):
        return self.__jumlahTiket
    
    def get_hargaTiket (self):
        return self.__hargaTiket
    
    def set_hargaTiker (self, baru):
        self.__hargaTiket = baru

    def jualTiket (self, jumlah):
        self.__jumlahTiket -= jumlah
    
    def cekSoldOut (self):
        if self.__jumlahTiket == 0:
            print(f'[ Konser {self.namaKonser} sudah SOLD OUT ]\n')
        else:
            print(f'[ Konser {self.namaKonser} belum sold out (sisa tiket: {self.__jumlahTiket}) ]\n')

    def info_konser (self):
        print(f'''
-----
INFORMASI KONSER [{self.namaKonser}]
-----
Artis: {self.artis}
Total tiket: {self.get_totalTiket()}
Harga per tiker: Rp.{self.get_hargaTiket()}
Sisa tiket: {self.get_jumlahTiket()}
''')
        
enigma = Konser('enigma', 'adele, taylor, chappell', 100, 900000)
enigma.cekSoldOut()
enigma.jualTiket(70)
enigma.cekSoldOut()
enigma.info_konser()