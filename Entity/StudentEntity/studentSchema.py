# Pydantic is a data validation library in python
from pydantic import BaseModel
from typing import List
from ..CourseEntity.courseSchema import CourseList

# Student
class StudentBase(BaseModel):
    name: str
    student_id: int

# Creating new student
class StudentCreate(StudentBase):
    pass

class StudentRead(StudentBase):
    id: int
    # it means if it is empty then return empty list
    courses: List["CourseList"] = []

    class Config:  # allows reading SQLAlchemy objects as pydantic models
        orm_mode = True
