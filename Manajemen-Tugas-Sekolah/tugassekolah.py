from datetime import date, timedelta

class Task:
    def __init__(self, mapel, dl):
        self.mapel = mapel
        self.dl = dl
        self.status = 'Belum selesai'

    def mark_as_complete (self):
        self.status = "Sudah selesai"

    def check_deadline (self):
        HARI_INI = date.today()

        if self.dl < HARI_INI:
            return 'deadline nya udah kelewat ege LU TELAT'
        elif self.dl == HARI_INI:
            return 'DEADLINE SEKARANG, CEPET KUMPULIN WOY'
        else:
            sisa_hari = (self.dl - HARI_INI).days
            return f'tenang bro, tinggal {sisa_hari} hari lagi'
        
    def info(self):
        print(f'''
INFO TUGAS LEK
> Mapel : {self.mapel}
> Tanggal hari ini : {date.today()}
> Deadline : {self.dl}
> Status : {self.status}
[{self.check_deadline()}]
''')
        
# date(year, month, date)
tugas = Task ('Matematika', date(2025, 2, 1))

tugas.mark_as_complete()  
tugas.info()
