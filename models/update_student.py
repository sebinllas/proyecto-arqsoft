from pydantic import BaseModel
from typing import Optional
from .update_person import Person


class Student(Person, BaseModel):
    attendant: Optional[Person]
    grade: Optional[int]
    gruop: Optional[str]
    state: Optional[str] = None
