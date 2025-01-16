import React, { useState, useEffect } from 'react';

interface InitialData {
  name?: string;
  age?: string;
  email?: string;
}

const PatientForm = ({ onSubmit, initialData = {} as InitialData }) => {
  const [name, setName] = useState(initialData.name || '');
  const [age, setAge] = useState(initialData.age || '');
  const [email, setEmail] = useState(initialData.email || '');

  const handleSubmit = (e) => {
    e.preventDefault();
    onSubmit({ name, age, email });
  };

  return (
    <form onSubmit={handleSubmit}>
      <div>
        <label>Name:</label>
        <input type="text" value={name} onChange={(e) => setName(e.target.value)} required />
      </div>
      <div>
        <label>Age:</label>
        <input type="number" value={age} onChange={(e) => setAge(e.target.value)} required />
      </div>
      <div>
        <label>Email:</label>
        <input type="text" value={email} onChange={(e) => setEmail(e.target.value)} required />
      </div>
      <button type="submit">Submit</button>
    </form>
  );
};

export default PatientForm;