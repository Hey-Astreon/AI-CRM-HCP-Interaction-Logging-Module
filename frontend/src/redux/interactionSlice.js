import { createSlice } from '@reduxjs/toolkit';

const initialState = {
  hcp_name: '',
  interaction_type: 'Meeting',
  date: '',
  time: '',
  attendees: '',
  topics_discussed: '',
  materials_shared: '',
  samples_distributed: '',
  sentiment: 'Neutral',
  outcome: '',
  follow_up: ''
};

export const interactionSlice = createSlice({
  name: 'interaction',
  initialState,
  reducers: {
    setField: (state, action) => {
      const { field, value } = action.payload;
      if (field in state) {
        state[field] = value;
      }
    },
    populateFromAI: (state, action) => {
      // Merge new data over existing. Keep existing if new is empty/null, or fully overwrite depending on design.
      // Usually, we just merge all provided keys
      Object.keys(action.payload).forEach(key => {
        if (key in state && action.payload[key] !== undefined && action.payload[key] !== null) {
          state[key] = action.payload[key];
        }
      });
    },
    resetForm: () => initialState
  }
});

export const { setField, populateFromAI, resetForm } = interactionSlice.actions;

export default interactionSlice.reducer;
