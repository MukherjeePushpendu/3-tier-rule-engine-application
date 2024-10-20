CREATE TABLE rules (
    id SERIAL PRIMARY KEY,
    rule_string TEXT NOT NULL,
    ast JSONB NOT NULL
);

CREATE TABLE metadata (
    id SERIAL PRIMARY KEY,
    key VARCHAR(255) NOT NULL,
    value TEXT NOT NULL
);
