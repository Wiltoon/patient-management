from .models.user import User, UserCreate, UserRead, get_user_db
from app.config.database import get_db
from .config.initializes import fastapi_init, get_jwt_strategy, jwt_backend
from fastapi import FastAPI, Depends
from .routes import patient
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

jwt_strategy = get_jwt_strategy()
jwt_strategy.name = jwt_backend.name
jwt_strategy.get_strategy = jwt_backend.get_strategy
jwt_strategy.transport = jwt_backend.transport

# app.include_router(fastapi_init.get_auth_router(jwt_strategy), prefix="/auth", tags=["auth"])
# app.include_router(fastapi_init.get_auth_router(UserRead, UserCreate), prefix="/auth", tags=["auth"])
app.include_router(patient.router)
