from sqlalchemy import String, Column, ForeignKey, Integer, Table
from sqlalchemy.orm import relationship
from .. import Base

class TeacherDb(Base):
    __tablename__ = "teachers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False)
    subject = Column(String(70), nullable=False)

    courses = relationship("CourseDb", back_populates="teachers")
