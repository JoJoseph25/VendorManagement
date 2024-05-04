from pydantic import BaseModel

class UserSingup(BaseModel):
    email : str
    username : str
    full_name: str
    password: str

    class Config:
        json_schema_extra = {
            "example": {
                "email": "dummy@mail.com",
                "username": "demo_user",
                "full_name": "John Doe",
                "password": "password",
            }
        }