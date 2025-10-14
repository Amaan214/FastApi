from sqlalchemy import String, Column, ForeignKey, Integer, Table
from sqlalchemy.orm import relationship
from .. import Base
from ..StudentEntity.studentModel import student_course

class CourseDb(Base):
    __tablename__ = "courses"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(50), nullable=False)
    code = Column(String(50), nullable=False, unique=True)

    teacher_id = Column(Integer, ForeignKey("teachers.id"), nullable=True)

    students = relationship("StudentDb", secondary=student_course, back_populates="courses")

    teachers = relationship("TeacherDb", back_populates="courses")