from sqlalchemy.orm import Session
from . import studentSchema as schema
from . import studentModel as models
from .ServiceInterface.studentServiceInterf import studentServiceInterface

class studentService(studentServiceInterface):

    def create_student(self, db: Session, std: schema.StudentCreate):
        student = models.StudentDb(name=std.name, student_id =std.student_id)
        db.add(student)
        db.commit()
        db.refresh(student)
        return student
    

        # This will retrieve the student based on the database primary key
    def get_student(self, db: Session, student_id: int):
        return db.query(models.StudentDb).filter(models.StudentDb.id == student_id).first()

    # This will retrieve the student based on custom identifier i.e. roll number
    def get_student_by_id(self, db: Session, roll_num: int):
        return db.query(models.StudentDb).filter(models.StudentDb.student_id == roll_num).first()

    # This will retrieve all the students
    def get_all_students(self, db: Session, skip: int=0, limit: int=100):
        return db.query(models.StudentDb).offset(skip).limit(limit).all()

    # students
    # +----+--------+------------+
    # | id | name   | student_id |
    # +----+--------+------------+
    # | 1  | Amaan  | 101        |
    # +----+--------+------------+