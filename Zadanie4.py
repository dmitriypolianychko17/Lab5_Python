class Liczba:
    def __init__(self, liczba):
        self.liczba = liczba
    def __add__(self, other):
        return Liczba(self.liczba*self.liczba+2*self.liczba*other.liczba+other.liczba)

    def toStr(self):
        return self.liczba

x = Liczba(5)
y = Liczba(3)
result = x + y
print(result.toStr())

