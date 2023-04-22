# Создать родительский класс Pet, содержащий все общие методы классов Dog, Cat, Parrot.
# Унаследовать Dog, Cat, Parrot от класса Pet.
# Удалить в дочерних классах те методы, которые имеются у родительского класса.
# Создать объект каждого класса и вызвать все его методы.
# Добавить два новых атрибута в родительский класс: weight и height.
# Добавить методы change_weight, change_height принимающий один параметр
# и прибавляющий его к соответствующему аргументу.
# В случае если параметр не был передан, увеличивать на 0.2.
# Изменить метод fly класса Parrot.
# Если вес больше 0.5 выводить сообщение This parrot cannot fly.
# Переопределить методы change_weight, change_height в классе Parrot.
# В случае непередачи параметра - вес изменяется на 0.05
# Добавить метод jump, принимающий высоту прыжка. Метод выводит сообщение “Jump X meters”
# Переопределить метод jump в дочерних классах.
# Если передать методу jump класса dog значение больше 0.5,
# выводить сообщение “Dogs cannot jump so high, аналогично для кошек(2), для попугаев(0.05)
# Добавить в класс Parrot  новый атрибут - species
# Добавить в класс Pet пустой метод voice.
# Заменить имена методов bark, meow на voice.
# Добавить voice для класса Parrot.
# Создать функцию, принимающую список животных и вызывающую у каждого животного метод voice.
# Определить магические методы сравнения для класса Pet:
# на равенство и неравенство. Два животных равны тогда,
# когда равны их возрасты, их рост и вес и класс.
import random
import string
from abc import ABC, abstractmethod
class Pet(ABC):
    __count = 0
    very_important = True
    def __init__(self, name, age, master, height, weight):
        self.name = name
        self.__age = age
        self.master = master
        self.weight = weight
        self.height = height
        Pet.__count += 1

    @staticmethod
    def get_random_name():
        result = random.choice(string.ascii_uppercase) + '-' + str(random.randint(1, 99))
        return result

    @classmethod
    def get_counter(cls):
        return cls.__count

    @staticmethod
    def go():
        print('go')


    def run(self):
        print(f'run {self.name}')

    def jump(self, x):
        print(f'jump {x} metrov {self.name}')

    def birthday(self):
        self.__age += 1

    def sleep(self):
        print(f'run {self.name}')

    def voice(self):
        pass

    def change_weight(self, arg=None):
        if arg:
            self.weight += arg
        else:
            self.weight += 0.2

    def change_height(self, arg=None):
        if arg:
            self.height += arg
        else:
            self.height += 0.2

    def __str__(self):
        return f'pet from class {self.__class__}- {self.name}'

    def __repr__(self):
        return f'repr for class {self.__class__}- {self.name}'

    def __eq__(self, other):
        return (self.name, self.__age, self.height, type(self)) == (other.name, other.__age, other.height, type(other))

    def __ne__(self, other):
        return (self.name, self.__age, self.height, type(self)) != (other.name, other.__age, other.height, type(other))

class Dog(Pet):

    def voice(self):
        print(f'bark {self.name}')

    def jump(self, x):
        if x > 0.5:
            print('Dogs cannot jump so high')
        else:
            super().jump(x)

class Cat(Pet):

    def voice(self):
        print(f'meow {self.name}')

    def jump(self, x):
        if x > 2:
            print('Cats cannot jump so high')
        else:
            super().jump(x)

class Parrot(Pet):
    def __init__(self, name, age, master, weight, height, species):
        super().__init__(name, age, master, weight, height)
        self.species = species

    def fly(self):
        if self.weight > 0.5:
            print(f"this parrot {self.name} cannot fly")
        else:
            print(f'fly {self.name}')

    def change_weight(self, arg=None):
        if arg:
            self.weight += arg
        else:
            self.weight += 0.05

    def jump(self, x):
        if x > 0.05:
            print('Parrot cannot jump so high')
        else:
            super().jump(x)

    def voice(self):
        print(f'sing {self.name}')
class Horse(Pet):

    def voice(self):
        print(f'{self.name} horse voice')

class Donkey(Pet):

    def voice(self):
        print(f'{self.name} donkey voice')

class Mule(Donkey, Horse):
    pass

dog = Dog(name="Alis", age=5, master="Dmitry",height=10, weight=4)
cat = Cat(name="Alex", age=12, master="Dmitro", height=15, weight=6)
parrot = Parrot(name="Sonyx", age=1, master="Doom", height=1, weight=0.6, species="ara")
print(dog.__dict__)
dog.jump(5)
print(cat.__dict__)
print(parrot.__dict__)
parrot.fly()
parrot.change_weight()
print(parrot.__dict__)
parrot.jump(1)
cat.voice()
dog.voice()
parrot.voice()

print(Pet.get_counter())
print(Pet.get_random_name())
print(Pet.get_random_name())

