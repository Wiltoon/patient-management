import React, { useState } from 'react';
import { Form, Input, Button, Label, Container } from './styles.ts';

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
    <Container>
      <Form onSubmit={handleSubmit}>
        <div>
          <Label>Name:</Label>
          <Input type="text" value={name} onChange={(e) => setName(e.target.value)} required />
        </div>
        <div>
          <Label>Age:</Label>
          <Input type="number" value={age} onChange={(e) => setAge(e.target.value)} required />
        </div>
        <div>
          <Label>Email:</Label>
          <Input type="text" value={email} onChange={(e) => setEmail(e.target.value)} required />
        </div>
        <Button type="submit">Submit</Button>
      </Form>
    </Container>
  );
};

export default PatientForm;