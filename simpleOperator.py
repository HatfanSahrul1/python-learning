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
        # ternary operation here
        return 0 if b==0 else a / b
    
    def Tukar(self, a, b):
        a, b = b, a
        return a, b
    
    def BubbleSort(self, arr):
        for x in range(0, len(arr)):
            for y in range(x+1, len(arr)):
                if arr[x] > arr[y] :
                    arr[x], arr[y] = self.Tukar(arr[x], arr[y])
        
        return arr