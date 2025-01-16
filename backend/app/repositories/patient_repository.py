from sqlalchemy.orm import Session
from ..models.patient import Patient, PatientModel

def get_patient_by_id(db: Session, patient_id: int):
    return db.query(Patient).filter(Patient.id == patient_id).first()

def get_all_patients(db: Session):
    return db.query(PatientModel).all()

def create_patient(db: Session, patient: Patient):
    db_patient = PatientModel(
        name=patient.name,
        age=patient.age,
        email=patient.email
    )
    db.add(db_patient)
    db.commit()
    db.refresh(db_patient)
    return db_patient

def update_patient(db: Session, existing_patient: Patient, updated_data: dict):
    for key, value in updated_data.items():
        setattr(existing_patient, key, value)
    db.commit()
    db.refresh(existing_patient)
    return existing_patient

def delete_patient(db: Session, patient: Patient):
    db.delete(patient)
    db.commit()
    return patient