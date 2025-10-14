from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from ..Entity.TeacherEntity import teacherSchema as schema
from ..DatabaseConnection import get_db
from ..Service.teacherServ import teacherService

router = APIRouter(prefix="/teachers", tags=["teachers"])
teach_serv = teacherService()

@router.post("/create", response_model=schema.TeacherRead)
def create_teacher(teach: schema.TeacherCreate, db: Session=Depends(get_db)):
    return teach_serv.create_teacher(db, teach)

@router.get("/all", response_model=list[schema.TeacherRead])
def get_teacher_list(skip: int=0, limit: int=100, db:Session=Depends(get_db)):
    return teach_serv.get_all_teacher(db, skip, limit)