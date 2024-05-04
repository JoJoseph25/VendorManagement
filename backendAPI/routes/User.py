from uuid import uuid4
from schemas.User import UserSingup
# from configs.extensions import logger
from fastapi.responses import JSONResponse
from configs.extensions import DBSession as db
from utils.User import check_user_exist, add_user
from fastapi import  HTTPException, APIRouter, Path, Depends, Request, Query

router = APIRouter()

@router.post(
    '/signup',
    tags=["User"], status_code=201,
    summary="Add User Signup",
    # responses={**clientCredits_Responses},
    )
def signup(request: Request, data: UserSingup):
    """
    User signup Route
    """
    try:
        user = check_user_exist(data.email)
        if user is None:
            user = add_user(data)
            db.commit()
            result = {
                'message': 'User Created',
                'user': user
            }
            status_code = 201
        else:
            status_code = 400
            result = {
                'message': f'User already exists.',
                'status': False
            }
    except Exception as e:
        request.app.logger.error(e)
        status_code = 500
        result = {
                'message': 'Unexpected Error',
                'status': False
            }
    finally:
        return JSONResponse(content=result, status_code=status_code)
 