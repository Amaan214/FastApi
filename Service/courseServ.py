from sqlalchemy.orm import Session
from . import courseSchema as schema
from . import courseModel as models
from .ServiceInterface.courseServInterf import courseServiceInterface
from ..Entity.StudentEntity.studentModel import StudentDb
from ..Entity.TeacherEntity.teacherModel import TeacherDb

class courseService(courseServiceInterface):

    def create_course(self, db: Session, crse: schema.CourseCreate):
        course = models.CourseDb(title=crse.title, code=crse.code)
        # If a teacher id is provided
        if crse.teacher_id:
            # then call get_teacher to fetch the teacher from db.
            teacher = db.query(TeacherDb).filter(TeacherDb.id == crse.teacher_id).first()
            # If found assign it to course.teachers
            if teacher:
                course.teachers = teacher
        db.add(course)
        db.commit()
        db.refresh(course)
        return course
    
    def get_course(self, db: Session, crse_id: int):
        return db.query(models.CourseDb).filter(models.CourseDb.id == crse_id).first()

    def get_all_courses(self, db: Session, skip: int=0, limit: int=100):
        return db.query(models.CourseDb).offset(skip).limit(limit).all()
    
        # courses
    # +----+---------+-------+------------+
    # | id | title   | code  | teacher_id |
    # +----+---------+-------+------------+
    # | 1  | Physics | P101  | 1          |
    # +----+---------+-------+------------+

    # adding student to the course
    def add_student_to_course(self, db: Session, std_id: int, crse_id: int):
        # fetch student and course from db
        student = db.query(StudentDb).filter(StudentDb.id == std_id).first()
        course_and_student = self.get_course(db, crse_id)
        # If either doesn't exist then return none
        if not student or not course_and_student:
            return None
        # checking if the students are already enrolled
        if student not in course_and_student.students:
            # this append is equivalent of INSERT
            course_and_student.students.append(student)
            db.add(course_and_student)
            db.commit()
            db.refresh(course_and_student)
        return course_and_student
    
    def remove_student_from_course(self, db: Session, std_id: int, crse_id: int):
        student = db.query(StudentDb).filter(StudentDb.id == std_id).first()
        course_and_student = self.get_course(db, crse_id)
        if not student or not course_and_student:
            return None
        if student in course_and_student:
            # this remove is equivalent of DELETE
            course_and_student.students.remove(student)
            db.add(course_and_student)
            db.commit()
            db.refresh(course_and_student)
        return course_and_student
    
        # student_course
    # +------------+-----------+
    # | student_id | course_id |
    # +------------+-----------+
    # | 1          | 1         |   (Amaan → Physics)
    # +------------+-----------+