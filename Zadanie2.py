class Osoba:
    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko

class Student(Osoba):
    def __init__(self, imie, nazwisko, nr_albumu):
        Osoba.__init__(self, imie, nazwisko)
        self.nr_albumu = nr_albumu

osoba1 = Osoba("Dmytro", "Polianychko")
student1 = Student ("Dmytro", "Polianychko", 110111)
osoba2 = Osoba("Karol", "Lech")
student2 = Student ("Karol", "Lech", 110112)
osoba3 = Osoba ("Philip", "Papiernik")
student3 = Student ("Philip", "Papiernik", 110113)
print(f"Imie: {osoba1.imie}, nazwisko: {osoba1.nazwisko}")
print(f"Imie: {student1.imie}, nazwisko: {student1.nazwisko}, numer albumu: {student1.nr_albumu}")
