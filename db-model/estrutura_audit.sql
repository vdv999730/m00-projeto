-- db-model/estrutura_audit.sql

CREATE TABLE IF NOT EXISTS audit_logs (
    id SERIAL PRIMARY KEY,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
    user_id INTEGER,
    action VARCHAR(255) NOT NULL,
    details TEXT
);
