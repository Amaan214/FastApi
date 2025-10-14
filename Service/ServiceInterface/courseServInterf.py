from abc import ABC, abstractmethod
from sqlalchemy.orm import Session
from . import courseSchema as schema

class courseServiceInterface(ABC):
    
    @abstractmethod
    def create_course(self, db: Session, crse: schema.CourseCreate):
        pass

    @abstractmethod
    def get_course(self, db: Session, crse_id: int):
        pass

    @abstractmethod
    def get_all_courses(self, db: Session, skip: int=0, limit: int=100):
        pass

    @abstractmethod
    # adding student to the course
    def add_student_to_course(self, db: Session, std_id: int, crse_id: int):
        pass

    @abstractmethod
    def remove_student_from_course(self, db: Session, std_id: int, crse_id: int):
        pass