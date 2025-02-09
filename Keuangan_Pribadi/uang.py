class IsiDompet:
    def __init__(self, saldo):
        self.__saldo = saldo

    def pemasukkan (self, jumlah):
        if jumlah > 0:
            self.__saldo += jumlah
            print(f'[ Pemasukkan anda sebanyak : {jumlah}, sisa saldo: {self.__saldo} ]\n')
        else:
            print('[ pemasukkan harus lebih dari Rp.0 ]\n')

    def pengeluaran (self, jumlah):
        if jumlah > 0:
            self.__saldo -= jumlah
            print(f'[ Pengeluaran anda sebanyak : {jumlah}, sisa saldo: {self.__saldo} ]\n')
        else:
            print('[ pengeluaran harus lebih dari Rp.0 ]\n')

    def getSaldo (self):
        print(f'\n> sisa saldo anda : {self.__saldo}\n')

print('\nMANAJEMEN UANG PRIBADI')
print('--------------------------')
saldo = int(input('\nMasukkan uang anda: '))

dompet = IsiDompet(saldo)

print('''
1. pemasukkan
2. pengeluaran
3. cek saldo''')
pil = input ('Masukkan pilihan: ')

if pil == '1':
    jumlah = int(input('\nMasukkan jumlah pemasukkan: '))
    dompet.pemasukkan(jumlah)
elif pil == "2":
    jumlah = int(input('\nMasukkan jumlah pengeluaran: '))
    dompet.pengeluaran(jumlah)
elif pil == '3':
    dompet.getSaldo()
else:
    print('\nPilihan tidak tersedia')
    
