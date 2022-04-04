from typing import Optional
from uuid import uuid4
from pydantic import UUID4, BaseModel, Field
from .update_student import Student
import datetime


class Enrollemnt(BaseModel):
    date: str = 'yyyy-mm-dd'
    student: Optional[Student]
