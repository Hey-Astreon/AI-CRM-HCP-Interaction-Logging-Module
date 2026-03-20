import React, { useState } from 'react';
import { useDispatch } from 'react-redux';
import { populateFromAI } from '../redux/interactionSlice';
import { sendChatMessage } from '../services/api';
import { Bot, Send } from 'lucide-react';

const AIChatPanel = () => {
  const [inputText, setInputText] = useState('');
  const [loading, setLoading] = useState(false);
  const dispatch = useDispatch();

  const handleLogInteraction = async () => {
    if (!inputText.trim()) return;
    
    setLoading(true);
    try {
      const result = await sendChatMessage(inputText);
      
      // The backend returns { reply: string, formUpdates: object | null }
      if (result && result.formUpdates) {
        dispatch(populateFromAI(result.formUpdates));
      }
      
      // Optionally handle the 'reply' if we want to show it in the chat area
      // For now, we'll just clear the input if it was successful
      setInputText('');
    } catch (error) {
      console.error('Failed to log interaction via AI:', error);
      alert('Failed to process text with AI. Is the backend running?');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="card chat-container">
      <div className="chat-header">
        <Bot size={20} color="#3b82f6" />
        AI Assistant
      </div>
      <p className="chat-subtitle">Log interaction via chat</p>

      <div className="chat-log-area">
        <div className="chat-example-box">
          Log interaction details here (e.g., "Met Dr. Smith, discussed Product X efficacy, positive sentiment, shared brochure") or ask for help.
        </div>
      </div>

      <div className="chat-input-row">
        <input
          type="text"
          className="chat-input"
          placeholder="Describe interaction..."
          value={inputText}
          onChange={(e) => setInputText(e.target.value)}
          onKeyDown={(e) => e.key === 'Enter' && handleLogInteraction()}
          disabled={loading}
        />
        <button className="log-action-btn" onClick={handleLogInteraction} disabled={loading} style={{ display: 'flex', alignItems: 'center', gap: '8px' }}>
          {loading ? '...' : <><Send size={16} /> <span>Log</span></>}
        </button>
      </div>
    </div>
  );
};

export default AIChatPanel;
