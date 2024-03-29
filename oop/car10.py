# Создать класс Car. Атрибуты: марка, модель, год  выпуска, скорость(по умолчанию 0).
# Методы: увеличить скорости(скорость + 5),
# уменьшение скорости(скорость  - 5),
# стоп(сброс скорости на 0),
# отображение скорости,
# разворот(изменение знака скорости).
# Все атрибуты приватные.
class Car:

    def __init__(self, brand, model, age, speed=0):
        self.__brand = brand
        self.__model = model
        self.__age = age
        self.__speed = speed

    def speed_plus(self, number=5):
        self.__speed += number

    def speed_minus(self, number=5):
        self.__speed -= number

    def stop(self):
        self.__speed = 0

    def show_speed(self):
        return self.__speed

    @property
    def speed(self):
        return self.__speed

    def change_speed(self):
        self.__speed = - self.__speed


car = Car("Lada", "granda", 2015)
car.speed_minus()
car.speed_plus()
car.speed_plus()
print(car.speed)