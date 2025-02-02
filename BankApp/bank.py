class Bank :

    saldo = 0

    def __init__(self, nama, aidi):
        self.nama = nama
        self.__id = aidi

    def withdraw(self, jumlah):
        Bank.saldo -= jumlah

    def deposit (self, jumlah):
        Bank.saldo += jumlah

    def get_id (self):
        return self.__id

    def info (self):
        print(f'''
Bank Account
----
Nama : {self.nama}
Id  : {self.get_id()}
Saldo : {Bank.saldo}
''')
        
akun1 = Bank('Neng AI', '103473')
akun1.deposit(1000000)
akun1.info()