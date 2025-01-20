import React, { useEffect, useState } from 'react';
import { fetchPatients } from '../../services/api';
import { Container, Title, List, ListItem, PatientInfo, InfoRow, AddLink, EditLink, FilterInput, SearchContainer, SearchButton, ScheduleButton, ButtonContainer } from './styles.ts';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faSearch } from '@fortawesome/free-solid-svg-icons';

const PatientList = () => {
  const [patients, setPatients] = useState([]);
  const [filter, setFilter] = useState('');
  const [filteredPatients, setFilteredPatients] = useState([]);

  useEffect(() => {
    const getPatients = async () => {
      try {
          const response = await fetchPatients();
          setPatients(response);
          setFilteredPatients(response.slice(0, 10)); // Limit initial list to 10 patients
      } catch (error) {
          console.error('Error fetching patients:', error);
      }
    };
    getPatients();
  }, []);

  const handleFilter = () => {
    const filtered = patients.filter(patient =>
      patient.name.toLowerCase().includes(filter.toLowerCase())
    );
    setFilteredPatients(filtered);
  };

  return (
    <Container>
      <Title>Patients</Title>
      <SearchContainer>
        <FilterInput
          type="text"
          placeholder="Filter by name"
          value={filter}
          onChange={e => setFilter(e.target.value)}
        />
        <SearchButton onClick={handleFilter}>
          <FontAwesomeIcon icon={faSearch} />
        </SearchButton>
      </SearchContainer>
      <AddLink to="/patients/new">Add New Patient</AddLink>
      <List>
        {filteredPatients && filteredPatients.length > 0 ? (
          filteredPatients.map(patient => (
            <ListItem key={patient.id}>
              <PatientInfo>
                <InfoRow>
                  <strong>Name:</strong> {patient.name}
                </InfoRow>
                <InfoRow>
                  <strong>Age:</strong> {patient.age}
                </InfoRow>
                <InfoRow>
                  <strong>Address:</strong> {patient.email}
                </InfoRow>
              </PatientInfo>
              <ButtonContainer>
                <EditLink to={`/patients/${patient.id}/edit`}>Edit</EditLink>
                <ScheduleButton>Schedule Appointment</ScheduleButton>
              </ButtonContainer>
            </ListItem>
          ))
        ) : (
          <ListItem>No patients found</ListItem>
        )}
      </List>
    </Container>
  );
};

export default PatientList;