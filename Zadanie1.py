class Student:
    def __init__(self, imie, nr_albumu):
        self.imie = imie
        self.nr_albumu = nr_albumu

student1 = Student ("Dmytro", 110111)
student2 = Student ("Własysław", 110112)
student3 = Student ("Karol", 110113)
print(student1.imie)
print(student2.imie)
print(student3.imie)