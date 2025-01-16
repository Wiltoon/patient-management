import config from '../config';

export const fetchPatients = async () => {
  const response = await fetch(`${config.backendUrl}/patients`);
  if (!response.ok) {
    throw new Error('Network response was not ok');
  }
  return response.json();
};