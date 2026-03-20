import axios from 'axios';

const api = axios.create({
  baseURL: 'http://127.0.0.1:8000',
  headers: {
    'Content-Type': 'application/json',
  },
});

export const sendChatMessage = async (message) => {
  try {
    const response = await api.post('/ai/chat', { message });
    return response.data;
  } catch (error) {
    console.error('Error sending chat message:', error);
    throw error;
  }
};

export const logInteraction = async (interactionData) => {
  try {
    const response = await api.post('/interaction/log', interactionData);
    return response.data;
  } catch (error) {
    console.error('Error logging interaction:', error);
    throw error;
  }
};

export default api;
