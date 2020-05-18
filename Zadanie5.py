class Dog:
    count = 0  # this is a class variable
    dogs = []  # this is a class variable

    def __init__(self, name):
        self.name = name  # self.name is an instance variable
        Dog.count += 1
        Dog.dogs.append(name)

    def bark(self, n):  # this is an instance method
        print("{} says: {}".format(self.name, "woof! " * n))

    @staticmethod
    def show():
        a = Dog
        print(f"Ilość psów: {str(a.count)}")
        for i in range (a.count):
            print(str(a.dogs[i]))

dog1 = Dog("Max")
dog2 = Dog("Balto")
dog3 = Dog ("Reks")
dog = Dog
dog.show()