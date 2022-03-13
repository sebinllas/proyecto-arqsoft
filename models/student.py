from pydantic import BaseModel
from typing import Optional
from .person import Person


class Student(Person, BaseModel):
    attendant: Person
    grade: int
    gruop: str
    state: Optional[str] = None
