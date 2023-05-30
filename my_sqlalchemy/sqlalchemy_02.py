# Создать файл sqlalchemy_02.py.
# Создать соединение к базе sa_test.db.
# Создать 5 книг с помощью sqlalchemy.
from sqlalchemy import create_engine, text
engine = create_engine('sqlite:///sa_test.db')
with engine.connect() as connection:
    insert_query = """
      INSERT INTO book (title, pages, author, price, release_year) values ('War', 100, 'Alexeev', 10, 2005),
      ('Evil', 50, 'Stalin', 25, 1995), ('Clean', 115, 'Barisov', 9, 2010), 
      ('World', 95, 'Gay', 20, 2001), ('Cinema', 60, 'Fredman', 15, 2009)"""
    query = text(insert_query)
    connection.execute(query)
    connection.commit()
