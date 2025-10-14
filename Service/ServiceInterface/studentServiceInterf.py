# ABC module helps define abstract base class
from abc import ABC, abstractmethod
from sqlalchemy.orm import Session
from . import studentSchema as schema

class studentServiceInterface(ABC):
    
    @abstractmethod
    def create_student(self, db: Session, std: schema.StudentCreate):
        pass

    @abstractmethod
    # This will retrieve the student based on the database primary key
    def get_student(self, db: Session, student_id: int):
        pass

    @abstractmethod
    # This will retrieve the student based on custom identifier i.e. roll number
    def get_student_by_id(self, db: Session, roll_num: int):
        pass

    @abstractmethod
    # This will retrieve all the students
    def get_all_students(self, db: Session, skip: int=0, limit: int=100):
        pass