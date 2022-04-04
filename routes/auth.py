from fastapi import APIRouter, status, HTTPException
from security.auth import AuthHandler
from models.user_auth import userAuth
from database.database import admins

router = APIRouter(
    tags=["auth"],
    responses={status.HTTP_401_UNAUTHORIZED: {"description": "Not found"}},
)
auth_handler = AuthHandler()


@router.post('/register', status_code=201)
def register(auth_details: userAuth):
    if admins.find_one({'username': auth_details.username}):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail='Username is taken')
    hashed_password = auth_handler.get_password_hash(auth_details.password)
    admins.insert_one({
        'username': auth_details.username,
        'password': hashed_password
    })
    token = auth_handler.encode_token(auth_details.username)
    return {'token': token, 'username': auth_details.username}


@router.post('/login')
def login(auth_details: userAuth):
    user = admins.find_one({'username': auth_details.username})
    if (user is None) or (not auth_handler.verify_password(auth_details.password, user['password'])):
       return { 'status':False, 'token': 'error', 'username': 'error'}
    token = auth_handler.encode_token(user['username'])
    return { 'status':True, 'token': token, 'username': auth_details.username}
