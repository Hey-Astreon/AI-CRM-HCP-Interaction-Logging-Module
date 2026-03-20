import React from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { setField } from '../redux/interactionSlice';
import RadioGroup from './RadioGroup';
import FormSection from './FormSection';
import { Mic, Search, Plus } from 'lucide-react';
import { Smile, Meh, Frown } from 'lucide-react';

const LogInteractionForm = () => {
  const dispatch = useDispatch();
  const formData = useSelector((state) => state.interaction);

  const handleChange = (field, value) => {
    dispatch(setField({ field, value }));
  };

  const sentimentOptions = [
    { value: 'Positive', label: 'Positive', icon: <Smile size={16} className="positive-icon" /> },
    { value: 'Neutral', label: 'Neutral', icon: <Meh size={16} className="neutral-icon" /> },
    { value: 'Negative', label: 'Negative', icon: <Frown size={16} className="negative-icon" /> }
  ];

  return (
    <div className="card hcp-form">
      <h2 className="card-title" style={{ fontSize: '18px', color: '#1f2937', marginBottom: '16px' }}>Interaction Details</h2>

      <div className="form-row">
        <div className="form-group">
          <label className="form-label">HCP Name</label>
          <input
            type="text"
            className="form-input"
            placeholder="Search or select HCP..."
            value={formData.hcp_name || ''}
            onChange={(e) => handleChange('hcp_name', e.target.value)}
          />
        </div>
        <div className="form-group">
          <label className="form-label">Interaction Type</label>
          <select
            className="form-select"
            value={formData.interaction_type || 'Meeting'}
            onChange={(e) => handleChange('interaction_type', e.target.value)}
          >
            <option value="Meeting">Meeting</option>
            <option value="Call">Call</option>
            <option value="Conference">Conference</option>
          </select>
        </div>
      </div>

      <div className="form-row">
        <div className="form-group">
          <label className="form-label">Date</label>
          <div className="date-time-container">
            <input
              type="date"
              className="form-input"
              value={formData.date || ''}
              onChange={(e) => handleChange('date', e.target.value)}
            />
          </div>
        </div>
        <div className="form-group">
          <label className="form-label">Time</label>
          <div className="date-time-container">
            <input
              type="time"
              className="form-input"
              value={formData.time || ''}
              onChange={(e) => handleChange('time', e.target.value)}
            />
          </div>
        </div>
      </div>

      <div className="form-group">
        <label className="form-label">Attendees</label>
        <input
          type="text"
          className="form-input"
          placeholder="Enter names or search..."
          value={formData.attendees || ''}
          onChange={(e) => handleChange('attendees', e.target.value)}
        />
      </div>

      <div className="form-group">
        <label className="form-label">Topics Discussed</label>
        <textarea
          className="form-textarea"
          placeholder="Enter key discussion points..."
          value={formData.topics_discussed || ''}
          onChange={(e) => handleChange('topics_discussed', e.target.value)}
        />
        <button className="summarize-btn">
          <Mic size={16} /> Summarize from Voice Note (Requires Consent)
        </button>
      </div>

      <FormSection title="Materials Shared / Samples Distributed">
        <div className="list-section-title">Materials Shared</div>
        <div className="list-container">
          <span className="list-empty-msg">{formData.materials_shared || 'No materials added.'}</span>
          <button className="action-btn"><Search size={14} /> Search/Add</button>
        </div>

        <div className="list-section-title">Samples Distributed</div>
        <div className="list-container">
          <span className="list-empty-msg">{formData.samples_distributed || 'No samples added.'}</span>
          <button className="action-btn"><Plus size={14} /> Add Sample</button>
        </div>
      </FormSection>

      <RadioGroup
        label="Observed/Inferred HCP Sentiment"
        name="sentiment"
        options={sentimentOptions}
        value={formData.sentiment || 'Neutral'}
        onChange={(val) => handleChange('sentiment', val)}
      />

      <div className="form-group">
        <label className="form-label">Outcomes</label>
        <textarea
          className="form-textarea"
          placeholder="Key outcomes or agreements..."
          value={formData.outcome || ''}
          onChange={(e) => handleChange('outcome', e.target.value)}
        />
      </div>

      <div className="form-group">
        <label className="form-label">Follow-up Actions</label>
        <textarea
          className="form-textarea"
          placeholder="Enter next steps or tasks..."
          value={formData.follow_up || ''}
          onChange={(e) => handleChange('follow_up', e.target.value)}
        />
        <div className="suggestions-heading">AI Suggested Follow-ups:</div>
        <ul className="suggestion-list">
          <li className="suggestion-item">Schedule follow-up meeting in 2 weeks</li>
          <li className="suggestion-item">Send OncoBoost Phase III PDF</li>
          <li className="suggestion-item">Add Dr. Sharma to advisory board invite list</li>
        </ul>
      </div>

    </div>
  );
};

export default LogInteractionForm;
