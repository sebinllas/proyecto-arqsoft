from pydantic import BaseModel, Field
from pydantic import EmailStr
from typing import Optional


class Person(BaseModel):
    id: str = Field(alias='_id')
    name: str
    phone: Optional[str]
    email: Optional[EmailStr]
    address: Optional[str]
    birthday: Optional[str]
