from pydantic import BaseModel
from typing import Optional
from .person import Person


class Student(Person, BaseModel):
    attendant: Person
    grade: int
    group: str
    state: Optional[str] = None
