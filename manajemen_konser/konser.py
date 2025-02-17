class Konser:
    def __init__(self, artis, jumlah, harga):
        self.namaKonser = 'ENIGMA'
        self.artis = artis
        self.__totalTiket = jumlah
        self.__jumlahTiket = jumlah
        self._hargaTiket = harga

    def get_totalTiket (self):
        return self.__totalTiket

    def get_jumlahTiket (self):
        return self.__jumlahTiket
    
    def get_hargaTiket (self):
        return self._hargaTiket
    
    def set_hargaTiker (self, baru):
        self._hargaTiket = baru

    def jualTiket (self, jumlah):
        self.__jumlahTiket -= jumlah
        print(f'[ Anda berhasil menjualkan tiket anda sebanyak {jumlah} tiket, sisa tiket {self.__jumlahTiket} ]')
    
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
Harga per tiket: Rp.{self.get_hargaTiket()}
Sisa tiket: {self.get_jumlahTiket()}
''')
        
print('\nWelcome to Konser ENIGMA')
artis = input('> Masukkan nama artis: ')
total_tiket = int(input('> Masukkan total tiket: '))
harga = int(input('> Masukkan harga per tiket: '))

konser = Konser(artis, total_tiket, harga)

while True : 
    print()
    print('''
1. Jual tiket
2. Informasi konser
3. Back''')
    pil = input('Masukkan pilihan: ')

    if pil == "1":
        jumlah = int(input('\nBerapa banyak tiket yang anda jual: '))
        konser.jualTiket(jumlah)
        print()

    elif pil == "2":
        konser.info_konser()
    elif pil == "3":
        pass
    else:
        print('Pilihan tidak valid')

        break