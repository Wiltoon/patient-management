import os
from fastapi_users import FastAPIUsers
from fastapi_users.db import SQLAlchemyUserDatabase
from fastapi_users.authentication import JWTStrategy, AuthenticationBackend, BearerTransport
from ..models.user import User, UserCreate, UserRead, get_user_db
from ..models.patient import Patient, PatientCreate, PatientUpdate

SECRET = os.getenv("SECRET_KEY")

bearer_transport = BearerTransport(tokenUrl="/auth/login")

def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(secret=SECRET, lifetime_seconds=3600)


jwt_backend = AuthenticationBackend(
    name="jwt",
    transport=bearer_transport,
    get_strategy=get_jwt_strategy,
)

fastapi_init = FastAPIUsers(
    get_user_db,
    [jwt_backend],
)

current_user = fastapi_init.current_user()