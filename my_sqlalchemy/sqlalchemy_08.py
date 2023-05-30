# Написать программу: пользователь вводит границы фильтрации по году.
# Отобразить на экране те книги, год которых находится в заданных границах.
# Если таких книг нет - вывести сообщение: Not found.
from sqlalchemy import create_engine, and_
from sqlalchemy.orm import sessionmaker, registry
from my_sqlalchemy.book import Book
from my_sqlalchemy.sqlalchemy_05 import users_table

def filter_year(start, finish):
    engine = create_engine('sqlite:///book.db', echo=True)
    session = sessionmaker(bind=engine)()

    mapper_registry = registry()
    mapper_registry.map_imperatively(Book, users_table)
    result = session.query(Book).filter(and_(Book.release_year > start, Book.release_year < finish))
    return result
def filter_1(start):
    engine = create_engine('sqlite:///book.db', echo=True)
    session = sessionmaker(bind=engine)()
    mapper_registry = registry()
    mapper_registry.map_imperatively(Book, users_table)
    result = session.query(Book).filter(Book.release_year > start)
    return result
def filter_year(finish):
    engine = create_engine('sqlite:///book.db', echo=True)
    session = sessionmaker(bind=engine)()
    mapper_registry = registry()
    mapper_registry.map_imperatively(Book, users_table)
    result = session.query(Book).filter(Book.release_year < finish)
    return result


def main():
    start_year = int(input('Введите стартовый год: '))
    finish_year = int(input('Введите конечный год: '))
    result = list(filter_year(finish_year))
    if len(result) > 0:
        for book in result:
            print(book.title, book.price)
    else:
        print('Not found')


if __name__ == '__main__':
    main()