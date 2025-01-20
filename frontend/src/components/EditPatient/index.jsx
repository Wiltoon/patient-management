import React, { useEffect, useState } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import PatientForm from '../PatientForm/index.tsx';
import config from '../../config.js';
import { Container, Title } from './styles.ts';

const EditPatient = () => {
  const { id } = useParams();
  const navigate = useNavigate();
  const [initialData, setInitialData] = useState(null);

  useEffect(() => {
    fetch(`${config.backendUrl}/patients/${id}`)
      .then(response => response.json())
      .then(data => setInitialData(data));
  }, [id]);

  const handleEditPatient = (patient) => {
    fetch(`${config.backendUrl}/patients/${id}`, {
      method: 'PUT',
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
      <Title>Edit Patient</Title>
      {initialData && <PatientForm initialData={initialData} onSubmit={handleEditPatient} />}
    </Container>
  );
};

export default EditPatient;