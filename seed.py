from connect_db import session
from models import Student, Group, Teacher, Subject, Marks
from datetime import datetime
from faker import Faker
import random
fake = Faker()

names = [fake.name() for _ in range(100)]

# Создаем три группы
group1 = Group(name='Group 1')
group2 = Group(name='Group 2')
group3 = Group(name='Group 3')
groups = [group1, group2, group3]
for group in groups:
    session.add(group)

# Создаем пять учителей
teachers = [Teacher(name=fake.name()) for _ in range(5)]
for teacher in teachers:
    session.add(teacher)

# Создаем 5 предметов студентов котрые относяться к каждому преподавателю
subject1 = Subject(name='Mathematics', teacher=teachers[0])
subject2 = Subject(name='English', teacher=teachers[1])
subject3 = Subject(name='Science', teacher=teachers[2])
subject4 = Subject(name='Literature', teacher=teachers[3])
subject5 = Subject(name='History', teacher=teachers[4])

subjects = [subject1, subject2, subject3, subject4, subject5]
for subject in subjects:
    session.add(subject)

# Создаем тридцать студентов и их оценки
for _ in range (30):
    student = Student(name=random.choice(names), group=random.choice(groups))
    session.add(student)

    for subject in subjects:
        marks = Marks(mark=random.randint(0, 5), student=student, subject=subject, date_received=datetime.now())
        session.add(marks)

session.commit()
