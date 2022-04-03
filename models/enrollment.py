from uuid import uuid4
from pydantic import UUID4, BaseModel, Field
from .student import Student
from datetime import datetime


class Enrollemnt(BaseModel):
    id: UUID4 = Field(alias="_id", default_factory=lambda: str(uuid4()))
    date: datetime = datetime.now()
    student: Student
