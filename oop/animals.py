# Создать три класса: Dog, Cat, Parrot.
# Атрибуты каждого класса: name, age, master.
# Каждый класс содержит конструктор и методы: run, jump, birthday(увеличивает age на 1), sleep.
# Класс Parrot имеет дополнительный метод fly. Cat - meow, Dog - bark.
class Dog:
    def __init__(self, name, age, master):
        self.name = name
        self.__age = age
        self.master = master

    def run(self):
        print(f'run {self.name}')

    def jump(self, x):
        print(f'jump {x} metrov {self.name}')

    def birthday(self):
        self.__age += 1

    def sleep(self):
        print(f'run {self.name}')

    def bark(self):
        print(f'bark {self.name}')

class Cat:
    def __init__(self, name, age, master):
        self.name = name
        self.__age = age
        self.master = master

    def run(self):
        print(f'run {self.name}')

    def jump(self, x):
        print(f'jump {x} metrov {self.name}')

    def birthday(self):
        self.__age += 1

    def sleep(self):
        print(f'run {self.name}')

    def meow(self):
        print(f'meow {self.name}')

class Parrot:
    def __init__(self, name, age, master):
        self.name = name
        self.__age = age
        self.master = master

    def run(self):
        print(f'run {self.name}')

    def jump(self, x):
        print(f'jump {x} metrov {self.name}')

    def birthday(self):
        self.__age += 1

    def sleep(self):
        print(f'run {self.name}')

    def fly(self):
        print(f'fly {self.name}')

dog = Dog(name="Alis", age=5, master="Dmitry")
cat = Cat(name="Alex", age=12, master="Dmitro")
parrot = Parrot(name="Sonyx", age=1, master="Doom")
print(dog.__dict__)
dog.bark()
print(cat.__dict__)
cat.meow()
print(parrot.__dict__)
parrot.fly()