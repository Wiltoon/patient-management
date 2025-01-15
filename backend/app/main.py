from fastapi import FastAPI
from .routes import patient

app = FastAPI()

app.include_router(patient.router)
