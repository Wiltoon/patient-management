from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from ..models.patient import Patient, PatientCreate, PatientUpdate
from ..config.database import get_db
from ..services.patient_service import get_patient, save_patient, update_patient_data, delete_patient_data, get_patients
from typing import List

router = APIRouter()

def get_db_session():
    db = next(get_db())
    try:
        yield db
    finally:
        db.close()

@router.get("/patients/{patient_id}", response_model=Patient)
def get_patient_route(patient_id: int, db: Session = Depends(get_db_session)):
    patient = get_patient(db, patient_id)
    if not patient:
        raise HTTPException(status_code=404, detail="Patient not found")
    return patient

@router.get("/patients", response_model=List[Patient])
def get_patient_route(db: Session = Depends(get_db_session)):
    patients = get_patients(db)
    if not patients:
        raise HTTPException(status_code=404, detail="Patient not found")
    return patients

@router.post("/patients", response_model=Patient)
def save_patient_route(patient: PatientCreate, db: Session = Depends(get_db_session)):
    print(patient)
    return save_patient(db, patient)

@router.put("/patients/{patient_id}", response_model=Patient)
def update_patient_route(patient_id: int, patient: PatientUpdate, db: Session = Depends(get_db_session)):
    updated_patient = update_patient_data(db, patient_id, patient)
    if not updated_patient:
        raise HTTPException(status_code=404, detail="Patient not found")
    return updated_patient

@router.delete("/patients/{patient_id}", response_model=Patient)
def delete_patient_route(patient_id: int, db: Session = Depends(get_db_session)):
    deleted_patient = delete_patient_data(db, patient_id)
    if not deleted_patient:
        raise HTTPException(status_code=404, detail="Patient not found")
    return deleted_patient