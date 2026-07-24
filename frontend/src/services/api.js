import axios from 'axios';

const api = axios.create({
  baseURL: 'http://localhost:8000',
  timeout: 120000,
});

export const submitCareerRequest = (payload) => api.post('/career-agent', payload);
