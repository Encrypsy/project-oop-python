class Anggota:
    def __init__(self, nama, id_anggota, jenis):
        self.nama = nama
        self.id = id_anggota
        self.jenis = jenis
    
    def info(self):
        print(f'''
> Info Anggota Perpus 11
Nama : {self.nama}
Id : {self.id}
Jenis : {self.jenis}
''')
        
class Siswa(Anggota):
    def __init__(self, nama, id_anggota):
        super().__init__(nama, id_anggota, 'Mahasiswa')\
        
    def info(self):
        super().info()
        
class Guru(Anggota):
    def __init__(self, nama, id_anggota):
        super().__init__(nama, id_anggota, 'Mahasiswa')\
        
    def info(self):
        super().info()

class Umum(Anggota):
    def __init__(self, nama, id_anggota):
        super().__init__(nama, id_anggota, 'Mahasiswa')\
        
    def info(self):
        super().info()

malya = Siswa('malya', 'M1738')
buRini = Guru('Bu Rini', 'R1435')
karina = Umum('Karina', 'K3423')

daftarAnggota = [malya, buRini, karina]

for i in daftarAnggota:
    i.info()

