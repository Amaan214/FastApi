from sqlalchemy.orm import Session
from . import teacherSchema as schema
from . import teacherModel as models
from .ServiceInterface.teacherServInterf import teacherServiceInterface

class teacherService(teacherServiceInterface):

    def create_teacher(self, db: Session, teach: schema.TeacherCreate):
        teacher = models.TeacherDb(name=teach.name, subject=teach.subject)
        db.add(teacher)
        db.commit()
        db.refresh(teacher)
        return teacher

    def get_teacher(self, db: Session, teach_id: int):
        return db.query(models.TeacherDb).filter(models.TeacherDb.id == teach_id).first()

    def get_all_teacher(self, db: Session, skip: int=0, limit: int=100):
        return db.query(models.TeacherDb).offset(skip).limit(limit).all()


    # teachers
    # +----+-------+---------+
    # | id | name  | subject |
    # +----+-------+---------+
    # | 1  | John  | Math    |
    # +----+-------+---------+