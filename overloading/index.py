# Overloading = fungsi/method dengan nama yang sama namun implementasi/parameter bisa berbeda beda

class Calc:

    """
    CARA YANG SALAH:

    def tambah (self, a, b, c): #pake 3 parameter
        return a + b + c
    
    def tambah (self, a, b): #pake 2 parameter
        return a + b

    def tambah (self, a): #pake 1 parameter
        return a


    DI DALAM PYTHON TIDAK BISA DIPISAH PISAH BEGITU!
    LANGSUNGIN AJA!
    """

    def tambah(self, a=None,b=None,c=None):
        h = 0

        if a != None and b != None and c != None: # 3 parameter
            h = a + b + c
        elif a != None and b != None: # 2 parameter
            h = a + b
        else: # 1 parameter
            h = a

        return h

a = Calc()
print(f"[ {a.tambah(1,2)} ]")