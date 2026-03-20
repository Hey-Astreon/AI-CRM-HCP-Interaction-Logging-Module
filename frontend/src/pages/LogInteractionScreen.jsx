import React from 'react';
import LogInteractionForm from '../components/LogInteractionForm';
import AIChatPanel from '../components/AIChatPanel';

const LogInteractionScreen = () => {
  return (
    <div className="app-container">
      <h1 className="page-title">Log HCP Interaction</h1>
      
      <div className="main-content">
        <div className="left-panel">
          <LogInteractionForm />
        </div>
        
        <div className="right-panel">
          <AIChatPanel />
        </div>
      </div>
    </div>
  );
};

export default LogInteractionScreen;
