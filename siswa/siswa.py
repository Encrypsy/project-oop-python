class Siswa:
    def __init__(self, nama, kelas, no):
        self.nama = nama
        self.kelas = kelas
        self.no = no

    def informasi (self):
        print(f'''
[ Informasi Siswa ]
Nama : {self.nama}
Kelas : {self.kelas}
No. Absen : {self.no}
''')
        
print('''
DATA SISWA
''')
nama = input('> Masukkan nama: ')
kelas = input('> Masukkan kelas: ')
no = input('> Masukkan nomor absen: ')

siswa1 = Siswa(nama, kelas, no) 
siswa1.informasi()
