class Student:
    def __init__(self, imie, nazwisko, nr_albumu):
        self.imie = imie
        self.nazwisko = nazwisko
        self.nr_albumu = nr_albumu
    def show(self):
        print(f"Cześć nazywam się {self.imie} {self.nazwisko} i mój numer albumu to {self.nr_albumu}")
student1 = Student ("Dmytro","Polianychko", 110111)
student1.show()