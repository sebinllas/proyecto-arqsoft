from datetime import date
from pydantic import BaseModel, Field
from pydantic import EmailStr
from typing import Optional


class Person(BaseModel):
    name: Optional[str]
    phone: Optional[str]
    email: Optional[EmailStr]
    address: Optional[str]
    birthday: Optional[str]
