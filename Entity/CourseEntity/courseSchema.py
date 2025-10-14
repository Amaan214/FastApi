from pydantic import BaseModel
from typing import List, TYPE_CHECKING, Optional

if TYPE_CHECKING:
    from ..StudentEntity.studentSchema import StudentRead
    from ..TeacherEntity.teacherSchema import TeacherRead

# Courses
class CourseBase(BaseModel):
    title: str
    code: str

class CourseCreate(CourseBase):
    teacher_id:  Optional[int] = None

class CourseRead(CourseBase):
    id: int
    teachers: Optional["TeacherRead"] = None
    students: List["StudentRead"] = []

    class Config:
        orm_mode = True

class CourseList(CourseBase):
    id: int
    class Config:
        orm_mode = True