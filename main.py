from fastapi import FastAPI
from . import Base, engine
from .Controller import StudentController, TeacherController, CourseController

Base.metadata.create_all(bind=engine)

app = FastAPI()

# Now including routers
app.include_router(StudentController.router)
app.include_router(TeacherController.router)
app.include_router(CourseController.router)

# Root
@app.get("/")
def root():
    return {"msg": "Class Project API"}