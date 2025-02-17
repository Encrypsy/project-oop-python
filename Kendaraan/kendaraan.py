class Kendaraan:
    def __init__(self, nama, merk, warna, kecepatan):
        self.nama = nama
        self.__merk = merk
        self._warna = warna
        self.__kecepatan = kecepatan

class Mobil(Kendaraan):
    def __init__(self, nama, merk, warna, kecepatan):
        super().__init__(nama, merk, warna, kecepatan)

    def get_Kecepatan(self):
        return self.__kecepatan

    