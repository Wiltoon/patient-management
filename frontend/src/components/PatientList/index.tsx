import React, { useEffect, useRef, useState } from 'react';
import { Link } from 'react-router-dom';
import { fetchPatients } from '../../services/api';

const PatientList = () => {
  const [patients, setPatients] = useState([]);
  const firstLoad = useRef(true);

  useEffect(() => {
    if (firstLoad.current) {
      firstLoad.current = false;
      return;
    }
    const getPatients = async () => {
      try {
          const response = await fetchPatients();
          setPatients(response);
      } catch (error) {
          console.error('Error fetching patients:', error);
      }
    };
    getPatients();
  }, []);

  return (
    <div>
      <h1>Patients</h1>
      <Link to="/patients/new">Add New Patient</Link>
      <ul>
      {patients && patients.length > 0 ? (
        patients.map(patient => (
          <li key={patient.id}>
            {patient.name} - {patient.age} - {patient.address}
            <Link to={`/patients/${patient.id}/edit`}>Edit</Link>
          </li>
        ))
      ) : (
        <li>No patients found</li>
      )}
    </ul>
    </div>
  );
};

export default PatientList;