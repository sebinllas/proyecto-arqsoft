from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException, status
from models.enrollment import Enrollemnt
from models.student import Student
from models.update_enrollment import Enrollemnt as UpdateEnrollment
from typing import List
from database.database import enrollments, students, admins
from routes.auth import auth_handler

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


@router.get("/{id}", response_model=Enrollemnt)
def get_enrollment(id):

    enrollment = enrollments.find_one({'_id': id})
    if enrollment:
        student = students.find_one({'_id': enrollment['student']['_id']})
        enrollment['student'] = student
        return Enrollemnt(**enrollment)
    raise HTTPException(status.HTTP_404_NOT_FOUND, 'Data not found')


@router.post("/", status_code=status.HTTP_201_CREATED)
def new_enrollment(enrollment: Enrollemnt):
    new_enrollment = enrollment.dict(by_alias=True)
    student = enrollment.student.dict(by_alias=True)
    new_enrollment['student'] = {'_id': enrollment.student.id, }
    old_student = students.find_one({'_id': enrollment.student.id})
    if old_student:
        students.update_one({'_id': enrollment.student.id}, {
                            '$set': {**student}})
    else:
        students.insert_one(student)
    enrollments.insert_one(new_enrollment)
    return 'saved'


@router.patch("/{id}")
def update_enrollment(id: str, new_enrollment: UpdateEnrollment):
    new_data_enrollment = new_enrollment.dict(exclude_unset=True)
    modified_count = 0
    enrollment = enrollments.find_one({'_id': id})
    print('enrollment antiguo', enrollment)
    print('std ID: ', enrollment['student']['_id'])

    if not enrollment:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
    student = students.find_one({'_id': enrollment['student']['_id']})
    print('student antiguo: ', student)
    if 'student' in new_data_enrollment.keys():
        new_data_student = new_data_enrollment.pop('student')
        if 'attendant' in new_data_student.keys():
            new_data_attendant = student['attendant']
            new_data_attendant.update(new_data_student['attendant'])
            new_data_student['attendant'] = new_data_attendant
        print(new_data_student)
        result_student = students.update_one({'_id': enrollment['student']['_id']}, {
                                             '$set': {**new_data_student}})
        modified_count += result_student.modified_count

    result_enrollment = enrollments.update_one({'_id':  id}, {
        "$set": {**new_data_enrollment}})
    modified_count += result_enrollment.modified_count
    if modified_count == 0:
        return "Given values equal than the stored ones"
    return "Updated successfully"


@router.delete('/{id}')
def delete_enrollment(id: str):
    result = enrollments.delete_one({'_id':  id})
    print(result.deleted_count)
    if result.deleted_count:
        return 'Deleted successfully'
    raise HTTPException(status.HTTP_404_NOT_FOUND,
                        detail=f'No items with id {id}')
