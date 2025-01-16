from sqlalchemy.orm import Session
from ..models.patient import Patient, PatientCreate, PatientUpdate, PatientModel
from ..repositories.patient_repository import get_patient_by_id, create_patient, update_patient, delete_patient, get_all_patients

def get_patient(db: Session, patient_id: int):
    return get_patient_by_id(db, patient_id)

def get_patients(db: Session):
    patientsModels: PatientModel = get_all_patients(db)
    patients = [
        Patient(
            id=patient.id,
            name=patient.name,
            age=patient.age,
            email=patient.email
        ) for patient in patientsModels]
    return patients

def save_patient(db: Session, patient_data: PatientCreate):
    new_patient = Patient(
        name=patient_data.name,
        age=patient_data.age,
        email=patient_data.email
    )
    return create_patient(db, new_patient)

def update_patient_data(db: Session, patient_id: int, patient_data: PatientUpdate):
    existing_patient = get_patient_by_id(db, patient_id)
    if not existing_patient:
        return None
    return update_patient(db, existing_patient, patient_data.dict())

def delete_patient_data(db: Session, patient_id: int):
    patient = get_patient_by_id(db, patient_id)
    if not patient:
        return None
    return delete_patient(db, patient)