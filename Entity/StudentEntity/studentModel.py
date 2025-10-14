from sqlalchemy import String, Column, ForeignKey, Integer, Table
from sqlalchemy.orm import relationship
from .. import Base

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