#  Создать класс Book. Атрибуты: количество страниц, год издания, автор, цена.
#  Добавить валидацию в конструкторе на ввод корректных данных.
#  Создать иерархию ошибок.
#  Ошибки вызываются при попытке создания неправильного объекта.
#  Обработка происходит в пользовательском коде(в main).
class MyException(Exception):
    def __init__(self, message='problems'):
        super().__init__(message)

class MyExeptionIntMustBe(MyException):
    def __init__(self, message='pages and year'):
        super().__init__(message)


class MyExeptionStrMustBe(MyException):
    def __init__(self, message='author'):
        super().__init__(message)


class MyExeptionIntOrFloatMustBe(MyException):
    def __init__(self, message='price must be int or float'):
        super().__init__(message)


class Book:
    def __init__(self, pages: int, year: int, author: str, price: float or int):
        if not isinstance(pages, int) or not isinstance(year, int):
            raise MyExeptionIntMustBe
        if not isinstance(author, str):
            raise MyExeptionStrMustBe
        if not isinstance(price, (int, float)):
            raise MyExeptionIntOrFloatMustBe
        self.pages = pages
        self.year = year
        self.author = author
        self.price = price


def main():
    try:
        Book(15, 1993, 'ibncvbvc', 'hfgh')
    except MyException as err:
        print(f'Problem with - {err}, object was not create')
    else:
        print('object was created')
    finally:
        print('for create book input pages: int, year: '
              'int, author: str, price: float or int')

if __name__ == '__main__':
    main()
