import React from 'react';

const FormSection = ({ title, children, noMargin }) => {
  return (
    <div style={{ marginBottom: noMargin ? 0 : '24px' }}>
      {title && <h3 className="card-title" style={{ marginBottom: '16px' }}>{title}</h3>}
      {children}
    </div>
  );
};

export default FormSection;
