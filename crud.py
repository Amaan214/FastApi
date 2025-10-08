from sqlalchemy.orm import Session
from app import schema, models

def create_student(db: Session, std: schema.StudentCreate):
    student = models.StudentDb(name=std.name, student_id =std.student_id)
    db.add(student)
    db.commit()
    db.refresh(student)
    return student

# This will retrieve the student based on the database primary key
def get_student(db: Session, student_id: int):
    return db.query(models.StudentDb).filter(models.StudentDb.id == student_id).first()

# This will retrieve the student based on custom identifier i.e. roll number
def get_student_by_id(db: Session, roll_num: int):
    return db.query(models.StudentDb).filter(models.StudentDb.student_id == roll_num).first()

# This will retrieve all the students
def get_all_students(db: Session, skip: int=0, limit: int=100):
    return db.query(models.StudentDb).offset(skip).limit(limit).all()

# students
# +----+--------+------------+
# | id | name   | student_id |
# +----+--------+------------+
# | 1  | Amaan  | 101        |
# +----+--------+------------+



def create_teacher(db: Session, teach: schema.TeacherCreate):
    teacher = models.TeacherDb(name=teach.name, subject=teach.subject)
    db.add(teacher)
    db.commit()
    db.refresh(teacher)
    return teacher

def get_teacher(db: Session, teach_id: int):
    return db.query(models.TeacherDb).filter(models.TeacherDb.id == teach_id).first()

def get_all_teacher(db: Session, skip: int=0, limit: int=100):
    return db.query(models.TeacherDb).offset(skip).limit(limit).all()


# teachers
# +----+-------+---------+
# | id | name  | subject |
# +----+-------+---------+
# | 1  | John  | Math    |
# +----+-------+---------+


def create_course(db: Session, crse: schema.CourseCreate):
    course = models.CourseDb(title=crse.title, code=crse.code)
    # If a teacher id is provided
    if crse.teacher_id:
        # then call get_teacher to fetch the teacher from db.
        teacher = get_teacher(db, crse.teacher_id)
        # If found assign it to course.teachers
        if teacher:
            course.teachers = teacher
    db.add(course)
    db.commit()
    db.refresh(course)
    return course

# courses
# +----+---------+-------+------------+
# | id | title   | code  | teacher_id |
# +----+---------+-------+------------+
# | 1  | Physics | P101  | 1          |
# +----+---------+-------+------------+

def get_course(db: Session, crse_id: int):
    return db.query(models.CourseDb).filter(models.CourseDb.id == crse_id).first()

def get_all_courses(db: Session, skip: int=0, limit: int=100):
    return db.query(models.CourseDb).offset(skip).limit(limit).all()

# adding student to the course
def add_student_to_course(db: Session, std_id: int, crse_id: int):
    # fetch student and course from db
    student = get_student(db, std_id)
    course_and_student = get_course(db, crse_id)
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

# student_course
# +------------+-----------+
# | student_id | course_id |
# +------------+-----------+
# | 1          | 1         |   (Amaan → Physics)
# +------------+-----------+


def remove_student_from_course(db: Session, std_id: int, crse_id: int):
    student = get_student(db, std_id)
    course_and_student = get_course(db, crse_id)
    if not student or not course_and_student:
        return None
    if student in course_and_student:
        # this remove is equivalent of DELETE
        course_and_student.students.remove(student)
        db.add(course_and_student)
        db.commit()
        db.refresh(course_and_student)
    return course_and_student