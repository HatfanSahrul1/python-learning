class SimpleMath:
    def __init__(self):
        pass

    def Jumlah(self, a, b):
        return a + b
    
    def Kurang(self, a, b):
        return a - b
    
    def Selisih(self, a, b):
        return abs(a-b)
    
    def Kali(self, a, b):
        return a * b
    
    def Bagi(self, a, b):
        return 0 if b==0 else a / b
    

def main():
    math = SimpleMath()
    
    bil1 = 10
    bil2 = 27

    hasil = math.Jumlah(bil1, bil2)

    print(hasil)

    return 0



if __name__ == '__main__':
    main()    