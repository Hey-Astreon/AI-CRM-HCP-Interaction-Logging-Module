CREATE TABLE IF NOT EXISTS interactions (
    id SERIAL PRIMARY KEY,
    hcp_name VARCHAR(255) NOT NULL,
    interaction_type VARCHAR(50),
    date DATE,
    time TIME,
    topics_discussed TEXT,
    materials_shared TEXT,
    samples_distributed TEXT,
    sentiment VARCHAR(50),
    outcome TEXT,
    follow_up TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
