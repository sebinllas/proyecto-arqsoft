from typing import Optional
from uuid import uuid4
from pydantic import UUID4, BaseModel, Field
from .update_student import Student
from datetime import datetime


class Enrollemnt(BaseModel):
    date: datetime = datetime.now()
    student: Optional[Student]
