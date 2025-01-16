from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel, Field

Base = declarative_base()

class PatientCreate(BaseModel):
    name: str
    age: int
    email: str

    class Config:
        from_attributes = True

class PatientUpdate(BaseModel):
    id: int
    name: str
    age: int
    email: str

    class Config:
        from_attributes = True

class Patient(BaseModel):
    id: int = Field(default=None)
    name: str
    age: int
    email: str
    
    def as_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "age": self.age,
            "email": self.email
        }

    class Config:
        from_attributes = True

class PatientModel(Base):
    __tablename__ = "patients"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, nullable=False)
    age = Column(Integer)
    email = Column(String, unique=True, index=True)

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}