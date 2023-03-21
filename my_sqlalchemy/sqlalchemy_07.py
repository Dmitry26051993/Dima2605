# Получить все книги и вывести их на экран в формате год - название - автор
from sqlalchemy import create_engine
from my_sqlalchemy.book import Book
from sqlalchemy.orm import sessionmaker, mapper, registry
from my_sqlalchemy.sqlalchemy_05 import users_table
engine1 = create_engine('sqlite:///book.db', echo=True)
Ssesion = sessionmaker(bind=engine1)
ssesion2 = Ssesion()
mapper_registry = registry()
mapper_registry.map_imperatively(Book, users_table)
data = ssesion2.query(Book)
print(data)
for book in data:
    print(data)
    print(book.id, book.release_year, book.author)


