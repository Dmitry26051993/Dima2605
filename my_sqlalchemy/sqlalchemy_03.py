# Создать файл sqlalchemy_03.py.
# Написать программу: пользователь вводит год.
# Отобразить на экране те книги, год которых меньше введенного пользователем года.
# Если таких книг нет - вывести сообщение: Not found.
# Для проверки количества записей - привести результат запроса к списку и использовать функцию len()
from sqlalchemy import create_engine, text
def find_me_book():
    engine = create_engine('sqlite:///sa_test.db')
    with engine.connect() as connection:
        ago = int(input("Введите год издания книги: "))
        select_query_text = f"""select * from book where releace_year < {ago}"""
        query = text(select_query_text)
        data = list(connection.execute(query))
        print(data)
        if len(data):
            for book in data:
                print(book)
        else:
            print("Not found")


def main():
    find_me_book()


if __name__ == '__main__':
    main()