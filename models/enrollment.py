from uuid import uuid4
from pydantic import UUID4, BaseModel, Field
from .student import Student
from datetime import datetime
#from pymongo import ObjectId


class Enrollemnt(BaseModel):
    id: UUID4 = Field(alias="_id", default_factory=uuid4)
    date: datetime = datetime.now()
    student: Student
