from ..DatabaseConnection import Database
from .StudentEntity.studentSchema import StudentRead
from .CourseEntity.courseSchema import CourseRead
from .TeacherEntity.teacherSchema import TeacherRead

db = Database()
Base = db.Base

# These are mentioned here because both of them use forward reference
StudentRead.model_rebuild()
CourseRead.model_rebuild()
TeacherRead.model_rebuild()