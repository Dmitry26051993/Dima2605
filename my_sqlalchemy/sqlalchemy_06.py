# Импортировать Book и сессию из модуля book.
# Создать 3 книги с помощью сессии.
from my_sqlalchemy.sqlalchemy_05 import users_table
from my_sqlalchemy.book import Book, session1
from sqlalchemy.orm import registry
mapper_reqistry = registry()
mapper_reqistry.map_imperatively(Book, users_table)
book1 = Book('Name', 100, 'Miles', 10, 1997)
book2 = Book('Sky', 120, 'Gym', 1, 2005)
book3 = Book('Her history', 115, 'Makarov', 15, 1991)
session1.add_all([book1, book2, book3])
session1.commit()


