from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm.session import Session
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from db.database import get_db
from db.models import DbUser
from db.hash import Hash
from auth import oauth2

router = APIRouter(
    tags=['authentication']
)


# 需要与 oauth2.py 中的tokenUrl一致
@router.post('/token')
def get_token(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(DbUser).filter(DbUser.username == request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Invalid credentials')
    if not Hash.verify(user.password, request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Incorrect password')

    access_token = oauth2.create_access_token(data={'sub': user.username})

    return {
        'access_token': access_token,
        'token_type': 'bearer',  # 不记名的令牌
        'user_id': user.id,
        'user_name': user.username,
    }
