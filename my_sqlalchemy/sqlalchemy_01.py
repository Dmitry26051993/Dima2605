# Создать таблицу Book с помощью sqlalchemy.
# Атрибуты: id(integer primary key), title(varchar),
# pages(int), author(varchar), price(float), release_year(int)
from sqlalchemy import create_engine, text
engine = create_engine('sqlite:///sa_test.db')
with engine.connect() as connection:
    create_table_query = """create table book (id integer primary key autoincrement, title varchar, pages int, author varchar, price float, releace_year int);"""
    query = text(create_table_query)
    connection.execute(query)