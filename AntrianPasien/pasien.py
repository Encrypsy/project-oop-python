class Pasien:
    def __init__(self, nama, no, penyakit):
        self.nama = nama
        self.__noTelp = no
        self.__riwayatPenyakit = penyakit

    def set_noTelp (self, baru):
        self.__noTelp = baru
    
    def set_riwayatPenyakit (self, baru):
        self.__riwayatPenyakit = baru

    def info (self):
        print(f'''
________________
Informasi Pasien
              
Nama : {self.nama}
No. Telp : {self.__noTelp}
Riwayat Penyakit : {self.__riwayatPenyakit}
''')

print('\nRUMAH SAKIT MITRA KASIH\n-------')
nama = input('Masukkan nama pasien: ')
no = input('Masukkan nomor telepon: ')
riwayat = input('Masukkan riwayat penyakit: ')

pasien1 = Pasien(nama, no, riwayat)
pasien1.info()
