from sqlalchemy import Boolean, String, Column, ForeignKey, Integer, Table
from sqlalchemy.orm import relationship

from app.database import Base

# Establishing many-to-many relationship between student and course
student_course = Table(
    "student_course", Base.metadata,
    Column("student_id", Integer, ForeignKey("students.id", ondelete="CASCADE"), primary_key=True),
    Column("course_id", Integer, ForeignKey("courses.id", ondelete="CASCADE"), primary_key=True),
)


class StudentDb(Base):
    __tablename__ = "students"

    # Column names
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False)
    student_id = Column(Integer, nullable=False, unique=True)

    # Now we will establish One-to-Many relationship
    courses = relationship("CourseDb", secondary=student_course, back_populates="students")


class TeacherDb(Base):
    __tablename__ = "teachers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False)
    subject = Column(String(70), nullable=False)

    courses = relationship("CourseDb", back_populates="teachers")


class CourseDb(Base):
    __tablename__ = "courses"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(50), nullable=False)
    code = Column(String(50), nullable=False, unique=True)

    teacher_id = Column(Integer, ForeignKey("teachers.id"), nullable=True)

    students = relationship("StudentDb", secondary=student_course, back_populates="courses")

    teachers = relationship("TeacherDb", back_populates="courses")