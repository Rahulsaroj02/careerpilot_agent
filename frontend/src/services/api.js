import axios from 'axios';

const baseURL = import.meta.env.VITE_API_BASE_URL;

const api = axios.create({
  baseURL,
  timeout: 120000,
});

export const submitCareerRequest = (payload) =>
  api.post('/career-agent', payload);
