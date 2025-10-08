from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app import crud, models, schema
from app.database import SessionLocal, engine, Base

# This command creates all database tables that are defined in your SQLAlchemy models.
models.Base.metadata.create_all(bind=engine)

app=FastAPI()

# dependency
def get_db():
    db=SessionLocal()
    try: 
        yield db
    finally:
        db.close()

# Root
@app.get("/")
def root():
    return {"msg": "Class Project Api"}

# students
@app.post("/students/", response_model=schema.StudentRead)
def create_student(std: schema.StudentCreate, db: Session=Depends(get_db)):
    existing = crud.get_student_by_id(db, std.student_id)
    if existing:
        raise HTTPException(status_code=400, detail="Student already already registered with this id")
    return crud.create_student(db, std)

@app.get("/students/{student_id}", response_model=schema.StudentRead)
def read_student(student_id: int, db:Session=Depends(get_db)):
    student = crud.get_student_by_id(db, student_id)
    if not student:
        raise HTTPException(status_code=404, detail="No such id exists")
    return student

@app.get("/students/", response_model=list[schema.StudentRead])
def get_student_list(skip: int=0, limit: int=100, db: Session=Depends(get_db)):
    return crud.get_all_students(db, skip, limit)

# Teacher
@app.post("/teachers/", response_model=schema.TeacherRead)
def create_teacher(teach: schema.TeacherCreate, db: Session=Depends(get_db)):
    return crud.create_teacher(db, teach)

@app.get("/teachers/", response_model=list[schema.TeacherRead])
def get_teacher_list(skip: int=0, limit: int=100, db:Session=Depends(get_db)):
    return crud.get_all_teacher(db, skip, limit)

# Course
@app.post("/course/", response_model=schema.CourseRead)
def create_course(course: schema.CourseCreate, db: Session=Depends(get_db)):
    return crud.create_course(db, course)

@app.get("/course/", response_model=list[schema.CourseRead])
def get_all_courses(skip: int=0, limit: int=100, db: Session=Depends(get_db)):
    return crud.get_all_courses(db, skip, limit)

# Adding student to the course
@app.post("/course/{course_id}/addStudent/{student_id}", response_model=schema.CourseRead)
def enroll_student(course_id: int, student_id: int, db: Session=Depends(get_db)):
    course = crud.add_student_to_course(db, student_id, course_id)
    if not course:
        raise HTTPException(status_code=404, detail="No course found")
    return course

@app.post("/course/{course_id}/deleteStudent/{student_id}", response_model=schema.CourseRead)
def unenroll_student(course_id: int, student_id: int, db: Session=Depends(get_db)):
    course = crud.remove_student_from_course(db, student_id, course_id)
    if not course:
        raise HTTPException(status_code=404, detail="No course found")
    return course