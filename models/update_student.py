from pydantic import BaseModel
from typing import Optional
from .update_person import Person


class Student(Person, BaseModel):
    attendant: Optional[Person]
    grade: Optional[int]
    group: Optional[str]
    state: Optional[str] = None
