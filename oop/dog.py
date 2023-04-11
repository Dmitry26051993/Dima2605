# Создать файл dog.py.Создать пустой класс Dog. Создать два объекта класса Dog.
# Вывести их на экран. Добавить два метода в класс Dog: jump и run.
# Методы выводят на экран Jump! и Run! соответственно.
# Создать объект и вызвать у него все методы. Создать класс Dog.
# Класс имеет четыре атрибута: height, weight, name, age.
# Класс имеет три метода: jump, run, bark. Каждый метод выводит сообщение на экран.
# Создать объект класса Dog, вызвать все методы объекта и вывести на экран все его атрибуты.
# Добавить в класс Dog метод change_name.
# Метод принимает на вход новое имя и меняет атрибут имени у объекта.
# Создать один объект класса. Вывести имя. Вызвать метод change_name. Вывести имя.
# Добавить в метод инициализации новый приватный атрибут - master.
# Создать метод get_master(), который возвращает значение атрибута master.
# Добавить новый приватный атрибут адрес(по-умолчанию равен ‘Minsk’).
# Добавить getter и setter для адреса.


class Dog():
    pet = "angry"
    def __init__(self, name, height, weight, age, master, adres):
        self.name = name
        self.height = height
        self.weight = weight
        self.age = age
        self.__master = master
        self.__adres = adres

    def run(self):
        print("Run!")
    def jump(self):
        print("Jump!")
    def bark(self):
        print(f"bark from {self.name}")
    def change_name(self, new_name):
        self.name = new_name
    def get_master(self):
        return self.__master
    def set_master(self, master):
        self.__master = master

    def get_adres(self):
        return self.__adres
    def set_adres(self, adres):
        self.__adres = adres


dog_1 = Dog(name="Kira", height=120, weight=20, age=10, master="Dmitry", adres="Bryansk")
dog_2 = Dog(name="Misha", height=135, weight=30, age=11, master="Dmitry", adres="Bryansk")
print(dog_1.__dict__)
print(dog_2.__dict__)
dog_1.pet = "not angry"
dog_1.run()
dog_1.bark()
dog_2.jump()
dog_2.change_name("Julia")
print(dog_2._Dog__master)
print(dog_2.get_master())
print(dog_2.get_adres())
dog_2.set_adres("Kiev")
print(dog_2.get_adres())
dog_2.set_master("Victor")
print(dog_2.get_master())
print(dog_2.__dict__)
