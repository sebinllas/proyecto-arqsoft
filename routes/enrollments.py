from fastapi import APIRouter, Depends, HTTPException, status
from models.enrollment import Enrollemnt
from typing import List
from database.database import enrollments, students, admins
from routes.admin import auth_handler

router = APIRouter(
    prefix="/enrollments",
    tags=["Enrollments"],
    responses={404: {"description": "Not found"}},
    dependencies=[Depends(auth_handler.auth_wrapper)]
)


@router.get("/", response_model=List[Enrollemnt], )
def get_all_enrollments():
    enrollments_list = [i for i in enrollments.find()]
    for i in enrollments_list:
        i['student'] = students.find_one({'_id': i['student']['_id']})
    return [Enrollemnt(**item) for item in enrollments_list]


@router.get("/{id}")
def get_enrollment(id):
    enrollment = enrollments.find_one({'_id': id})
    if enrollment:
        student = students.find_one({'_id': enrollment['student']['_id']})
        enrollment['student'] = student
        return enrollment
    return HTTPException(status.HTTP_404_NOT_FOUND, 'Data not found')


@router.post("/", status_code=status.HTTP_201_CREATED)
def new_enrollment(enrollment: Enrollemnt):
    new_enrollment = enrollment.dict(by_alias=True)
    student = enrollment.student.dict(by_alias=True)
    new_enrollment['student'] = {'_id': enrollment.student.id, }
    students.insert_one(student)
    enrollments.insert_one(new_enrollment)
    return 'saved'


@router.put("/{id}")
def update_enrollment(id: str, new_enrollment: Enrollemnt):
    return f'update enrollment {id}, to {new_enrollment}'


@router.delete('/{id}')
def delete_enrollment(id: str):
    return f'delete enrollment {id}'
