# Создать файл sqlalchemy_04.py.
# Написать программу: пользователь вводит данные о книге.
# Пользователю отображается введенная им информация.
# Пользователю задается вопрос: “Хотите сохранить эту книгу?”.
# Если ответ да - выполнить метод .commit(), иначе - .rollback()
from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError
engine = create_engine('sqlite:///sa_test.db')
with engine.connect() as connection:
    transaction = connection.begin()
    try:
        create_table_query = """create table book (id integer primary key autoincrement, title varchar, pages int, author varchar, price float, releace_year int);"""
        ddl = text(create_table_query)
        connection.execute(ddl)
        transaction.commit()
    except SQLAlchemyError as e:
        transaction.rollback()
        print(f"Ошибка при выполнении SQL-запроса: {str(e)}")