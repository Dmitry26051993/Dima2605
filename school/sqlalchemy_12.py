# Получить всех студентов и создать для каждого дневник.
from school.models import session, Student, Diary

students_all = session.query(Student).all()

arr = []
for student in students_all:
    avg_score = float(input(f'enter avg_score for student {student.firstname} - '))
    diary = Diary(avg_score, student)
    arr.append(diary)