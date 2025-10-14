from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..Entity.CourseEntity import courseSchema as schema
from ..DatabaseConnection import get_db
from ..Service.courseServ import courseService 

router = APIRouter(prefix="/courses", tags=["courses"])
crse_serv = courseService()

@router.post("/create", response_model=schema.CourseRead)
def create_course(course: schema.CourseCreate, db: Session=Depends(get_db)):
    return crse_serv.create_course(db, course)

@router.get("/all", response_model=list[schema.CourseRead])
def get_all_courses(skip: int=0, limit: int=100, db: Session=Depends(get_db)):
    return crse_serv.get_all_courses(db, skip, limit)

# Adding student to the course
@router.post("/{course_id}/addStudent/{student_id}", response_model=schema.CourseRead)
def enroll_student(course_id: int, student_id: int, db: Session=Depends(get_db)):
    course = crse_serv.add_student_to_course(db, student_id, course_id)
    if not course:
        raise HTTPException(status_code=404, detail="No course found")
    return course

@router.post("/{course_id}/deleteStudent/{student_id}", response_model=schema.CourseRead)
def unenroll_student(course_id: int, student_id: int, db: Session=Depends(get_db)):
    course = crse_serv.remove_student_from_course(db, student_id, course_id)
    if not course:
        raise HTTPException(status_code=404, detail="No course found")
    return course