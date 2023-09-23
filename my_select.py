from sqlalchemy import select, func

from connect_db import session
from models import Group, Student, Teacher, Subject, Marks


def select_1():
    subquery = (
        session.query(Marks.student_id, func.avg(Marks.mark).label('avg_mark')).group_by(Marks.student_id).subquery())

    top_students = (
        session.query(Student, subquery.c.avg_mark).join(subquery, Student.id == subquery.c.student_id)
        .order_by(subquery.c.avg_mark.desc()).limit(5).all())

    for student, avg_mark in top_students:
        print(f"Student: {student.name}, Average Mark: {avg_mark:}")


def select_2():
    subject_name = input('Subject:')
    top_student = (
        session.query(Student)
        .join(Marks, Student.id == Marks.student_id)
        .join(Subject, Marks.subject_id == Subject.id)
        .filter(Subject.name == subject_name)
        .group_by(Student.id)
        .order_by(func.avg(Marks.mark).desc())
        .first()
    )
    print(f"Top Student for {subject_name}: {top_student.name}")


def select_3():
    subject_name = input('Subject:')
    group_avg_query = (
        session.query(Group.id, func.avg(Marks.mark).label('average_mark'))
        .join(Student, Student.group_id == Group.id)
        .join(Marks, Marks.student_id == Student.id)
        .join(Subject, Subject.id == Marks.subject_id)
        .filter(Subject.name == subject_name)
        .group_by(Group.id)
    )
    group_avg_results = group_avg_query.all()
    for group_number, average_mark in group_avg_results:
        print(f"Group {group_number}: Average Mark for {subject_name}: {average_mark:.2f}")


def select_4():
    average_mark = (
        session.query(func.avg(Marks.mark).label('average_mark'))
    ).scalar()
    print(f"Average Mark on the Stream: {average_mark:.2f}")


def select_5():
    teacher_name = input('Enter name of teacher: ')
    courses_taught_by_teacher = (
        session.query(Subject.name)
        .join(Teacher, Teacher.id == Subject.teacher_id)
        .filter(Teacher.name == teacher_name)
        .all()
    )
    if courses_taught_by_teacher:
        print(f"Courses taught by {teacher_name}:")
        for course in courses_taught_by_teacher:
            print(course[0])
    else:
        print(f"No courses found for {teacher_name}")


def select_6():
    group_id = input('Write group:')
    students_in_group = (
        session.query(Student)
        .join(Group, Student.group_id == Group.id)
        .filter(Group.id == group_id)
        .all()
    )

    if students_in_group:
        print(f"Students in Group {group_id}:")
        for student in students_in_group:
            print(student.name)


def select_7():
    group_id = input('Write group:')
    subject_name = input('Subject:')
    marks_for_group_and_subject = (
        session.query(Marks)
        .join(Student, Student.id == Marks.student_id)
        .join(Subject, Subject.id == Marks.subject_id)
        .join(Group, Student.group_id == Group.id)
        .filter(Group.id == group_id, Subject.name == subject_name)
        .all()
    )
    if marks_for_group_and_subject:
        print(f"Marks for {subject_name} in Group {group_id}:")
        for mark in marks_for_group_and_subject:
            print(f"Student: {mark.student.name}, Mark: {mark.mark}")


def select_8():
    teacher_name = input('Enter name of teacher: ')
    average_mark_by_teacher = (
        session.query(func.avg(Marks.mark).label('average_mark'))
        .join(Subject, Subject.id == Marks.subject_id)
        .join(Teacher, Teacher.id == Subject.teacher_id)
        .filter(Teacher.name == teacher_name)
        .scalar()
    )
    if average_mark_by_teacher is not None:
        print(f"Average Mark given by {teacher_name} for his subjects: {average_mark_by_teacher:.2f}")
    else:
        print(f"No data found for {teacher_name}")


def select_9():
    student_id = input('Select student: ')
    courses_attended_by_student = (
        session.query(Subject.name)
        .join(Marks, Subject.id == Marks.subject_id)
        .join(Student, Student.id == Marks.student_id)
        .filter(Student.id == student_id)
        .distinct()
        .all()
    )
    if courses_attended_by_student:
        print(f"Courses attended by {student_id}:")
        for course in courses_attended_by_student:
            print(course[0])


def select_10():
    student_id = input('Select student: ')
    teacher_name = input('Enter name of teacher: ')
    courses_attended_by_student_and_taught_by_teacher = (
        session.query(Subject.name)
        .join(Marks, Subject.id == Marks.subject_id)
        .join(Student, Student.id == Marks.student_id)
        .join(Teacher, Teacher.id == Subject.teacher_id)
        .filter(Student.id == student_id, Teacher.name == teacher_name)
        .distinct()
        .all()
    )

    if courses_attended_by_student_and_taught_by_teacher:
        print(f"Courses attended by {student_id} and taught by {teacher_name}:")
        for course in courses_attended_by_student_and_taught_by_teacher:
            print(course[0])


if __name__ == '__main__':
    while True:
        command = input('Enter command: ')
        if command == '1':
            select_1()
        elif command == '2':
            select_2()
        elif command == '3':
            select_3()
        elif command == '4':
            select_4()
        elif command == '5':
            select_5()
        elif command == '6':
            select_6()
        elif command == '7':
            select_7()
        elif command == '8':
            select_8()
        elif command == '9':
            select_9()
        elif command == "10":
            select_10()
        else:
            print("Wrong command!")
            break
