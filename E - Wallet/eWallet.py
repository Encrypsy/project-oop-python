from abc import ABC, abstractmethod

class Pembayaran:
    def __init__(self, nama, total, pembayaran):
        self.nama = nama
        self.total = total
        self.pembayaran = pembayaran

    def bayar():
        pass

class Kartu_Kredit(Pembayaran):
    def __init__(self, nama, total, noKartu):
        super().__init__(nama, total, 'Kartu Kredit')
        self.noKartu = noKartu

    def bayar(self):
        print(f'> Berhasil melakukan transaksi sebesar Rp.{self.total} dengan no. Kartu ({self.noKartu})')

class eWallet (Pembayaran):
    def __init__(self, nama, total, pembayaran, noTelp, biaya_admin):
        super().__init__(nama, total, pembayaran)
        self.noTelp = noTelp
        self.biaya_admin = biaya_admin

    def bayar(self):
        print (f'''
[ Transaksi {self.pembayaran} berhasil !! ]
No. Telp : {self.noTelp}
Total yang ingin di tf : Rp.{self.total} 
Biaya Admin : {self.biaya_admin}%''')

class Gopay (eWallet):
    def __init__(self, nama, total, noTelp):
        super().__init__(nama, total, 'Gopay', noTelp, 5)
    
    def bayar(self):
        super().bayar()
        biaya_admin = self.biaya_admin / 100
        total_transaksi = self.total + (self.total * biaya_admin)
        print(f'Total : Rp.{total_transaksi}\n')

class Dana (eWallet):
    def __init__(self, nama, total, noTelp):
        super().__init__(nama, total, 'Dana', noTelp, 2)
    
    def bayar(self):
        super().bayar()
        biaya_admin = self.biaya_admin / 100
        total_transaksi = self.total + (self.total * biaya_admin)
        print(f'Total : Rp.{total_transaksi}\n')

class Ovo (eWallet):
    def __init__(self, nama, total, noTelp):
        super().__init__(nama, total, 'Ovo', noTelp, 8)
    
    def bayar(self):
        super().bayar()
        biaya_admin = self.biaya_admin / 100
        total_transaksi = self.total + (self.total * biaya_admin)
        print(f'Total : Rp.{total_transaksi}\n')

user = Gopay('Malya', 50000, 6285142399278)
user1 = Ovo('Mustika', 40000, 62832742374)
user2 = Dana('Khumaira', 100000, 6256347563475697)

daftar = [user, user1, user2]

for i in daftar:
    i.bayar()




    

