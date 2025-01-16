import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import PatientList from './components/PatientList/index.tsx';
import AddPatient from './components/AddPatient/index.jsx';
import EditPatient from './components/EditPatient/index.jsx';

const App = () => {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<PatientList />} />
        <Route path="/patients/new" element={<AddPatient />} />
        <Route path="/patients/:id/edit" element={<EditPatient />} />
      </Routes>
    </Router>
  );
};

export default App;