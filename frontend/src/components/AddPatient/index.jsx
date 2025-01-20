import React from 'react';
import { useNavigate } from 'react-router-dom';
import PatientForm from '../PatientForm/index.tsx';
import config from '../../config.js';
import { Container, Title } from './styles.ts';

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
    <Container>
      <Title>Add New Patient</Title>
      <PatientForm onSubmit={handleAddPatient} />
    </Container>
  );
};

export default AddPatient;