CREATE TABLE IF NOT EXISTS persons (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    phone VARCHAR(20)
);

INSERT INTO persons (name, phone) VALUES
('Alice', '555-1234'),
('Bob', '555-5678'),
('Charlie', '555-8765');
