from abc import ABC, abstractmethod
from sqlalchemy.orm import Session
from . import teacherSchema as schema

class teacherServiceInterface(ABC):

    @abstractmethod
    def create_teacher(self, db: Session, teach: schema.TeacherCreate):
        pass

    @abstractmethod
    def get_teacher(self, db: Session, teach_id: int):
        pass

    @abstractmethod
    def get_all_teacher(self, db: Session, skip: int=0, limit: int=100):
        pass
    