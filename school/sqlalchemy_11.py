# Создать две группы. Добавить в каждую по три студента.
from school.models import Group, Student, session
group_1 = Group("a1")
group_2 = Group("a2")
student_1 = Student("Alex",'Makarov', group=group_1)
student_2 = Student("Dmytry","Alexeev", group=group_1)
student_3 = Student("Sam","Dakson", group=group_1)
student_4 = Student("Sasha","Mix", group=group_2)
student_5 = Student("Shura","Max", group=group_2)
student_6 = Student("Dys","Daks", group=group_2)
session.add_all([group_1, group_2, student_1, student_2, student_3, student_4, student_5, student_6])
session.commit()