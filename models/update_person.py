from pydantic import BaseModel, Field
from pydantic import EmailStr
from typing import Optional
from datetime import datetime


class Person(BaseModel):
    name: Optional[str]
    phone: Optional[str]
    email: Optional[EmailStr]
    address: Optional[str]
    birthday: Optional[datetime]
