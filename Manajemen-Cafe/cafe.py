from abc import ABC, abstractmethod

class Order(ABC):
    def __init__(self, nama, menu, jumlah, harga):
        self.nama = nama
        self.menu = menu
        self.jumlah = jumlah
        self.harga = harga

    @abstractmethod
    def calculate_price (self):
        pass

    def order_info (self):
        print(f'''
\nOrderan atas nama [{self.nama}]
Memesan : {self.menu} ({self.jumlah})
Total Harga : {self.calculate_price()}''')

class DineIn (Order):
    def __init__(self, nama, menu, jumlah, harga, noMeja):
        super().__init__(nama, menu, jumlah, harga)
        self.noMeja = noMeja

    def calculate_price (self):
        diskon = 10 / 100
        return self.harga - (self.harga * diskon)

    def order_info(self):
        super().order_info()
        print(f'No. meja : {self.noMeja}')
        print(f'< Mendapatkan diskon sebesar 10% >\n')

class TakeAway (Order):
    def __init__(self, nama, menu, jumlah, harga):
        super().__init__(nama, menu, jumlah, harga)

    def calculate_price(self):
        packaging_fee = 2000
        return self.harga + packaging_fee
    
    def order_info(self):
        super().order_info()

orderan1 = DineIn('Malya', 'Kopi Susu', 2, 3000, 10)
orderan1.order_info()
    