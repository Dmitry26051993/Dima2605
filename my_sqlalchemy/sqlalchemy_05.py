# Создать файл book.py.
# Создать базу book.db.
# Создать таблицу Book с помощью механизма описания таблиц sqlalchemy.
# Атрибуты: id(integer primary key), title(varchar), pages(int), author(varchar), price(float), release_year(int)
from sqlalchemy import create_engine
from sqlalchemy import Table, Column, INTEGER, VARCHAR, FLOAT, MetaData
engine = create_engine('sqlite:///book.db', echo=True)
metadata = MetaData()
users_table = Table('Book', metadata,
                    Column('id', INTEGER, primary_key=True),
                    Column('title', VARCHAR),
                    Column('pages', INTEGER),
                    Column('author', VARCHAR),
                    Column('price', FLOAT),
                    Column('release_year', INTEGER),)
metadata.create_all(engine)
