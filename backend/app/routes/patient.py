from fastapi import APIRouter
from ..models.patient import Patient

router = APIRouter()

@router.get("/patients/{patient_id}", response_model=Patient)
def get_patient(patient_id: int):
    # Aqui você simula a busca de um paciente, futuramente com banco de dados
    return Patient(id=patient_id, name="John Doe", age=45, diagnosis="Flu")
