# Pydantic is a data validation library in python
from pydantic import BaseModel
from typing import List, Optional

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

    class Config:
        orm_mode = True

# Teacher
class TeacherBase(BaseModel):
    name: str
    subject: str

class TeacherCreate(TeacherBase):
    pass

class TeacherRead(TeacherBase):
    id: int

    class Config:
        orm_mode = True


# Courses
class CourseBase(BaseModel):
    title: str
    code: str

class CourseCreate(CourseBase):
    teacher_id:  Optional[int] = None

class CourseRead(CourseBase):
    id: int
    teachers: Optional[TeacherRead] = None
    students: List[StudentRead] = []

    class Config:
        orm_mode = True

class CourseList(CourseBase):
    id: int
    class Config:
        orm_mode = True

StudentRead.model_rebuild()