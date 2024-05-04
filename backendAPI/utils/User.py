from models.User import Users
from configs.extensions import DBSession as db
from dependencies.security import get_hashed_password

def check_user_exist(email: str):
    data = (db.query(Users)
            .filter_by(email=email)
            .one_or_none())
    return data

def add_user(data):
    user = Users(
            email=data.email,
            full_name=data.full_name,
            username=data.username,
            password=get_hashed_password(data.password),
        )
    db.add(user)
    db.flush()
    return user

