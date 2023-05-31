# Создать 5 книг.
# Получить всех студентов и добавить каждому студенту эти пять книг.
from school.models import session, Book, Student

arr = [
    Book('War', 33),
    Book('Colt', 500),
    Book('Obitel', 300),
    Book('Math', 100),
    Book('Sky', 30)
]

session.add_all(arr)
session.commit()
students_all = session.query(Student).all()
books_all = session.query(Book).all()

for book in books_all:
    book.students = students_all

session.commit()
