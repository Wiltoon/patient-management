import React from 'react';
import { useNavigate } from 'react-router-dom';
import PatientForm from '../PatientForm/index.tsx';
import config from '../../config.js';

const AddPatient = () => {
  const navigate = useNavigate();

  const handleAddPatient = (patient) => {
    fetch(`${config.backendUrl}/patients`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(patient),
    })
      .then(response => response.json())
      .then(() => navigate('/'));
  };

  return (
    <div>
      <h1>Add New Patient</h1>
      <PatientForm onSubmit={handleAddPatient} />
    </div>
  );
};

export default AddPatient;