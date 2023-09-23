from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


# Таблица групп
class Group(Base):
    __tablename__ = 'groups'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    student = relationship('Student', back_populates='group')


# Таблица студентов с указанием группы
class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    group_id = Column(Integer, ForeignKey('groups.id'))
    group = relationship('Group', back_populates='student')
    marks = relationship('Marks', back_populates='student')


# Таблица преподавателей
class Teacher(Base):
    __tablename__ = 'teachers'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    subject = relationship('Subject', back_populates='teacher')


# Таблица предметов с указанием преподавателя
class Subject(Base):
    __tablename__ = 'subjects'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    teacher_id = Column(Integer, ForeignKey('teachers.id'))
    teacher = relationship('Teacher', back_populates='subject')
    marks = relationship('Marks', back_populates='subject')


# Таблица с оценками по предметам с указанием когда оценка получена
class Marks(Base):
    __tablename__ = 'marks'
    id = Column(Integer, primary_key=True)
    mark = Column(Float)
    student_id = Column(Integer, ForeignKey('students.id'))
    subject_id = Column(Integer, ForeignKey('subjects.id'))
    date_received = Column(DateTime)
    student = relationship('Student', back_populates='marks')
    subject = relationship('Subject', back_populates='marks')
