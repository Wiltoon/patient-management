from sqlalchemy.orm import Session
from ..models.patient import Patient, PatientCreate, PatientUpdate, PatientModel
from ..repositories.patient_repository import get_patient_by_id, create_patient, update_patient, delete_patient, get_all_patients

def get_patient(db: Session, patient_id: int):
    patientModel: PatientModel = get_patient_by_id(db, patient_id)
    patient = Patient(
        id=patientModel.id,
        name=patientModel.name,
        age=patientModel.age,
        email=patientModel.email
    )
    return patient

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
    patient_update = Patient(
        id=patient_id,
        name=patient_data.name,
        age=patient_data.age,
        email=patient_data.email
    )
    return update_patient(db, patient_update)

def delete_patient_data(db: Session, patient_id: int):
    patient = get_patient_by_id(db, patient_id)
    if not patient:
        return None
    return delete_patient(db, patient)