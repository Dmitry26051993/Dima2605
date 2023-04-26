# Создать пять классов описывающие реальные объекты.
# Каждый класс должен содержать минимум три приватных атрибута,
# конструктор, геттеры и сеттеры для каждого атрибута, два метода.
class Dog:
    def __init__(self, name, ago, master):
        self.__name = name
        self.__ago = ago
        self.__master = master

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, n_name):
        self.__name = n_name

    @property
    def ago(self):
        return self.__ago

    @ago.setter
    def ago(self, n_ago):
        self.__ago = n_ago

    @property
    def master(self):
        return self.__master

    @master.setter
    def master(self, n_master):
        self.__master = n_master

    def run(self):
        print("Run!")

    def jump(self):
        print("Jump!")


class Cat:
    def __init__(self, name, ago, adres):
        self.__name = name
        self.__ago = ago
        self.__adres = adres

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def ago(self):
        return self.__ago

    @ago.setter
    def ago(self, n_ago):
        self.__ago = n_ago

    @property
    def adres(self):
        return self.__adres

    @adres.setter
    def adres(self, n_adres):
        self.__adres = n_adres

    def mouse(self):
        print("Mouse!")

    def jump(self):
        print("Jump!")

class Pat:
    def __init__(self, name, ago, master):
        self.__name = name
        self.__ago = ago
        self.__master = master

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, n_name):
        self.__name = n_name

    @property
    def ago(self):
        return self.__ago

    @ago.setter
    def ago(self, n_ago):
        self.__ago = n_ago

    @property
    def master(self):
        return self.__master

    @master.setter
    def master(self, n_master):
        self.__master = n_master

    def fly(self):
        print("Flu!")

    def jump(self):
        print("Jump!")

class Monkey:
    def __init__(self, name, ago, master):
        self.__name = name
        self.__ago = ago
        self.__master = master

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, n_name):
        self.__name = n_name

    @property
    def ago(self):
        return self.__ago

    @ago.setter
    def ago(self, n_ago):
        self.__ago = n_ago

    @property
    def master(self):
        return self.__master

    @master.setter
    def master(self, n_master):
        self.__master = n_master

    def Sleep(self):
        print("Sleep!")

    def jump(self):
        print("Jump!")

class Snake:
    def __init__(self, name, ago, master):
        self.__name = name
        self.__ago = ago
        self.__master = master

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, n_name):
        self.__name = n_name

    @property
    def ago(self):
        return self.__ago

    @ago.setter
    def ago(self, n_ago):
        self.__ago = n_ago

    @property
    def master(self):
        return self.__master

    @master.setter
    def master(self, n_master):
        self.__master = n_master

    def sleep(self):
        print("Sleep!")

    def crowl(self):
        print("Crowl!")

dog_1 = Dog(name="Bob", ago=5, master='Boris')
print(dog_1.__dict__)
dog_1.run()
dog_1.jump()
cat_1 = Cat(name="Alex", ago=5, adres='Minsk')
print(cat_1.__dict__)
cat_1.jump()
cat_1.mouse()
pet_1 = Pat(name="Kesha", ago=2, master='Sveta')
print(pet_1.__dict__)
pet_1.jump()
pet_1.fly()
monkey_1 = Monkey(name="Dmitry", ago=7, master='Filip')
print(monkey_1.__dict__)
monkey_1.jump()
monkey_1.Sleep()
snake_1 = Snake(name="Dmitro", ago=3, master='Fakir')
print(snake_1.__dict__)
snake_1.sleep()
snake_1.crowl()


