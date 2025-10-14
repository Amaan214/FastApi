from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..Entity.StudentEntity import studentSchema as schema
from ..DatabaseConnection import get_db
from ..Service.studentServ import studentService

router = APIRouter(prefix="/students", tags=["students"])
std_serv = studentService()

@router.post("/create", response_model=schema.StudentRead)
def create_student(std: schema.StudentCreate, db: Session=Depends(get_db)):
    existing = std_serv.get_student_by_id(db, std.student_id)
    if existing:
        raise HTTPException(status_code=400, detail="Student already already registered with this id")
    return std_serv.create_student(db, std)

@router.get("/id/{student_id}", response_model=schema.StudentRead)
def read_student(student_id: int, db:Session=Depends(get_db)):
    student = std_serv.get_student_by_id(db, student_id)
    if not student:
        raise HTTPException(status_code=404, detail="No such id exists")
    return student

@router.get("/all", response_model=list[schema.StudentRead])
def get_student_list(skip: int=0, limit: int=100, db: Session=Depends(get_db)):
    return std_serv.get_all_students(db, skip, limit)