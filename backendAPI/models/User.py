import bcrypt
from uuid import uuid4
from configs.extensions import dbModel

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.postgresql import UUID, JSON
from sqlalchemy import ForeignKey, Integer, Boolean, Float, String, DateTime

class Users(dbModel):
    __tablename__ = "users"

    id: Mapped[uuid4] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    username: Mapped[str]  = mapped_column(String(128), unique=True, nullable=False)
    email: Mapped[str]  = mapped_column(String(128), unique=True, nullable=False)
    password: Mapped[str]  = mapped_column(String(256), nullable=False)
    full_name: Mapped[str]  = mapped_column(String(256), nullable=False)
    disabled: Mapped[str]  = mapped_column(Boolean, nullable=False, default=False)

    def __init__(self, username, email, password, full_name):
        self.username = username
        self.email = email
        self.password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        self.full_name = full_name
        self.disabled = False

    def __repr__(self):
        return f'<Users {self.username}>'
    
