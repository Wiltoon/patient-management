import React, { useEffect, useState } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import PatientForm from '../PatientForm/index.tsx';

const EditPatient = () => {
  const { id } = useParams();
  const navigate = useNavigate();
  const [initialData, setInitialData] = useState(null);

  useEffect(() => {
    fetch(`/patients/${id}`)
      .then(response => response.json())
      .then(data => setInitialData(data));
  }, [id]);

  const handleEditPatient = (patient) => {
    fetch(`/patients/${id}`, {
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
    <div>
      <h1>Edit Patient</h1>
      {initialData && <PatientForm initialData={initialData} onSubmit={handleEditPatient} />}
    </div>
  );
};

export default EditPatient;