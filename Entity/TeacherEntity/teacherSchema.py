from pydantic import BaseModel

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