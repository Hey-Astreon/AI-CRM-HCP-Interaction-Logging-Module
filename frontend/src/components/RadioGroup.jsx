import React from 'react';

const RadioGroup = ({ label, name, options, value, onChange }) => {
  return (
    <div className="radio-group-container">
      {label && <label className="form-label">{label}</label>}
      <div className="radio-group">
        {options.map((option) => (
          <label key={option.value} className="radio-item">
            <input
              type="radio"
              name={name}
              value={option.value}
              checked={value === option.value}
              onChange={(e) => onChange(e.target.value)}
              className="radio-input"
            />
            <span className="radio-label">
              {option.icon && <span className="sentiment-icon">{option.icon}</span>}
              {option.label}
            </span>
          </label>
        ))}
      </div>
    </div>
  );
};

export default RadioGroup;
